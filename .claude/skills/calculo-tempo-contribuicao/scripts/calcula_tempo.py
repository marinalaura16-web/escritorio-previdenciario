#!/usr/bin/env python3
"""
Calcula cenarios de aposentadoria a partir do resultado do cruzamento CNIS x CTPS.

Uso:
    python calcula_tempo.py --input divergencias.json --output resultado.json --nascimento 15/03/1965 --sexo M

Validacao das tabelas de calculo (INPC e teto do RGPS), sem rodar nenhum
calculo de caso:
    python calcula_tempo.py --validar-tabelas
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime


# Raiz do repositorio, calculada a partir da localizacao deste script
# (.claude/skills/calculo-tempo-contribuicao/scripts/calcula_tempo.py),
# para que --validar-tabelas funcione independente do diretorio atual.
RAIZ_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TABELA_INPC_PADRAO = os.path.join(RAIZ_REPO, "legislacao", "tabelas", "inpc-historico.csv")
TABELA_TETO_PADRAO = os.path.join(RAIZ_REPO, "legislacao", "tabelas", "tetos-rgps-historico.csv")

PADRAO_COMPETENCIA = re.compile(r'^(0[1-9]|1[0-2])/\d{4}$')


def _competencia_para_indice(competencia):
    mes, ano = competencia.split('/')
    return int(ano) * 12 + int(mes)


def validar_tabela(caminho, colunas_esperadas, colunas_texto=frozenset()):
    """Valida uma tabela CSV de calculo: colunas, formato de competencia,
    valores numericos e lacunas na serie mensal.

    colunas_texto: colunas dentre colunas_esperadas[1:] que sao texto livre
    (ex.: observacao com o simbolo da moeda) e por isso ficam isentas da
    checagem numerica — podem inclusive estar vazias.

    Retorna (ok: bool, mensagens: list[str]).
    """
    mensagens = []

    if not os.path.isfile(caminho):
        return False, [f"Arquivo nao encontrado: {caminho}"]

    with open(caminho, 'r', encoding='utf-8', newline='') as f:
        leitor = csv.DictReader(f)
        colunas = leitor.fieldnames or []
        if colunas != colunas_esperadas:
            mensagens.append(
                f"Colunas incorretas. Esperado {colunas_esperadas}, encontrado {colunas}"
            )
            return False, mensagens

        linhas = list(leitor)

    if not linhas:
        mensagens.append("Tabela vazia (so tem cabecalho) — dados ainda nao preenchidos")
        return False, mensagens

    competencias = []
    for i, linha in enumerate(linhas, start=2):  # linha 1 e o cabecalho
        competencia = linha.get("competencia", "")
        if not PADRAO_COMPETENCIA.match(competencia):
            mensagens.append(f"Linha {i}: competencia invalida ou fora do formato MM/AAAA: '{competencia}'")
            continue

        for coluna in colunas_esperadas[1:]:
            if coluna in colunas_texto:
                continue
            valor = linha.get(coluna, "")
            try:
                float(valor.replace(",", "."))
            except (ValueError, AttributeError):
                mensagens.append(f"Linha {i}: valor nao numerico em '{coluna}': '{valor}'")

        competencias.append(_competencia_para_indice(competencia))

    competencias.sort()
    for anterior, atual in zip(competencias, competencias[1:]):
        if atual - anterior > 1:
            mensagens.append(
                f"Lacuna na serie: faltam competencias entre indice {anterior} e {atual}"
            )

    ok = len(mensagens) == 0
    if ok:
        mensagens.append(f"OK: {len(linhas)} competencias, sem lacunas, todas as colunas validas")
    return ok, mensagens


def validar_tabelas(caminho_inpc=TABELA_INPC_PADRAO, caminho_teto=TABELA_TETO_PADRAO):
    """Valida as duas tabelas de calculo. Nao executa nenhum calculo de caso."""
    tudo_ok = True

    print(f"--- {caminho_inpc} ---")
    ok, mensagens = validar_tabela(caminho_inpc, ["competencia", "indice_inpc", "variacao_mensal"])
    tudo_ok = tudo_ok and ok
    for m in mensagens:
        print(m)

    print()
    print(f"--- {caminho_teto} ---")
    ok, mensagens = validar_tabela(
        caminho_teto,
        ["competencia", "teto_rgps", "piso_salario_minimo", "observacao"],
        colunas_texto={"observacao"}
    )
    tudo_ok = tudo_ok and ok
    for m in mensagens:
        print(m)

    print()
    print("RESULTADO: tabelas validas" if tudo_ok else "RESULTADO: ha problemas nas tabelas — veja acima")
    return tudo_ok


REGRAS_TRANSICAO = {
    "pontos": {
        "mulher": {"pontos": 93, "tempo_min": 30},
        "homem": {"pontos": 103, "tempo_min": 35},
    },
    "idade_progressiva": {
        "mulher": {"idade": 59.5, "tempo_min": 30},
        "homem": {"idade": 64.5, "tempo_min": 35},
    },
}

APOSENTADORIA_IDADE = {
    "mulher": {"idade": 62, "carencia_anos": 15},
    "homem": {"idade": 65, "carencia_anos": 20},
}


def calcular_idade(nascimento_str, referencia=None):
    """Retorna idade em anos (float)."""
    nasc = datetime.strptime(nascimento_str, "%d/%m/%Y")
    ref = referencia or datetime.now()
    anos = ref.year - nasc.year
    meses = ref.month - nasc.month
    if ref.day < nasc.day:
        meses -= 1
    if meses < 0:
        anos -= 1
        meses += 12
    return anos + meses / 12


def simular_cenario(regra, idade_atual, tempo_anos, carencia_anos, sexo):
    regra_sexo = REGRAS_TRANSICAO.get(regra, {}).get(sexo, {})
    resultado = {
        "regra": regra,
        "requisitos": regra_sexo,
        "idade_atual": round(idade_atual, 1),
        "tempo_atual": round(tempo_anos, 1),
        "carencia_atual": round(carencia_anos, 1),
        "atendido": False,
        "faltam": {}
    }

    if regra == "pontos":
        pontos_atual = idade_atual + tempo_anos
        resultado["pontos_atual"] = round(pontos_atual, 1)
        resultado["faltam"]["pontos"] = round(max(0, regra_sexo["pontos"] - pontos_atual), 1)
        resultado["faltam"]["tempo_min"] = round(max(0, regra_sexo["tempo_min"] - tempo_anos), 1)
        resultado["atendido"] = pontos_atual >= regra_sexo["pontos"] and tempo_anos >= regra_sexo["tempo_min"]

    elif regra == "idade_progressiva":
        resultado["faltam"]["idade"] = round(max(0, regra_sexo["idade"] - idade_atual), 1)
        resultado["faltam"]["tempo_min"] = round(max(0, regra_sexo["tempo_min"] - tempo_anos), 1)
        resultado["atendido"] = idade_atual >= regra_sexo["idade"] and tempo_anos >= regra_sexo["tempo_min"]

    return resultado


def simular_aposentadoria_idade(idade_atual, carencia_anos, sexo):
    req = APOSENTADORIA_IDADE[sexo]
    return {
        "regra": "aposentadoria_idade",
        "requisitos": req,
        "idade_atual": round(idade_atual, 1),
        "carencia_atual": round(carencia_anos, 1),
        "faltam": {
            "idade": round(max(0, req["idade"] - idade_atual), 1),
            "carencia": round(max(0, req["carencia_anos"] - carencia_anos), 1)
        },
        "atendido": idade_atual >= req["idade"] and carencia_anos >= req["carencia_anos"]
    }


def main():
    parser = argparse.ArgumentParser(description="Calcula cenarios de aposentadoria")
    parser.add_argument("--input", help="JSON do cruza_cnis_ctps.py")
    parser.add_argument("--output", help="JSON de saida")
    parser.add_argument("--nascimento", help="Data DD/MM/AAAA")
    parser.add_argument("--sexo", choices=["M", "F"])
    parser.add_argument("--tempo-cnis-anos", type=float, default=0, help="Tempo de contribuicao apurado no CNIS em anos")
    parser.add_argument(
        "--validar-tabelas", action="store_true",
        help="Valida legislacao/tabelas/inpc-historico.csv e tetos-rgps-historico.csv "
             "(colunas, formato de competencia, valores numericos, lacunas). "
             "Nao roda calculo de nenhum caso."
    )
    args = parser.parse_args()

    if args.validar_tabelas:
        tudo_ok = validar_tabelas()
        raise SystemExit(0 if tudo_ok else 1)

    faltando = [nome for nome, valor in [
        ("--input", args.input), ("--output", args.output),
        ("--nascimento", args.nascimento), ("--sexo", args.sexo)
    ] if not valor]
    if faltando:
        parser.error(f"argumentos obrigatorios ausentes: {', '.join(faltando)}")

    with open(args.input, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    sexo = "mulher" if args.sexo == "F" else "homem"
    idade = calcular_idade(args.nascimento)

    meses_a_averbar = dados.get("resumo", {}).get("meses_a_averbar", 0)
    tempo_a_averbar_anos = meses_a_averbar / 12
    tempo_total_anos = args.tempo_cnis_anos + tempo_a_averbar_anos

    cenarios = []
    for regra in ["pontos", "idade_progressiva"]:
        cenarios.append(simular_cenario(
            regra=regra,
            idade_atual=idade,
            tempo_anos=tempo_total_anos,
            carencia_anos=tempo_total_anos,
            sexo=sexo
        ))

    cenarios.append(simular_aposentadoria_idade(idade, tempo_total_anos, sexo))

    resultado = {
        "dados_entrada": {
            "nascimento": args.nascimento,
            "sexo": args.sexo,
            "idade_atual": round(idade, 1),
            "tempo_cnis_anos": args.tempo_cnis_anos,
            "meses_a_averbar": meses_a_averbar,
            "tempo_a_averbar_anos": round(tempo_a_averbar_anos, 2),
            "tempo_total_considerado": round(tempo_total_anos, 2)
        },
        "observacao": "O agente Claude deve complementar com a formula de RMI (60% da media + 2% por ano acima de 20/15).",
        "cenarios": cenarios,
        "proximos_passos": [
            "Confirmar tempo de contribuicao apurado do CNIS",
            "Aplicar formula de RMI sobre a media salarial",
            "Verificar regras especificas de aposentadoria especial se aplicavel"
        ]
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    print(f"OK: {args.output}")
    print(f"Idade atual: {round(idade, 1)} anos")
    print(f"Tempo total considerado: {round(tempo_total_anos, 2)} anos")
    print(f"Cenarios calculados: {len(cenarios)}")


if __name__ == "__main__":
    main()
