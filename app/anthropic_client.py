"""Cliente da API Anthropic (SDK `anthropic`, sem Claude Agent SDK) usado
pela interface Streamlit para analisar um caso previdenciário.

Monta um único prompt consolidado (system + user) reunindo os prompts dos
subagentes relevantes do sistema multiagente do escritório, o contexto do
escritório e os documentos do caso, e pede ao modelo que simule o fluxo
completo (triagem -> cálculo -> arquivo médico -> petição) em uma única
resposta, no formato de um bloco JSON.
"""

from __future__ import annotations

import json
from typing import Dict

import anthropic

from prompts import carregar_prompt, carregar_skill, montar_contexto_escritorio

# Únicos IDs de modelo aceitos por esta interface. Ver CLAUDE.md / instruções
# do projeto: "claude-sonnet-4-5" e "Opus 4.1" (pedidos originalmente) não
# existem na API Anthropic atual — os vigentes desta família são estes dois.
MODELOS_VALIDOS = {"claude-sonnet-5", "claude-opus-5"}

CHAVES_ESPERADAS = ("triagem", "calculo", "arquivo_medico", "peticao")

# max_tokens generoso (o retorno esperado — triagem + cálculo + análise
# médica + petição — pode somar vários milhares de tokens), dentro da faixa
# recomendada (16000-32000) e sempre com streaming para evitar timeout HTTP.
MAX_TOKENS = 32000


class ErroAnaliseCaso(Exception):
    """Erro de validação de entrada (ex.: modelo inválido) — não é um erro
    da API Anthropic em si, então não usamos as exceções do SDK aqui."""


def _montar_system_prompt() -> str:
    orquestrador = carregar_prompt("orquestrador-prev")
    return (
        "Você está atuando como o Orquestrador do sistema multiagente de um "
        "escritório de Direito Previdenciário brasileiro, descrito abaixo. "
        "Nesta interface simplificada (sem Claude Agent SDK, sem acesso a "
        "ferramentas externas como leitura de arquivos), você deve simular "
        "internamente, em uma única resposta, o trabalho que os subagentes "
        "listados fariam, usando apenas o que for fornecido na mensagem do "
        "usuário (prompts dos subagentes, contexto do escritório, "
        "documentos já extraídos e dados do formulário).\n\n"
        "## Prompt do Agente Orquestrador (.claude/agents/orquestrador-prev.md)\n"
        + orquestrador
    )


def _montar_user_prompt(
    nome_cliente: str,
    sexo: str,
    data_nascimento: str,
    beneficio: str,
    documentos: Dict[str, str],
) -> str:
    blocos = []

    blocos.append(
        "# REGRA INVIOLÁVEL DO ESCRITÓRIO (CLAUDE.md, regra 1 e regra 2)\n"
        "1. Todo output que você gerar nas 4 seções abaixo é um RASCUNHO "
        "para revisão do advogado responsável — em nenhuma hipótese uma "
        "peça ou parecer final.\n"
        "2. NUNCA invente jurisprudência, número de tema, súmula ou "
        "julgado. Se não tiver certeza absoluta, marque explicitamente "
        "[JURISPRUDÊNCIA A CONFIRMAR] no texto.\n"
        "3. NUNCA afirme diagnóstico médico sem CID explicitamente presente "
        "no documento anexado."
    )

    blocos.append("# Prompts dos Subagentes Relevantes\n")
    for nome_agente in (
        "triagem-viabilidade",
        "calculo-previdenciario",
        "analise-arquivo-medico",
    ):
        blocos.append(
            f"## Subagente: {nome_agente} (.claude/agents/{nome_agente}.md)\n"
            + carregar_prompt(nome_agente)
        )

    # A skill calculo-tempo-contribuicao detalha a metodologia determinística
    # de cruzamento CNIS x CTPS referenciada pelo subagente calculo-previdenciario.
    blocos.append(
        "## Skill de apoio: calculo-tempo-contribuicao "
        "(.claude/skills/calculo-tempo-contribuicao/SKILL.md)\n"
        + carregar_skill("calculo-tempo-contribuicao")
    )

    blocos.append("# Contexto do Escritório\n" + montar_contexto_escritorio())

    blocos.append(
        "# Dados do Formulário\n"
        f"- Nome do cliente: {nome_cliente}\n"
        f"- Sexo: {sexo}\n"
        f"- Data de nascimento: {data_nascimento}\n"
        f"- Benefício pretendido: {beneficio}\n"
    )

    blocos.append("# Documentos Anexados (texto já extraído do PDF)\n")
    if documentos:
        for nome_doc, texto in documentos.items():
            texto_seguro = (
                texto.strip()
                if texto and texto.strip()
                else "[sem texto extraível deste documento — ver aviso na interface]"
            )
            blocos.append(f"## Documento: {nome_doc}\n```\n{texto_seguro}\n```")
    else:
        blocos.append("Nenhum documento foi anexado a este caso.")

    blocos.append(
        "# Instrução Final\n"
        "Simule o fluxo completo internamente: triagem → cálculo → análise "
        "médica (se aplicável) → rascunho de petição. Retorne APENAS um "
        "único bloco JSON válido, sem texto antes ou depois, com "
        "exatamente 4 chaves: triagem, calculo, arquivo_medico, peticao — "
        "cada uma como uma string de markdown."
    )

    return "\n\n".join(blocos)


