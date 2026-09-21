# RASCUNHO — PARA REVISÃO DO ADVOGADO

> Documento produzido por sistema de apoio (`calculo-previdenciario`). Nenhum número aqui
> apurado autoriza protocolo de requerimento administrativo ou peça processual sem
> conferência do profissional habilitado.
> Data deste fechamento: 21/09/2026 · Cliente: **JULIO CESAR DA SILVA** (CPF 030.896.214-10,
> nascido 04/05/1977, sexo masculino).
> Base: `casos/2026-001/analises/triagem.md` + `casos/2026-001/analises/calculo.md` (tempo de
> contribuição e tempo especial já apurados e não recalculados aqui) + tabelas oficiais de
> correção monetária e teto, agora populadas em `legislacao/tabelas/`.

---

## 0. Confirmação de identidade e de dados de base

Conferido diretamente em `triagem.md` (Seção 1) e `calculo.md` (cabeçalho): o cliente deste
caso é **JULIO CESAR DA SILVA**, CPF 030.896.214-10, nascido 04/05/1977, masculino. Não há,
nestes documentos, qualquer outro nome associado ao caso 2026-001. Todos os dados usados
abaixo vêm exclusivamente de `triagem.md` e `calculo.md`, mais a reextração própria do CNIS
descrita na Seção 2.

---

## 1. Tabelas oficiais — confirmação de carregamento e validação

Executado `python3 .claude/skills/calculo-tempo-contribuicao/scripts/calcula_tempo.py --validar-tabelas`:

```
--- legislacao/tabelas/inpc-historico.csv ---
OK: 570 competencias, sem lacunas, todas as colunas validas

--- legislacao/tabelas/tetos-rgps-historico.csv ---
OK: 444 competencias, sem lacunas, todas as colunas validas

RESULTADO: tabelas validas
```

- `inpc-historico.csv`: 03/1979 a 08/2026 (570 competências).
- `tetos-rgps-historico.csv`: 01/1990 a 12/2026 (444 competências).

Competência de referência para a correção monetária adotada: **08/2026** (última competência
disponível na série do INPC; a série de teto vai até 12/2026, mas isso não afeta a correção,
apenas a checagem de teto vigente em cada competência histórica e o teto atual de referência).

---

## 2. Metodologia

### 2.1 Extração do CNIS

