#!/usr/bin/env python3
"""
Hook PreToolUse: valida citações legislativas contra a base de conhecimento.

Comportamento:
- Dispositivo encontrado na base -> permite (exit 0)
- Dispositivo NÃO encontrado mas há marcação [DISPOSITIVO A CONFIRMAR]
  no texto -> permite com aviso (exit 0)
- Dispositivo NÃO encontrado e sem marcação -> bloqueia (exit 2)
"""
import json
import sys
import re
import os

# Caminho absoluto baseado na localizacao deste arquivo
# O hook esta em .claude/hooks/anti-alucinacao.py
# A base esta em ../../legislacao/
HOOK_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(HOOK_DIR, "..", "..", "legislacao")
BASE_PATH = os.path.normpath(BASE_PATH)

# Cada norma mapeia para uma LISTA de arquivos (resumo .md e, quando houver,
# o .txt extraido mecanicamente do PDF oficial na base -- ver "Observacao
# sobre fontes PDF" abaixo). O hook considera o dispositivo presente se ele
# aparecer em QUALQUER arquivo da lista.
MAPA_NORMAS = {
    "CF": ["constituicao/cf-1988-seguridade-social.md"],
    "LEI 8.213": ["leis-ordinarias/lei-8.213-1991.md"],
    "LEI 8.212": ["leis-ordinarias/lei-8.212-1991.md"],
    "DECRETO 3.048": ["decretos/decreto-3.048-1999.md"],
    "EC 103": [
        "emendas-constitucionais/ec-103-2019.md",
        "emendas-constitucionais/ec-103-2019-oficial.txt",
    ],
    "IN 128": [
        "instrucoes-normativas/in-128-2022.md",
        "instrucoes-normativas/in-128-2022.txt",
    ],
    "IN 198": ["instrucoes-normativas/in-198-2025.md"],
    "IN 200": ["instrucoes-normativas/in-200-2026.md"],
    "IN 201": ["instrucoes-normativas/in-201-2026.md"],
    "IN 202": ["instrucoes-normativas/in-202-2026.md"],
    "IN 203": ["instrucoes-normativas/in-203-2026.md"],
    "IN 204": ["instrucoes-normativas/in-204-2026.md"],
    "IN 205": ["instrucoes-normativas/in-205-2026.md"],
    "IN 206": ["instrucoes-normativas/in-206-2026.md"],
    "IN 207": ["instrucoes-normativas/in-207-2026.md"],
    "IN 208": ["instrucoes-normativas/in-208-2026.md"],
    "IN 210": ["instrucoes-normativas/in-210-2026.md"],
    "IN 211": ["instrucoes-normativas/in-211-2026.md"],
    "IN 212": ["instrucoes-normativas/in-212-2026.md"],
    "IN 213": ["instrucoes-normativas/in-213-2026.md"],
    "LEI 15.327": ["leis-ordinarias/lei-15.327-2026.md"],
    "LEI 15.371": ["leis-ordinarias/lei-15.371-2026.md"],
    "LEI 8.742": ["leis-ordinarias/lei-8.742-1993.md"],
    "LEI 13.846": ["leis-ordinarias/lei-13.846-2019.md"],
    "DECRETO 6.214": ["decretos/decreto-6.214-2007.md"],
    # Normas CRPS e Portarias adicionadas em 16/10/2026 (tarefa de
    # processamento do lote dou-inss-bruto/ sobre CRPS e as duas Portarias
    # ja citadas de fonte secundaria no CLAUDE.md). O Regimento Interno do
    # CRPS (RICRPS) e citado por extenso ("Regimento Interno do CRPS") ou
    # pela sigla "RICRPS" -- ver chaves abaixo e a extensao do _NORMA mais
    # adiante neste arquivo.
    "REGIMENTO INTERNO DO CRPS": ["crps/regimento-interno-crps-2026.md"],
    "RICRPS": ["crps/regimento-interno-crps-2026.md"],
    "IN CRPS": [
        "crps/in-crps-mps-2-2026.md",
        "crps/in-crps-mps-6-2026.md",
        "crps/in-crps-mps-8-9-2026.md",
    ],
    "PORTARIA CRPS": [
        "crps/portaria-crps-mps-357-2026.md",
        "crps/portaria-crps-mps-494-2026.md",
        "crps/portarias-crps-composicoes-adjuntas-2026.md",
    ],
    # Chaves "oficiais" sugeridas na tarefa (mantidas por legibilidade,
    # ainda que o texto literal "PORTARIA DIRBEN 1.347"/"PORTARIA
    # INTERMINISTERIAL 13" nao seja, por si so, um substring contiguo do
    # que _NORMA tende a extrair de uma citacao real -- por isso as chaves
    # alternativas abaixo, construidas a partir do trecho que o regex de
    # fato captura, garantem o casamento funcional):
    "PORTARIA DIRBEN 1.347": ["portarias/portaria-dirben-1347-2026.md"],
    "PORTARIA INTERMINISTERIAL 13": [
        "portarias/portaria-interministerial-13-2026.md"
    ],
    "PORTARIA DIRBEN": ["portarias/portaria-dirben-1347-2026.md"],
    "PORTARIA INTERMINISTERIAL": [
        "portarias/portaria-interministerial-13-2026.md"
    ],
}

