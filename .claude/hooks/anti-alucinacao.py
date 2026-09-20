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


def main():
    try:
        input_data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    if not content:
        sys.exit(0)

    # Se o texto tem marcacao de confirmar, permite com aviso
    tem_marcador = tem_marcacao_confirmar(content)

    padrao = r'(CF|LEI\s+[\d.]+|DECRETO\s+[\d.]+|EC\s+\d+|IN\s+\d+)[,\s]+art\.?\s*(\d+)'
    citacoes = re.findall(padrao, content, re.IGNORECASE)

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