Não havia, neste ambiente, arquivo de trabalho com os salários já extraídos e individualizados
(apenas a referência, em `calculo.md`, a "314 competências... disponíveis no arquivo de
trabalho", não commitado). Reextraído com `pdftotext -layout casos/2026-001/documentos/CNIS.pdf`
(13 páginas, texto nativo, íntegra e legível). Foram parseados dois formatos de tabela
presentes no extrato:

1. Vínculos "Empregado ou Agente Público" (seqs. 1, 3, 4, 5, 6, 7, 10): tabela repetida
   "MM/AAAA valor MM/AAAA valor MM/AAAA valor".
2. Vínculos "Contribuinte Individual/Cooperado" (seqs. 8 e 9, COOPSERSA): tabela com colunas
   Competência / Contratante / Estabelecimento / Tomador / Forma de Prestação / Remuneração —
   exige um segundo padrão de extração (a primeira tentativa de parsing, só com o padrão 1,
   **perdia silenciosamente** os 3 lançamentos da COOPSERSA como contribuinte individual:
   04/2023 R$1.464,46, 05/2023 R$120,78 e 11/2023 R$1.853,50).

**Concomitância de vínculos:** tratada por soma dos valores de todos os vínculos ativos na
mesma competência, sem soma de tempo, conforme já feito em `calculo.md`.

**Validação cruzada da extração:** o próprio CNIS traz, na página 12, a tabela "Valores
Consolidados por Ano Civil" (2019-2026). Comparando essa tabela oficial com a soma por
competência obtida na extração própria:

- **68 de 79 competências conferidas batem exatamente** (diferença ≤ R$0,02).
- **1 competência (04/2023)** diverge porque o valor consolidado oficial (R$7.507,49) já vem
  **capado no teto RGPS da época** (R$7.507,49 — conferido em
  `tetos-rgps-historico.csv`), enquanto a soma bruta dos vínculos ativos nesse mês
  (Hospitais Associados + FMS + COOPSERSA) totaliza R$7.866,59. Isso **confirma
  independentemente** a necessidade do capeamento por teto histórico (Seção 3 abaixo) e valida
  a extração.
- **11 competências (02/2020 a 12/2020)** divergem porque a tabela oficial "Valores
  Consolidados" **exclui** a remuneração do vínculo Hospital de Ávila nesses meses — vínculo
  que carrega o indicador **PREM-BLOQ-EC103** ("Pendência de bloqueio de remuneração/
  contribuição para ajuste entre competências"). Ou seja, o próprio sistema do INSS está,
  hoje, **represando** esses ~11 lançamentos (R$1.284,70 a R$1.740,84/mês) até uma conferência
  manual. **Achado novo desta apuração, não quantificado antes** — ver ressalva na Seção 3.2.

**Não foi necessário usar a estimativa de fallback (médias nominais da Seção 8.2 de
`calculo.md`)** — a extração individualizada de todas as competências foi bem-sucedida e
validada linha a linha contra os "Valores Consolidados" do próprio CNIS.

### 2.2 Correção monetária (INPC)

Para cada competência com remuneração:

```
valor_corrigido = valor_capado_no_teto × (índice_INPC_08/2026 / índice_INPC_da_competência)
```

Índice de referência (08/2026): **7.810,09** (`inpc-historico.csv`).

### 2.3 Teto histórico

Para cada competência, o valor **nominal** (antes da correção) foi comparado ao `teto_rgps` da
mesma competência em `tetos-rgps-historico.csv`. Onde o nominal ultrapassava o teto, o valor foi
capado nesse teto **antes** de aplicar a correção monetária.

**Resultado:** das 314 competências com remuneração (04/1997 a 05/2026, idêntico ao total já
apurado em `calculo.md`, Seção 7.1), **apenas 1 (04/2023)** precisou de capeamento — de
R$7.866,59 (soma bruta) para R$7.507,49 (teto da competência).

---

## 3. Salário de benefício (SB)

### 3.1 Período-base

Cliente iniciou contribuições em 04/1997 (**após** 07/1994) — pela Lei 8.213/1991, art. 29-A,
a média usa **todas** as competências com remuneração desde o início da vida contributiva
(não desde 07/1994). Usadas as 314 competências com remuneração, de 04/1997 a 05/2026 (última
competência com remuneração lançada no CNIS na data de emissão do extrato, 11/06/2026).

> **Nota sobre a DER:** como a data exata do requerimento ainda não está definida (três
> cenários de DIB, ver Seção 6), usa-se aqui o mesmo recorte já adotado em `calculo.md`
> (todas as competências disponíveis no CNIS até a última remuneração lançada, 05/2026), que é
> a aproximação mais completa disponível hoje. **Se a DER real vier a ocorrer em competência
> posterior com novas remunerações, o SB deve ser refeito** incluindo essas competências
> adicionais.

### 3.2 Resultado

| Métrica | Valor |
|---|---|
| Competências com remuneração (04/1997-05/2026) | 314 |
| Competências que precisaram de capeamento no teto | 1 (04/2023) |
| Média nominal capada, **sem** correção INPC (referência de ordem de grandeza) | R$ 2.021,66 |
| **SB corrigido pelo INPC (ref. 08/2026)** — soma integral de todos os vínculos ativos por competência | **R$ 3.288,02** |
| SB corrigido — cenário alternativo excluindo as 11 competências PREM-BLOQ-EC103 (Hospital de Ávila, 02-12/2020) | R$ 3.221,65 |
| Diferença entre os dois cenários | R$ 66,37 (≈ 2%) |

**SB adotado para o fechamento da RMI: R$ 3.288,02** (soma integral de todos os vínculos,
mesma metodologia de `calculo.md`, Seção 2, item 4 — "todas as 314 competências... somadas por
competência, tratando concomitância por soma de valores").

**[PENDÊNCIA A ESCLARECER]** — a divergência PREM-BLOQ-EC103 (2.2 acima) é uma pendência real e
ainda não resolvida na fonte (o próprio CNIS ainda não consolidou esses 11 valores). O impacto
no SB é pequeno (R$66,37, ≈2%), mas **não é zero**, e a resolução dessa pendência no CNIS
(retificação/liberação do bloqueio) deve ocorrer **antes** de qualquer simulação oficial no
Meu INSS/PRISMA, para que o valor seja o mesmo usado pelo INSS na concessão.

**Ressalva herdada de `calculo.md` (Seção 7.2, item a):** a competência SOSERVI duplicada
(seq. 2 do CNIS, 04-09/1997) foi somada como vínculo concomitante, conforme metodologia
adotada; se se confirmar tratar-se de duplicidade cadastral (não vínculo real distinto), o SB
pode sofrer pequeno ajuste para baixo nesse trecho (impacto marginal, competências de 1997 têm
peso baixo na média por INPC).

Não há valor mínimo (salário mínimo por competência) que reduza a base de cálculo abaixo do
observado — todas as competências capadas ficaram acima do salário mínimo da época.

---

## 4. Coeficiente aplicado

**Base:** tempo especial documentado (PPP), já apurado em `calculo.md`, Seção 5.1: **27 anos e
8 meses**, até 10/12/2024 (marco dos 25 anos de efetiva exposição em ≈09-10/04/2022).

Fórmula: RMI = coeficiente × SB; coeficiente = 60% + 2% por ano que exceder o piso de anos
aplicável à modalidade.

| Cenário de piso | Piso (anos) | Excedente sobre o piso | Coeficiente | Fonte / status |
|---|---|---|---|---|
| **Original — `calculo.md`, Seção 8.1** | 25 anos | 2,667 anos (27a8m − 25a) | **≈ 65,33%** | Piso adotado por ser "o piso da modalidade efetivamente pleiteada" (agente biológico, Anexo IV, 3.0.1); marcado desde então como **[BASE NORMATIVA A CONFIRMAR]** |
| **Instrução da advogada responsável para este caso (nova, desta apuração)** | 20 anos | 7,667 anos (27a8m − 20a) | **≈ 75,33%** | Ver ressalva abaixo — **[DISPOSITIVO A CONFIRMAR]** |

### 4.1 Ressalva obrigatória sobre o piso de 20 vs. 25 anos

A advogada responsável por este caso orientou que, para a categoria de 25 anos de efetiva
exposição (a deste cliente), o piso do bônus de 2% ao ano seria de **20 anos**, e não de 25 —
raciocínio de que o bônus da aposentadoria especial usaria sempre o piso "imediatamente
inferior" da tabela de categorias (15/20/25 anos).

**[DISPOSITIVO A CONFIRMAR — regra informada pela advogada responsável; o art. 26, § 2º da
EC 103/2019 não consta em texto integral na base `legislacao/`, que só tem
`legislacao/INDICE.md`.]** O próprio `INDICE.md` (item 2) registra a fórmula "60% da média +
2% por ano acima de 20/15 anos" no contexto da **aposentadoria por tempo de contribuição**
(regra permanente do art. 19, caput: 20 anos homem / 15 anos mulher) — não fica claro, sem o
texto integral do art. 26, § 2º, se essa mesma referência de "20/15" se aplica **também** ao
bônus da aposentadoria **especial** de 25 anos, ou se a especial de 25 anos usa piso próprio de
25 anos (como `calculo.md` havia adotado provisoriamente).

**Isto diverge do que `calculo.md` (Seção 8.1) assumiu provisoriamente** (piso de 25 anos,
coeficiente ≈65,3%, excedente de 2,67 anos). **O número antigo não foi apagado** — está mantido
na tabela acima e em `calculo.md` — apenas passa a conviver, nesta apuração, com o número
alternativo de 75,33%, calculado por instrução da advogada e **sujeito a confirmação no texto
legal antes de qualquer uso em petição, requerimento administrativo ou comunicação ao
cliente sobre valor de benefício.**

Enquanto não houver essa confirmação, a RMI deste caso deve ser tratada como uma **faixa**,
não como um número único (Seção 5).

---

## 5. RMI final

| Cenário de coeficiente | Coeficiente | SB | **RMI** |
|---|---|---|---|
| Piso 25 anos (original, `calculo.md` 8.1) | 65,33% | R$ 3.288,02 | **R$ 2.148,17** |
| Piso 20 anos (instrução da advogada — a confirmar) | 75,33% | R$ 3.288,02 | **R$ 2.476,98** |

**RMI estimada: entre R$ 2.148,17 e R$ 2.476,98**, a depender da confirmação do piso do bônus
de 2% (Seção 4.1). **Nenhum dos dois valores deve ser comunicado ao cliente ou usado em peça
como número definitivo** até essa confirmação — mas ambos aplicam corretamente a fórmula
legal, variando apenas o parâmetro do piso.

### 5.1 Comparação com o teto e com o salário mínimo

- **Teto vigente (Portaria MPS/MF 13/2026, `legislacao/INDICE.md` item 7 e última linha de
  `tetos-rgps-historico.csv`): R$ 8.475,55.** Ambos os cenários de RMI (R$2.148,17 e
  R$2.476,98) estão **muito abaixo do teto** — o teto não é fator limitante neste caso,
  confirmando a observação já feita na triagem e em `calculo.md`.
- **Salário mínimo vigente: R$ 1.621,00.** Ambos os cenários de RMI estão **acima** do salário
  mínimo — não se aplica a regra de elevação da RMI ao piso do salário mínimo.

---

## 6. DIB — três cenários (referência: `calculo.md`, "Reanálise Pós-ADI 6309", 04/09/2026)

Não recalculada aqui — a análise jurídica completa está em `calculo.md`. Resumo dos três
cenários, hoje = **21/09/2026**:

| # | Cenário de modulação da ADI 6309/DF | DIB provável |
|---|---|---|
| 1 | Sem modulação (efeito retroativo pleno) | **≈ 09-10/04/2022** |
| 2 | Modulação a partir da data do julgamento | **03/06/2026** |
| 3 | Sem efeito retroativo (via administrativa padrão) | **Data do requerimento administrativo (DER)**, ainda não protocolado |

**Prescrição quinquenal (Lei 8.213/1991, art. 103):** hoje (21/09/2026) menos 5 anos =
**21/09/2021**. Nenhum dos três cenários de DIB é anterior a essa data — **a prescrição
quinquenal não atinge nenhuma parcela em nenhum dos três cenários, na data de hoje.**

---

## 7. Retroativos aproximados por cenário (ordem de grandeza)

**Metodologia simplificada, conforme instrução:** retroativos ≈ nº de meses entre a DIB do
cenário e hoje (21/09/2026) × RMI atual (nominal). **Isto NÃO substitui** a atualização
mês a mês de cada parcela vencida (que teria seu próprio valor real na época) nem o cômputo de
juros de mora — cálculo fora do escopo desta apuração, a ser feito com o simulador oficial
(PRISMA/Meu INSS) ou planilha própria do escritório antes de qualquer execução.

| Cenário DIB | Meses decorridos até hoje (aprox.) | Retroativos aprox. — RMI piso 25 (R$2.148,17) | Retroativos aprox. — RMI piso 20 (R$2.476,98) |
|---|---|---|---|
| 1 — ≈10/04/2022 (sem modulação) | ≈ 53 meses | **≈ R$ 113.853** | **≈ R$ 131.280** |
| 2 — 03/06/2026 (modulação no julgamento) | ≈ 3 meses | **≈ R$ 6.445** | **≈ R$ 7.431** |
| 3 — data do requerimento (sem retroação) | 0 (benefício só passa a ser devido a partir da DER futura) | **R$ 0** de retroativo — apenas parcelas mensais a partir da concessão | **R$ 0** de retroativo — idem |

Nenhum dos três cenários é afetado pela prescrição quinquenal na data de hoje (Seção 6).

---

## 8. Ressalvas finais

1. **Este documento é RASCUNHO**, sujeito a revisão do advogado responsável (CLAUDE.md, regra 1;
   protocolo do agente `calculo-previdenciario`). Nenhum número aqui autoriza protocolo de
   requerimento ou peça processual.
2. **A RMI não é um número único nesta apuração** — é uma faixa (R$2.148,17 a R$2.476,98),
   porque um dos dois parâmetros da fórmula (piso do bônus de 2% para a aposentadoria especial:
   20 ou 25 anos) está marcado **[DISPOSITIVO A CONFIRMAR]**, por falta de texto integral do
   art. 26, §2º da EC 103/2019 na base `legislacao/` (que só contém `INDICE.md`). **Antes de
   qualquer petição, requerimento administrativo ou comunicação de valor ao cliente, o
   advogado deve confirmar essa redação na fonte oficial e optar por um dos dois cenários** (ou
   obter ambos os pareceres, se a estratégia comportar impugnação do critério adotado pelo
   INSS).
3. **Nenhuma jurisprudência é afirmada como definitiva.** A ADI 6309/DF segue com trânsito em
   julgado e modulação de efeitos pendentes de confirmação oficial (ver `calculo.md` e
   `triagem.md`, Seção 9.2) — os três cenários de DIB e retroativos (Seções 6-7) dependem
   dessa confirmação.
4. **Nenhum diagnóstico médico é mencionado** — não é matéria deste cálculo.
5. **Achado novo desta apuração:** indicador **PREM-BLOQ-EC103** no vínculo Hospital de Ávila
   (11 competências, 02-12/2020) já está sendo **excluído pelo próprio sistema do INSS** dos
   "Valores Consolidados" do CNIS, pendente de ajuste manual. Impacto no SB é pequeno (≈2%,
   R$66,37) mas deve ser resolvido/retificado no CNIS antes de qualquer simulação oficial, para
   que o valor usado na concessão não surpreenda o escritório.
6. Os retroativos da Seção 7 são **estimativa de ordem de grandeza** (RMI atual × meses), não
   valor de execução. O valor real exigiria atualização monetária mês a mês de cada parcela
   vencida (pelo índice vigente à época de cada competência em atraso) mais juros de mora —
   tarefa de liquidação, fora do escopo desta apuração.
7. Mantidas as pendências já registradas em `calculo.md` (Seção 10): PPP atualizado dos dois
   vínculos ativos, PPP retificado da COOPSERSA, fichas de pagamento da SOSERVI para as ~36
   competências sem remuneração lançada, e confirmação da redação exata dos arts. 21 e 26 da
   EC 103/2019.
8. `practice-profile.md` contém dados de teste ("Escritório: Teste", "OAB: Teste") — substituir
   antes de qualquer uso em produção.

---

## Anexo — dados de apoio (não commitados como arquivo de trabalho do caso)

Scripts e planilhas intermediárias de extração/correção usados nesta apuração ficaram no
diretório de scratch da sessão, não no repositório do caso (mesma prática já observada em
`calculo.md`). Caso o escritório queira preservar o detalhamento competência a competência
(314 linhas: nominal, capeamento, índice INPC aplicado, valor corrigido), deve ser solicitada
a regeneração e o commit explícito desse anexo em `casos/2026-001/documentos/` ou
`casos/2026-001/analises/`.

---
*Relatório gerado pelo agente `calculo-previdenciario` · Caso 2026-001 · 21/09/2026*
