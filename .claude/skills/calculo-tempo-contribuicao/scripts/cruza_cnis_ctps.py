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


PADRAO_DATA_COMPLETA = re.compile(r'\d{2}/\d{2}/\d{4}')
PADRAO_MES_ANO = re.compile(r'\d{2}/\d{4}')
PADRAO_CNPJ = re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}')
# Linha de vinculo do CNIS comeca com "Seq." + NIT no formato PIS/PASEP
# (DDD.DDDDD.DD-D). Essa ancora evita capturar linhas da tabela de
# remuneracoes (competencia MM/AAAA, sem NIT) ou do cabecalho de pagina
# (que tambem tem datas DD/MM/AAAA, como "Data de nascimento" e a data de
# emissao do extrato) como se fossem vinculos.
PADRAO_LINHA_VINCULO_CNIS = re.compile(r'^\s*\d{1,2}\s+\d{3}\.\d{5}\.\d{2}-\d')
# Linha de contrato da CTPS Digital: soh a data (ou intervalo de datas),
# sem texto de evento anexado. Ex.: "01/02/2020 - 15/12/2020" ou
# "20/09/2010 - Aberto". Isso separa o resumo do contrato dos eventos da
# linha do tempo (ex.: "01/02/2020 - Admissao"), que tem a mesma cara mas
# NAO sao vinculos novos.
PADRAO_LINHA_CONTRATO_CTPS = re.compile(
    r'^\s*\d{2}/\d{2}/\d{4}\s*-\s*(?:\d{2}/\d{2}/\d{4}|Aberto)\s*$'
)


