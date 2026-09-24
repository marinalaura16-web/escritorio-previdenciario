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

MAPA_NORMAS = {
    "CF": "constituicao/cf-1988-seguridade-social.md",
    "LEI 8.213": "leis-ordinarias/lei-8.213-1991.md",
    "LEI 8.212": "leis-ordinarias/lei-8.212-1991.md",
    "DECRETO 3.048": "decretos/decreto-3.048-1999.md",
    "EC 103": "emendas-constitucionais/ec-103-2019.md",
    "IN 128": "instrucoes-normativas/in-128-2022.md",
    "LEI 15.327": "leis-ordinarias/lei-15.327-2026.md",
    "LEI 15.371": "leis-ordinarias/lei-15.371-2026.md",
    "LEI 8.742": "leis-ordinarias/lei-8.742-1993.md",
    "LEI 13.846": "leis-ordinarias/lei-13.846-2019.md",
    "DECRETO 6.214": "decretos/decreto-6.214-2007.md",
}


def dispositivo_existe(norma, artigo):
    """Retorna True se o dispositivo for encontrado na base."""
    for chave, arquivo in MAPA_NORMAS.items():
        if chave in norma.upper():
            caminho = os.path.join(BASE_PATH, arquivo)
            if os.path.exists(caminho):
                try:
                    with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
                        if artigo in f.read():
                            return True
                except Exception:
                    pass
    return False


def tem_marcacao_confirmar(texto):
    """Verifica se o texto contem a marcacao de confirmacao."""
    marcadores = [
        "[DISPOSITIVO A CONFIRMAR]",
        "[JURISPRUDÊNCIA A CONFIRMAR]",
        "[JURISPRUDENCIA A CONFIRMAR]",
        "[A CONFIRMAR]",
    ]
    return any(m in texto for m in marcadores)


# Reconhece dois formatos de citacao legislativa:
#   1) "NORMA, art. N"      (ex.: "Lei 8.213, art. 48")   -> grupos 1,2
#   2) "art. N da/do NORMA" (ex.: "art. 48 da Lei 8.213")  -> grupos 3,4 (invertidos)
PADRAO_CITACAO = re.compile(
    r'(?:'
    r'(CF|LEI\s+[\d.]+|DECRETO\s+[\d.]+|EC\s+\d+|IN\s+\d+)[,\s]+art\.?\s*(\d+)'
    r'|'
    r'art\.?\s*(\d+)[,\s]+d[ao]\s+(CF|LEI\s+[\d.]+|DECRETO\s+[\d.]+|EC\s+\d+|IN\s+\d+)'
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
