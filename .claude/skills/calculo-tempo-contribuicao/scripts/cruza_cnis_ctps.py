#!/usr/bin/env python3
"""
Cruza CNIS e CTPS, identificando:
- Periodos que estao so na CTPS (a averbar)
- Periodos que estao so no CNIS
- Divergencias de datas entre os dois documentos

Uso:
    python cruza_cnis_ctps.py --cnis cnis.txt --ctps ctps.txt --output divergencias.json
"""
import argparse
import json
import re


def normalizar_mes_ano(texto):
    """Converte 'MM/AAAA' ou 'MM-AAAA' em tupla (ano, mes)."""
    if not texto:
        return None
    match = re.search(r'(\d{2})[/-](\d{4})', str(texto))
    if match:
        return (int(match.group(2)), int(match.group(1)))
    return None


def calcular_duracao_meses(inicio, fim):
    """Retorna diferenca em meses entre duas tuplas (ano, mes)."""
    if not inicio or not fim:
        return 0
    return (fim[0] - inicio[0]) * 12 + (fim[1] - inicio[1])


def parse_vinculos(texto, origem):
    """Extrai vinculos de um texto (CNIS ou CTPS) usando datas MM/AAAA."""
    vinculos = []
    padrao_data = re.compile(r'(\d{2}/\d{4})')
    padrao_cnpj = re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}')

    for linha in texto.split('\n'):
        datas = padrao_data.findall(linha)
        if len(datas) >= 2:
            cnpj_match = padrao_cnpj.search(linha)
            vinculos.append({
                "empregador": linha.strip()[:120],
                "cnpj": cnpj_match.group() if cnpj_match else None,
                "admissao": datas[0],
                "demissao": datas[1],
                "origem": origem
            })
    return vinculos


def mesmo_periodo(v1, v2, tolerancia_meses=1):
    """Considera dois vinculos iguais se datas estiverem dentro da tolerancia."""
    a1 = normalizar_mes_ano(v1.get("admissao"))
    a2 = normalizar_mes_ano(v2.get("admissao"))
    d1 = normalizar_mes_ano(v1.get("demissao"))
    d2 = normalizar_mes_ano(v2.get("demissao"))

    if not (a1 and a2):
        return False

    if abs(calcular_duracao_meses(a1, a2)) > tolerancia_meses:
        return False

    if d1 and d2:
        if abs(calcular_duracao_meses(d1, d2)) > tolerancia_meses:
            return False

    return True


def cruzar(vinculos_cnis, vinculos_ctps):
    apenas_ctps = []
    apenas_cnis = []
    divergencias_datas = []

    for v_ctps in vinculos_ctps:
        encontrado = False
        for v_cnis in vinculos_cnis:
            if mesmo_periodo(v_ctps, v_cnis):
                encontrado = True
                if v_ctps["admissao"] != v_cnis["admissao"] or v_ctps["demissao"] != v_cnis["demissao"]:
                    divergencias_datas.append({
                        "ctps": v_ctps,
                        "cnis": v_cnis,
                        "tipo": "data_divergente"
                    })
                break
        if not encontrado:
            apenas_ctps.append(v_ctps)

    for v_cnis in vinculos_cnis:
        encontrado = any(mesmo_periodo(v_cnis, v_ctps) for v_ctps in vinculos_ctps)
        if not encontrado:
            apenas_cnis.append(v_cnis)

    return {
        "apenas_ctps": apenas_ctps,
        "apenas_cnis": apenas_cnis,
        "divergencias_datas": divergencias_datas
    }


def main():
    parser = argparse.ArgumentParser(description="Cruza CNIS e CTPS")
    parser.add_argument("--cnis", required=True, help="Arquivo texto do CNIS")
    parser.add_argument("--ctps", required=True, help="Arquivo texto da CTPS")
    parser.add_argument("--output", required=True, help="Arquivo JSON de saida")
    args = parser.parse_args()

    with open(args.cnis, 'r', encoding='utf-8', errors='ignore') as f:
        cnis_text = f.read()
    with open(args.ctps, 'r', encoding='utf-8', errors='ignore') as f:
        ctps_text = f.read()

    vinculos_cnis = parse_vinculos(cnis_text, "CNIS")
    vinculos_ctps = parse_vinculos(ctps_text, "CTPS")

    resultado = cruzar(vinculos_cnis, vinculos_ctps)

    total_meses_a_averbar = sum(
        calcular_duracao_meses(
            normalizar_mes_ano(v["admissao"]),
            normalizar_mes_ano(v["demissao"])
        )
        for v in resultado["apenas_ctps"]
    )

    saida = {
        "resumo": {
            "total_vinculos_cnis": len(vinculos_cnis),
            "total_vinculos_ctps": len(vinculos_ctps),
            "total_apenas_ctps": len(resultado["apenas_ctps"]),
            "total_apenas_cnis": len(resultado["apenas_cnis"]),
            "total_divergencias_datas": len(resultado["divergencias_datas"]),
            "meses_a_averbar": total_meses_a_averbar
        },
        "apenas_ctps": resultado["apenas_ctps"],
        "apenas_cnis": resultado["apenas_cnis"],
        "divergencias_datas": resultado["divergencias_datas"]
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(saida, f, indent=2, ensure_ascii=False)

    print(f"OK: {args.output}")
    print(f"Vinculos CNIS: {len(vinculos_cnis)}")
    print(f"Vinculos CTPS: {len(vinculos_ctps)}")
    print(f"Apenas CTPS (a averbar): {len(resultado['apenas_ctps'])}")
    print(f"Meses a averbar: {total_meses_a_averbar}")


if __name__ == "__main__":
    main()
