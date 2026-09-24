"""Interface Streamlit do Escritório Previdenciário.

Versão simplificada do sistema multiagente: chama a API Anthropic
diretamente (SDK `anthropic`, sem Claude Agent SDK) para que o escritório
possa analisar casos sem precisar do Claude Code. O Claude Code Web
continua sendo a versão completa do sistema.

⚠️ Todo resultado gerado aqui é RASCUNHO para revisão do advogado
responsável (regra inviolável 1 do projeto — ver CLAUDE.md).
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

import anthropic
import streamlit as st

import anthropic_client
from pdf_utils import extrair_texto_pdf
from prompts import REPO_ROOT

CASOS_DIR = REPO_ROOT / "casos"

AVISO_RASCUNHO = "⚠️ RASCUNHO — PARA REVISÃO DO ADVOGADO"

# As 9 opções de benefício foram tomadas dos "Benefícios Mais Trabalhados"
# listados em practice-profile.md (os 9 primeiros da lista do escritório) —
# a enumeração original de 9 itens citada na tarefa não estava disponível
# neste contexto; ajuste esta lista se divergir do que foi pedido.
BENEFICIOS_OPCOES = [
    "Aposentadoria por idade",
    "Aposentadoria por tempo de contribuição",
    "Aposentadoria rural",
    "Aposentadoria especial",
    "Auxílio-doença (incapacidade temporária)",
    "Aposentadoria por invalidez (incapacidade permanente)",
    "Pensão por morte",
    "BPC-LOAS (idoso ou pessoa com deficiência)",
    "Auxílio-reclusão",
]

MODELOS_OPCOES = {
    "Sonnet 5 (rápido)": "claude-sonnet-5",
    "Opus 5 (preciso)": "claude-opus-5",
}

# Placeholder genérico — ajuste para a URL real do README no GitHub caso
# o branch padrão do repositório seja diferente de "main".
URL_DOCUMENTACAO = (
    "https://github.com/marinalaura16-web/escritorio-previdenciario"
    "/blob/main/app/README.md"
)

CHAVES_SECOES = ("triagem", "calculo", "arquivo_medico", "peticao")
LABELS_SECOES = {
    "triagem": "Triagem",
    "calculo": "Cálculo",
    "arquivo_medico": "Arquivo Médico",
    "peticao": "Petição",
}


# --------------------------------------------------------------------------
# Config visual
# --------------------------------------------------------------------------

def configurar_pagina() -> None:
    st.set_page_config(
        page_title="Escritório Previdenciário",
        layout="wide",
        page_icon="⚖️",
    )
    # Cores primárias/secundárias vêm de .streamlit/config.toml. O CSS abaixo
    # cobre apenas o que o Streamlit não expõe via config (esconder o menu
    # hambúrguer e o rodapé "Made with Streamlit").
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header [data-testid="stToolbar"] {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------

def resolver_api_key(api_key_input: str) -> str:
    """Resolve a API Key: prioridade para o campo da sidebar; se vazio,
    tenta `st.secrets["ANTHROPIC_API_KEY"]`. Nunca lança exceção — em
    qualquer falha de acesso a `st.secrets` (ex.: arquivo secrets.toml
    inexistente), devolve string vazia."""
    if api_key_input:
        return api_key_input
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        return ""


def montar_sidebar() -> tuple[str, str]:
    st.sidebar.title("Escritório Previdenciário")
    st.sidebar.caption("Sistema de Análise de Casos")
    st.sidebar.divider()

    api_key_input = st.sidebar.text_input(
        "API Key da Anthropic",
        type="password",
        help=(
            "Opcional: se deixado em branco, a interface tenta usar "
            "st.secrets['ANTHROPIC_API_KEY'] (arquivo "
            ".streamlit/secrets.toml)."
        ),
    )
    api_key = resolver_api_key(api_key_input)
    if not api_key:
        st.sidebar.warning(
            "⚠️ Nenhuma API Key configurada. Informe uma acima ou "
            "configure `ANTHROPIC_API_KEY` em "
            "`app/.streamlit/secrets.toml` (veja "
            "`secrets.toml.example`)."
        )

    label_modelo = st.sidebar.selectbox(
        "Modelo",
        options=list(MODELOS_OPCOES.keys()),
        index=0,
    )
    modelo = MODELOS_OPCOES[label_modelo]

    st.sidebar.divider()
    st.sidebar.markdown(f"[📖 Documentação]({URL_DOCUMENTACAO})")
    st.sidebar.caption(
        "Versão simplificada. O Claude Code Web continua sendo a versão "
        "completa do sistema multiagente."
    )

    return api_key, modelo


# --------------------------------------------------------------------------
# Utilitários de caso
# --------------------------------------------------------------------------

def gerar_numero_caso() -> str:
    """Gera um número de caso no formato AAAA-NNN, verificando os casos já
    existentes em casos/ para não colidir."""
    ano = datetime.now().year
    maior_seq = 0
    if CASOS_DIR.exists():
        padrao = re.compile(rf"^{ano}-(\d{{3,}})$")
        for item in CASOS_DIR.iterdir():
            if item.is_dir():
                m = padrao.match(item.name)
                if m:
                    maior_seq = max(maior_seq, int(m.group(1)))
    return f"{ano}-{maior_seq + 1:03d}"


def validar_data_nascimento(data_texto: str) -> bool:
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", data_texto or ""):
        return False
    try:
        datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def salvar_documentos(numero_caso: str, arquivos) -> dict[str, str]:
    """Salva os PDFs enviados em casos/{numero}/documentos/ e extrai o
    texto de cada um. Devolve {nome_arquivo: texto_extraido} e mostra um
    aviso na interface para cada arquivo cujo texto não pôde ser extraído."""
    pasta_documentos = CASOS_DIR / numero_caso / "documentos"
    pasta_documentos.mkdir(parents=True, exist_ok=True)

    documentos: dict[str, str] = {}
    for arquivo in arquivos:
        destino = pasta_documentos / arquivo.name
        destino.write_bytes(arquivo.getvalue())

        texto, erro = extrair_texto_pdf(destino)
        if erro:
            st.warning(f"**{arquivo.name}**: {erro}")
        documentos[arquivo.name] = texto

    return documentos


def salvar_analises(numero_caso: str, resultado: dict[str, str]) -> None:
    pasta_analises = CASOS_DIR / numero_caso / "analises"
    pasta_analises.mkdir(parents=True, exist_ok=True)

    if "erro" in resultado:
        (pasta_analises / "erro-resposta-bruta.md").write_text(
            resultado.get("texto_bruto", ""), encoding="utf-8"
        )
        return

    for chave in CHAVES_SECOES:
        conteudo = resultado.get(chave, "")
        (pasta_analises / f"{chave}.md").write_text(conteudo, encoding="utf-8")


def montar_markdown_combinado(numero_caso: str, resultado: dict[str, str]) -> str:
    partes = [f"# Caso {numero_caso}\n\n{AVISO_RASCUNHO}\n"]
    for chave in CHAVES_SECOES:
        partes.append(f"\n---\n\n## {LABELS_SECOES[chave]}\n\n{resultado.get(chave, '')}")
    return "\n".join(partes)


# --------------------------------------------------------------------------
# Tab 1 — Novo Caso
# --------------------------------------------------------------------------

def exibir_resultado(numero_caso: str, resultado: dict[str, str]) -> None:
    st.warning(AVISO_RASCUNHO)

    if "erro" in resultado:
        st.error(resultado["erro"])
        with st.expander("Ver texto bruto retornado pelo modelo"):
            st.code(resultado.get("texto_bruto", ""), language="markdown")
        return

    tabs = st.tabs([LABELS_SECOES[c] for c in CHAVES_SECOES])
    for tab, chave in zip(tabs, CHAVES_SECOES):
        with tab:
            st.markdown(resultado.get(chave, "_(vazio)_"))

    st.divider()
    col1, col2 = st.columns(2)

    markdown_combinado = montar_markdown_combinado(numero_caso, resultado)
    with col1:
        st.download_button(
            "📥 Baixar tudo em .md",
            data=markdown_combinado,
            file_name=f"caso-{numero_caso}-analise.md",
            mime="text/markdown",
        )
    with col2:
        with st.expander("📋 Copiar para área de transferência"):
            # Streamlit não tem um componente nativo robusto de clipboard;
            # st.code() já exibe um ícone de cópia embutido no canto
            # superior direito do bloco, que cobre o caso de uso de forma
            # simples (limitação documentada no README).
            st.code(markdown_combinado, language="markdown")


def tab_novo_caso(api_key: str, modelo: str) -> None:
    st.subheader("Novo Caso")

    with st.form("form_novo_caso"):
        nome_cliente = st.text_input("Nome do cliente")
        sexo = st.radio("Sexo", options=["Masculino", "Feminino"], horizontal=True)
        data_nascimento = st.text_input("Data de nascimento (DD/MM/AAAA)")
        beneficio = st.selectbox("Benefício pretendido", options=BENEFICIOS_OPCOES)
        arquivos = st.file_uploader(
            "Documentos (CNIS, CTPS, PPPs, laudos médicos, carta de "
            "indeferimento — envie todos juntos)",
            type="pdf",
            accept_multiple_files=True,
            help=(
                "O Streamlit não segmenta o upload por categoria "
                "facilmente; um único uploader com múltiplos arquivos é "
                "usado aqui como simplificação — o tipo de cada documento "
                "é inferido pelo modelo a partir do próprio conteúdo."
            ),
        )
        enviado = st.form_submit_button("🔍 ANALISAR CASO")

    if not enviado:
        return

    if not nome_cliente:
        st.error("Informe o nome do cliente.")
        return
    if not validar_data_nascimento(data_nascimento):
        st.error("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
        return
    if not api_key:
        st.error(
            "Nenhuma API Key configurada. Configure na barra lateral antes "
            "de analisar o caso."
        )
        return

    numero_caso = gerar_numero_caso()
    st.info(f"Caso criado: **{numero_caso}**")

    documentos = salvar_documentos(numero_caso, arquivos or [])

    resultado = None
    with st.spinner("Analisando... (pode levar 3-5 minutos)"):
        try:
            resultado = anthropic_client.analisar_caso(
                nome_cliente=nome_cliente,
                sexo=sexo,
                data_nascimento=data_nascimento,
                beneficio=beneficio,
                documentos=documentos,
                api_key=api_key,
                modelo=modelo,
            )
        except anthropic_client.ErroAnaliseCaso as e:
            st.error(str(e))
        except anthropic.AuthenticationError:
            st.error(
                "Chave de API inválida ou não autorizada. Verifique a API "
                "Key na barra lateral."
            )
        except anthropic.RateLimitError:
            st.error(
                "Limite de requisições da API da Anthropic atingido. "
                "Aguarde um pouco e tente novamente."
            )
        except anthropic.APIConnectionError:
            st.error(
                "Falha de conexão com a API da Anthropic. Verifique sua "
                "internet e tente novamente."
            )
        except anthropic.APIStatusError as e:
            st.error(f"Erro da API Anthropic (status {e.status_code}): {e.message}")

    if resultado is None:
        return

    salvar_analises(numero_caso, resultado)
    st.session_state["ultimo_caso_numero"] = numero_caso
    st.session_state["ultimo_caso_resultado"] = resultado

    exibir_resultado(numero_caso, resultado)


# --------------------------------------------------------------------------
# Tab 2 — Casos Anteriores
# --------------------------------------------------------------------------

def listar_casos() -> list[Path]:
    if not CASOS_DIR.exists():
        return []
    pastas = [p for p in CASOS_DIR.iterdir() if p.is_dir()]
    pastas.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return pastas


def carregar_analises_salvas(pasta_caso: Path) -> dict[str, str]:
    pasta_analises = pasta_caso / "analises"
    resultado: dict[str, str] = {}
    if not pasta_analises.exists():
        return resultado
    for chave in CHAVES_SECOES:
        arquivo = pasta_analises / f"{chave}.md"
        if arquivo.exists():
            resultado[chave] = arquivo.read_text(encoding="utf-8")
    return resultado


def tab_casos_anteriores() -> None:
    st.subheader("Casos Anteriores")

    pastas = listar_casos()
    if not pastas:
        st.info("Nenhum caso encontrado em `casos/`.")
        return

    opcoes = [p.name for p in pastas]
    numero_selecionado = st.selectbox("Selecione um caso", options=opcoes)
    pasta_caso = CASOS_DIR / numero_selecionado

    analises = carregar_analises_salvas(pasta_caso)
    if not analises:
        st.info(
            f"O caso **{numero_selecionado}** não tem análises geradas por "
            "esta interface ainda (pasta `analises/` vazia ou ausente)."
        )
        return

    st.warning(AVISO_RASCUNHO)
    tabs = st.tabs([LABELS_SECOES[c] for c in analises.keys()])
    for tab, chave in zip(tabs, analises.keys()):
        with tab:
            st.markdown(analises[chave])


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> None:
    configurar_pagina()
    api_key, modelo = montar_sidebar()

    tab1, tab2 = st.tabs(["Novo Caso", "Casos Anteriores"])
    with tab1:
        tab_novo_caso(api_key, modelo)
    with tab2:
        tab_casos_anteriores()


if __name__ == "__main__":
    main()