def _extrair_json(texto: str) -> Dict[str, str]:
    """Parse defensivo da resposta do modelo.

    1. Tenta `json.loads` no texto completo.
    2. Se falhar, extrai o trecho do primeiro '{' ao último '}' e tenta de
       novo (cobre casos em que o modelo, apesar da instrução, cercou o
       JSON com texto extra).
    3. Se ainda falhar, devolve um dict com uma única chave de erro
       contendo o texto bruto, para a interface exibir um aviso em vez de
       quebrar com uma exceção não tratada.
    """
    try:
        dado = json.loads(texto)
        if isinstance(dado, dict):
            return dado
    except (json.JSONDecodeError, TypeError):
        pass

    inicio = texto.find("{")
    fim = texto.rfind("}")
    if inicio != -1 and fim != -1 and fim > inicio:
        trecho = texto[inicio : fim + 1]
        try:
            dado = json.loads(trecho)
            if isinstance(dado, dict):
                return dado
        except json.JSONDecodeError:
            pass

    return {
        "erro": (
            "Não foi possível interpretar a resposta do modelo como JSON "
            "válido. O texto bruto retornado está na chave 'texto_bruto' "
            "abaixo — revise manualmente."
        ),
        "texto_bruto": texto,
    }


def analisar_caso(
    nome_cliente: str,
    sexo: str,
    data_nascimento: str,
    beneficio: str,
    documentos: Dict[str, str],
    api_key: str,
    modelo: str,
) -> Dict[str, str]:
    """Analisa um caso previdenciário chamando a API Anthropic diretamente.

    Args:
        nome_cliente, sexo, data_nascimento, beneficio: dados do formulário.
        documentos: dict {nome_do_documento: texto_extraido}.
        api_key: chave da API. Se vazia/None, o cliente é criado sem chave
            explícita (`anthropic.Anthropic()`), que resolve a credencial
            via `ANTHROPIC_API_KEY`/ambiente — a resolução a partir de
            `st.secrets` é feita pelo chamador (streamlit_app.py) antes de
            invocar esta função.
        modelo: "claude-sonnet-5" ou "claude-opus-5" (nenhum outro valor é
            aceito).

    Returns:
        Um dict com as chaves 'triagem', 'calculo', 'arquivo_medico' e
        'peticao' (strings de markdown), ou, em caso de falha no parse do
        JSON de resposta, um dict com as chaves 'erro' e 'texto_bruto'.

    Raises:
        ErroAnaliseCaso: se `modelo` não for um dos IDs válidos.
        Exceções típicas do SDK `anthropic` (anthropic.AuthenticationError,
        anthropic.RateLimitError, anthropic.APIStatusError,
        anthropic.APIConnectionError, etc.) propagam para o chamador, que
        deve tratá-las com as classes tipadas do SDK.
    """
    if modelo not in MODELOS_VALIDOS:
        raise ErroAnaliseCaso(
            f"Modelo inválido: {modelo!r}. Use um destes: "
            f"{sorted(MODELOS_VALIDOS)}."
        )

    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    system_prompt = _montar_system_prompt()
    user_prompt = _montar_user_prompt(
        nome_cliente, sexo, data_nascimento, beneficio, documentos
    )

    with client.messages.stream(
        model=modelo,
        max_tokens=MAX_TOKENS,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    ) as stream:
        resposta = stream.get_final_message()

    texto_completo = "".join(
        bloco.text
        for bloco in resposta.content
        if getattr(bloco, "type", None) == "text"
    )

    resultado = _extrair_json(texto_completo)

    # Garante que as 4 chaves esperadas sempre existam (quando o parse deu
    # certo, mas o modelo omitiu alguma) para a interface não quebrar.
    if "erro" not in resultado:
        for chave in CHAVES_ESPERADAS:
            resultado.setdefault(
                chave, f"[chave '{chave}' ausente na resposta do modelo]"
            )

    return resultado