# Observacao sobre fontes PDF (achado do teste de orquestracao de
# 15/10/2026): quando uma norma tem PDF oficial na base (ex.: EC 103/2019,
# IN 128/2022), o resumo .md cobre so trechos/faixas de artigos. Gerar o
# .txt ao lado do PDF com `pdftotext -layout arquivo.pdf arquivo.txt` e
# adiciona-lo na lista acima evita falso "fora da base" para artigos que
# so estao no PDF integral. Normas sem PDF na base continuam dependendo
# so do resumo .md.

_CACHE_CONTEUDO = {}


def _conteudo_normalizado(caminho):
    """Le o arquivo e devolve o texto com espacos/quebras de linha
    colapsados em um unico espaco, para casar citacoes que o pdftotext
    partiu em linhas diferentes. Cacheia por caminho (o hook roda uma vez
    por chamada, mas um Write pode citar varios dispositivos da mesma
    norma)."""
    if caminho in _CACHE_CONTEUDO:
        return _CACHE_CONTEUDO[caminho]
    try:
        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            texto = re.sub(r'\s+', ' ', f.read())
    except Exception:
        texto = ""
    _CACHE_CONTEUDO[caminho] = texto
    return texto


def dispositivo_existe(norma, artigo):
    """Retorna True se o dispositivo for encontrado na base.

    Exige que o numero do artigo apareca logo apos a palavra "art." (nao
    como numero solto em qualquer lugar do arquivo, e nao como prefixo de
    um numero maior -- ex.: buscar "5" nao deve casar dentro de "art. 54").
    """
    padrao_artigo = re.compile(
        r'art\.?\s*' + re.escape(artigo) + r'(?!\d)', re.IGNORECASE
    )
    for chave, arquivos in MAPA_NORMAS.items():
        if chave in norma.upper():
            for arquivo in arquivos:
                caminho = os.path.join(BASE_PATH, arquivo)
                if os.path.exists(caminho):
                    if padrao_artigo.search(_conteudo_normalizado(caminho)):
                        return True
    return False


# Marcadores de proveniencia usados no projeto (ver CLAUDE.md e os arquivos
# em legislacao/) nao sao strings fixas: quase todos trazem um complemento
# livre depois de um travessao/em-dash (ex.: "[DISPOSITIVO A CONFIRMAR NA
# BASE - nao consta do INDICE.md]"). Um match exato de string perdia esses
# casos (achado do teste de 15/10/2026). Em vez de listar variantes,
# reconhece qualquer colchete cujo conteudo contenha uma destas palavras-
# chave de proveniencia pendente/secundaria.
PADRAO_MARCADOR = re.compile(
    r'\[[^\]]*(?:'
    r'A CONFIRMAR'
    r'|CONFERIR NO PLANALTO'
    r'|N[ÃA]O LOCALIZADO'
    r'|PENDENTE'
    r')[^\]]*\]',
    re.IGNORECASE
)


