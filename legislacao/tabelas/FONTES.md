# Fontes das Tabelas de Cálculo

Este documento registra a origem oficial dos dados usados em `inpc-historico.csv`
e `tetos-rgps-historico.csv`. Os CSVs ainda estão **vazios (só cabeçalho)** —
os dados numéricos serão preenchidos manualmente a partir das fontes abaixo.

## 1. Qual índice usar — CJF (SICOM), não a tabela administrativa do INSS

Este escritório atua no JEF-PE/TRF-5 (`practice-profile.md`). Para correção de
parcelas vencidas de benefício previdenciário em juízo, prevalece o índice do
**Conselho da Justiça Federal (CJF)**, não a tabela administrativa do INSS.
A posição do CJF é que parcelas vencidas de benefício previdenciário devem ser
atualizadas pelo **INPC**. Usar a tabela do INSS isoladamente pode gerar valor
divergente do que o juízo/contadoria judicial vai homologar.

- SICOM — Sistema de Correção Monetária (CJF): https://sicom.cjf.jus.br/
- Notícia CJF sobre o critério de atualização (INPC): https://www.cjf.jus.br/cjf/noticias/2018/maio/parcelas-vencidas-de-beneficio-previdenciario-devem-ser-atualizadas-pelo-inpc

**Status:** URL registrada. Dados ainda não baixados.
**Data de download:** _(preencher quando os CSVs forem populados)_

## 2. Manual de Cálculos da Justiça Federal 2025 — referência para conferência manual

Use este manual para conferir manualmente o resultado de qualquer cálculo
gerado por script antes de levar a número a uma petição. Ele traz a
metodologia oficial de atualização monetária adotada pela Justiça Federal
(Resolução CJF n. 963/2025).

- Manual de Cálculos da Justiça Federal 2025 (PDF): https://sicom.cjf.jus.br/arquivos/pdf/manual_de_calculos_2025_vf.pdf
- Resolução CJF n. 963, de 22/07/2025: https://www.cjf.jus.br/publico/biblioteca/Res_963-2025.pdf

**Status:** URL registrada. Ainda não usado para conferência de nenhum cálculo deste escritório.

## 3. Série bruta do INPC — IBGE/SIDRA Tabela 1736

Fonte primária do índice, caso seja necessário reconstruir ou conferir a série
usada pelo CJF/SICOM. Série histórica com número-índice, variação mensal e
variações acumuladas, a partir de abril/1979 (base dezembro/1993 = 100).

- IBGE/SIDRA — Tabela 1736: https://sidra.ibge.gov.br/tabela/1736

**Status:** URL registrada. Dados ainda não baixados.

## 4. Teto e piso do RGPS por período

- INSS — Tabela de contribuição – histórico: https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal/tabela-de-contribuicao-historico
- Valor vigente em 2026 (já registrado em `legislacao/INDICE.md`, seção 7):
  Portaria Interministerial MPS/MF 13/2026 — teto R$ 8.475,55, piso (salário
  mínimo) R$ 1.621,00.

**Status:** URL registrada. Série histórica completa (1994–hoje) ainda não baixada.

## Como preencher os CSVs

`inpc-historico.csv` — uma linha por competência:
```
competencia,indice_inpc,variacao_mensal
04/1997,<numero-indice>,<variacao-percentual-do-mes>
```

`tetos-rgps-historico.csv` — uma linha por competência (o teto/piso só muda
quando há reajuste, mas registre competência a competência para permitir
lookup direto sem lógica de "vigência entre datas"):
```
competencia,teto_rgps,piso_salario_minimo
04/1997,<teto-vigente>,<piso-vigente>
```

Formato de `competencia`: sempre `MM/AAAA`, mesmo padrão usado em
`cruza_cnis_ctps.py`.

## Como validar

Depois de preencher os CSVs, rode:

```
python3 .claude/skills/calculo-tempo-contribuicao/scripts/calcula_tempo.py --validar-tabelas
```

Isso confere, para cada tabela: presença das colunas esperadas, formato de
`competencia` (MM/AAAA), valores numéricos válidos nas demais colunas, e se
há lacunas (meses faltantes) na série. Não gera nenhum cálculo de caso —
serve só para validar a integridade dos dados antes de usá-los.

## Registro de atualização

| Tabela | Data de download | Fonte usada | Responsável |
|---|---|---|---|
| inpc-historico.csv | _pendente_ | _pendente_ | _pendente_ |
| tetos-rgps-historico.csv | _pendente_ | _pendente_ | _pendente_ |

Atualize esta tabela toda vez que os CSVs forem repopulados, para que o
advogado saiba a validade/data-base de cada número usado em um cálculo.