def parse_vinculos(texto, origem):
    """Extrai vinculos de um texto (CNIS ou CTPS).

    Exige data completa (DD/MM/AAAA) e uma ancora especifica de formato por
    origem (ver PADRAO_LINHA_VINCULO_CNIS / PADRAO_LINHA_CONTRATO_CTPS).
    Isso evita dois falsos positivos observados em documentos reais:
    1) linhas da tabela de remuneracoes do CNIS (so tem MM/AAAA, sem NIT);
    2) fragmentos de CNPJ/matricula (ex.: "853/0001") sendo lidos como data,
       o que acontecia com o regex antigo (\\d{2}/\\d{4}) aplicado a linha
       inteira, incluindo o proprio CNPJ do empregador.
    """
    vinculos = []

    for linha in texto.split('\n'):
        if origem == "CNIS":
            if not PADRAO_LINHA_VINCULO_CNIS.match(linha):
                continue
        else:
            if not PADRAO_LINHA_CONTRATO_CTPS.match(linha):
                continue

        datas_completas = PADRAO_DATA_COMPLETA.findall(linha)
        if not datas_completas:
            continue

        cnpj_match = PADRAO_CNPJ.search(linha)
        admissao = datas_completas[0]
        em_curso = len(datas_completas) < 2

        if em_curso:
            # Sem Data Fim: o vinculo segue ativo. Usa a Ult. Remuneracao
            # (MM/AAAA, aparece apos a Data Inicio no extrato do CNIS) como
            # prova de que o vinculo persistia ate aquela competencia — NAO
            # e uma data de rescisao, por isso o campo em_curso fica True.
            resto = linha.split(admissao, 1)[-1]
            mes_ano_apos = PADRAO_MES_ANO.findall(resto)
            demissao = mes_ano_apos[-1] if mes_ano_apos else None
        else:
            demissao = datas_completas[1]

        vinculos.append({
            "empregador": linha.strip()[:120],
            "cnpj": cnpj_match.group() if cnpj_match else None,
            "admissao": admissao,
            "demissao": demissao,
            "origem": origem,
            "em_curso": em_curso
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


def periodo_para_intervalo(vinculo):
    """Converte admissao/demissao de um vinculo em (inicio_idx, fim_idx), indice
    absoluto de meses (0-based) a partir do ano 0. Retorna None se nao houver
    data de admissao valida."""
    a = normalizar_mes_ano(vinculo.get("admissao"))
    if not a:
        return None
    d = normalizar_mes_ano(vinculo.get("demissao"))

    inicio = a[0] * 12 + (a[1] - 1)
    fim = (d[0] * 12 + (d[1] - 1)) if d else inicio
    if fim < inicio:
        inicio, fim = fim, inicio
    return (inicio, fim)


def idx_para_mes_ano(idx):
    """Inverte o indice absoluto de meses para 'MM/AAAA'."""
    ano, mes = divmod(idx, 12)
    return f"{mes + 1:02d}/{ano:04d}"


def unir_periodos(vinculos):
    """
    Une periodos de vinculos concomitantes (sobrepostos ou contiguos).

    Sem isso, um segurado com dois vinculos simultaneos (ex.: dois empregos no
    mesmo mes, ou um cadastro duplicado no CNIS) teria o mesmo periodo contado
    duas vezes na soma do tempo de contribuicao — o que é vedado, pois tempo
    concomitante nao se soma para fins de tempo de contribuicao (apenas pode
    impactar o salario de contribuicao/RMI).

    Retorna um dict com:
      - total_meses: meses cobertos pela UNIAO dos intervalos (sem duplicidade)
      - intervalos_unidos: lista de {inicio, fim, vinculos: [...]}
      - concomitancias: subconjunto de intervalos_unidos com mais de 1 vinculo
    """
    itens = []
    for v in vinculos:
        intervalo = periodo_para_intervalo(v)
        if intervalo:
            itens.append((intervalo[0], intervalo[1], v))

    itens.sort(key=lambda x: (x[0], x[1]))

    unidos = []
    for inicio, fim, vinculo in itens:
        if unidos and inicio <= unidos[-1]["fim"] + 1:
            unidos[-1]["fim"] = max(unidos[-1]["fim"], fim)
            unidos[-1]["vinculos"].append(vinculo)
        else:
            unidos.append({"inicio": inicio, "fim": fim, "vinculos": [vinculo]})

    total_meses = sum((u["fim"] - u["inicio"] + 1) for u in unidos)
    concomitancias = [u for u in unidos if len(u["vinculos"]) > 1]

    return {
        "total_meses": total_meses,
        "intervalos_unidos": unidos,
        "concomitancias": concomitancias
    }


def formatar_concomitancias(concomitancias):
    """Serializa concomitancias em formato legivel para o JSON de saida."""
    saida = []
    for grupo in concomitancias:
        saida.append({
            "periodo_unido": f"{idx_para_mes_ano(grupo['inicio'])} a {idx_para_mes_ano(grupo['fim'])}",
            "vinculos": [
                {
                    "empregador": v.get("empregador"),
                    "origem": v.get("origem"),
                    "admissao": v.get("admissao"),
                    "demissao": v.get("demissao")
                }
                for v in grupo["vinculos"]
            ]
        })
    return saida


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

    # Meses a averbar = uniao dos periodos que so existem na CTPS (exclui
    # dupla contagem caso dois vinculos "apenas CTPS" sejam concomitantes).
    uniao_apenas_ctps = unir_periodos(resultado["apenas_ctps"])
    total_meses_a_averbar = uniao_apenas_ctps["total_meses"]

    # Tempo total de contribuicao = uniao de TODO o CNIS + o que so aparece
    # na CTPS, excluindo vinculos concomitantes (nao se soma tempo em
    # duplicidade quando o segurado tem mais de um vinculo no mesmo periodo).
    uniao_total = unir_periodos(vinculos_cnis + resultado["apenas_ctps"])
    total_meses_uniao = uniao_total["total_meses"]

    saida = {
        "resumo": {
            "total_vinculos_cnis": len(vinculos_cnis),
            "total_vinculos_ctps": len(vinculos_ctps),
            "total_apenas_ctps": len(resultado["apenas_ctps"]),
            "total_apenas_cnis": len(resultado["apenas_cnis"]),
            "total_divergencias_datas": len(resultado["divergencias_datas"]),
            "meses_a_averbar": total_meses_a_averbar,
            "tempo_total_uniao_meses": total_meses_uniao,
            "tempo_total_uniao_anos_meses": f"{total_meses_uniao // 12}a {total_meses_uniao % 12}m",
            "vinculos_concomitantes_detectados": len(uniao_total["concomitancias"])
        },
        "apenas_ctps": resultado["apenas_ctps"],
        "apenas_cnis": resultado["apenas_cnis"],
        "divergencias_datas": resultado["divergencias_datas"],
        "concomitancias": formatar_concomitancias(uniao_total["concomitancias"])
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(saida, f, indent=2, ensure_ascii=False)

    print(f"OK: {args.output}")
    print(f"Vinculos CNIS: {len(vinculos_cnis)}")
    print(f"Vinculos CTPS: {len(vinculos_ctps)}")
    print(f"Apenas CTPS (a averbar): {len(resultado['apenas_ctps'])}")
    print(f"Meses a averbar: {total_meses_a_averbar}")
    print(f"Vinculos concomitantes detectados: {len(uniao_total['concomitancias'])}")
    print(f"Tempo total (uniao, sem duplicar concomitancia): {saida['resumo']['tempo_total_uniao_anos_meses']}")


if __name__ == "__main__":
    main()