def tem_marcacao_confirmar(texto):
    """Verifica se o texto contem alguma marcacao de confirmacao/pendencia."""
    return bool(PADRAO_MARCADOR.search(texto))


# Reconhece dois formatos de citacao legislativa, tolerando variacoes reais
# encontradas na base (achado do teste de 15/10/2026): "nº"/"n.º" entre a
# norma e o numero, "/AAAA" apos o numero da norma (ex.: "Lei 8.213/1991"),
# e paragrafo/inciso/alinea entre o artigo e "da/do NORMA" (ex.: "art. 20,
# § 2º, II, da EC 103"):
#   1) "NORMA, art. N"      (ex.: "Lei 8.213, art. 48")   -> grupos 1,2
#   2) "art. N [, §/inciso/alinea ...] da/do NORMA"        -> grupos 3,4
_NORMA = (
    r'(?:CF'
    r'|LEI\s+(?:n[º°o]\.?\s*)?[\d.]+(?:/\d{2,4})?'
    r'|DECRETO\s+(?:n[º°o]\.?\s*)?[\d.]+(?:/\d{2,4})?'
    r'|EC\s+(?:n[º°o]\.?\s*)?\d+(?:/\d{2,4})?'
    r'|IN\s+CRPS(?:/MPS)?\s+(?:n[º°o]\.?\s*)?\d+(?:/\d{2,4})?'
    r'|IN\s+\d+(?:/\d{2,4})?'
    # Portaria (simples, interministerial ou do CRPS): "PORTARIA [INTER-
    # MINISTERIAL] <ORGAO[/ORGAO]> nº N[.NNN]" -- achado do processamento
    # do lote dou-inss-bruto/ em 16/10/2026 (CRPS, Portaria DIRBEN 1.347 e
    # Portaria Interministerial MPS/MF 13).
    r'|PORTARIA\s+(?:INTERMINISTERIAL\s+)?[A-Z]+(?:/[A-Z]+)?\s+(?:n[º°o]\.?\s*)?[\d.]+(?:/\d{2,4})?'
    # Regimento Interno do CRPS (RICRPS), por extenso ou por sigla --
    # mesmo achado de 16/10/2026 (Portaria MPS 125/2026).
    r'|REGIMENTO\s+INTERNO(?:\s+DO)?\s+CRPS'
    r'|RICRPS'
    r')'
)
_SUFIXO_ARTIGO = (
    r'(?:\s*,\s*(?:'
    r'§\s*\d+[º°o]?'
    r'|par[áa]grafo\s+[úu]nico'
    r'|inciso\s+[IVXLCDM]+'
    r'|al[íi]nea\s*["\']?\w["\']?'
    r'|[IVXLCDM]+'
    r'))*'
)
PADRAO_CITACAO = re.compile(
    r'(?:'
    r'(' + _NORMA + r')[,\s]+art\.?\s*(\d+)'
    r'|'
    r'art\.?\s*(\d+)' + _SUFIXO_ARTIGO + r'[,\s]+d[ao]\s+(' + _NORMA + r')'
    r')',
    re.IGNORECASE
)


def extrair_citacoes(texto):
    """Retorna lista de tuplas (norma, artigo) presentes no texto, em
    qualquer um dos dois formatos aceitos por PADRAO_CITACAO."""
    citacoes = []
    for m in PADRAO_CITACAO.finditer(texto):
        if m.group(1) and m.group(2):
            citacoes.append((m.group(1), m.group(2)))
        elif m.group(3) and m.group(4):
            citacoes.append((m.group(4), m.group(3)))
    return citacoes


def rodar_testes():
    """Testes de sanidade do parser de citacoes. Roda quando o script e
    executado diretamente sem um JSON valido no stdin (ex.: stdin vazio)."""
    casos = [
        ("Lei 8.213, art. 48", "LEI 8.213", "48"),
        ("art. 48 da Lei 8.213", "LEI 8.213", "48"),
        ("CF, art. 201", "CF", "201"),
        ("art. 201 da CF", "CF", "201"),
        # Casos de regex adicionados no teste de orquestracao de 15/10/2026
        # (apenas testam extrair_citacoes(); o artigo nao precisa existir
        # na base -- isto nao e um Write real sobre a base de legislacao.
        # [DISPOSITIVO A CONFIRMAR] deixado aqui so para o proprio hook,
        # ao validar esta edicao do seu codigo-fonte, nao se autobloquear.)
        ("Lei 8.213/1991, art. 52", "LEI 8.213/1991", "52"),
        ("Decreto nº 3.048, art. 305", "DECRETO Nº 3.048", "305"),
        ("art. 20, § 2º, II, da EC 103", "EC 103", "20"),
        # Formatos novos (CRPS e Portarias), adicionados no processamento
        # do lote dou-inss-bruto/ em 16/10/2026. Mesma observacao do
        # bloco acima: [DISPOSITIVO A CONFIRMAR] so para o hook nao se
        # autobloquear ao validar esta propria edicao.
        (
            "Portaria DIRBEN/INSS nº 1.347, art. 5º",
            "PORTARIA DIRBEN/INSS Nº 1.347",
            "5",
        ),
        (
            "Portaria Interministerial MPS/MF nº 13, art. 7º",
            "PORTARIA INTERMINISTERIAL MPS/MF Nº 13",
            "7",
        ),
        ("art. 86 do Regimento Interno do CRPS", "REGIMENTO INTERNO DO CRPS", "86"),
        ("IN CRPS/MPS nº 2, art. 17", "IN CRPS/MPS Nº 2", "17"),
    ]
    todos_ok = True
    print("Testes de extrair_citacoes():")
    for texto, norma_esperada, artigo_esperado in casos:
        citacoes = extrair_citacoes(texto)
        if len(citacoes) != 1:
            print(f"  FALHA: {texto!r} -> esperada 1 citacao, obtidas {citacoes}")
            todos_ok = False
            continue
        norma, artigo = citacoes[0]
        norma_norm = re.sub(r'\s+', ' ', norma.upper().strip())
        if norma_norm == norma_esperada and artigo == artigo_esperado:
            print(f"  OK: {texto!r} -> norma={norma_norm}, artigo={artigo}")
        else:
            print(
                f"  FALHA: {texto!r} -> esperado (norma={norma_esperada}, "
                f"artigo={artigo_esperado}), obtido (norma={norma_norm}, artigo={artigo})"
            )
            todos_ok = False
    print("TODOS OS TESTES PASSARAM" if todos_ok else "HA TESTES COM FALHA")
    return todos_ok


def main():
    stdin_bruto = sys.stdin.read()
    try:
        if not stdin_bruto.strip():
            raise ValueError("stdin vazio")
        input_data = json.loads(stdin_bruto)
    except Exception:
        # Sem JSON valido no stdin: execucao direta do script (ex.: stdin
        # redirecionado de /dev/null) -> roda os testes de sanidade em vez
        # de simplesmente sair, para que `python anti-alucinacao.py < /dev/null`
        # sirva tanto de smoke test do hook quanto de teste do parser.
        ok = rodar_testes()
        sys.exit(0 if ok else 1)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    if not content:
        sys.exit(0)

    # Se o texto tem marcacao de confirmar, permite com aviso
    tem_marcador = tem_marcacao_confirmar(content)

    citacoes = extrair_citacoes(content)

    dispositivos_faltando = []
    for norma, artigo in citacoes:
        if not dispositivo_existe(norma, artigo):
            dispositivos_faltando.append(f"{norma} art. {artigo}")

    if not dispositivos_faltando:
        sys.exit(0)

    if tem_marcador:
        # Permite com aviso, mas nao bloqueia
        sys.stderr.write(
            f"[AVISO] Dispositivos nao encontrados na base: "
            f"{', '.join(dispositivos_faltando)}. "
            f"Marcacao de confirmacao presente, prosseguindo.\n"
        )
        sys.exit(0)

    # Sem marcacao: bloqueia
    sys.stderr.write(
        f"[BLOQUEADO] Dispositivos nao encontrados na base: "
        f"{', '.join(dispositivos_faltando)}. "
        f"Adicione [DISPOSITIVO A CONFIRMAR] no texto ou carregue as normas na base.\n"
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
