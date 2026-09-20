# TRIAGEM DE VIABILIDADE — CASO 2026-TESTE-001

**Data da análise:** 19/09/2026
**Agente:** triagem-viabilidade
**Natureza do documento:** RASCUNHO para revisão do advogado responsável

---

## NOTA METODOLÓGICA CRÍTICA — LEIA ANTES DO RELATÓRIO

**1. A base legislativa local está vazia.** A pasta `legislacao/` contém apenas
`INDICE.md` e `ATUALIZACAO.md`. Todas as subpastas (`constituicao/`,
`emendas-constitucionais/`, `leis-ordinarias/`, `decretos/`, `instrucoes-normativas/`,
`jurisprudencia-vinculante/`, `leis-complementares/`, `portarias/`, `indices/`) foram
verificadas e **não contêm nenhum arquivo**. O próprio `INDICE.md` reconhece isso em
"Pendências desta base": *"Textos integrais (.html/.pdf) de cada norma ainda não
populados"*.

**2. Os números de artigo foram deliberadamente SUPRIMIDOS deste relatório.** O hook de
validação do projeto (`.claude/hooks/anti-alucinacao.py`) rejeita toda citação no formato
"NORMA, art. N" cujo texto não seja localizável na base — e, estando a base vazia,
**nenhuma citação numérica é verificável**. Optou-se por **não contornar a verificação**
reescrevendo as citações de forma a escapar do padrão detectado. Em vez disso, cada norma
é identificada pela **rubrica constante do `INDICE.md`** (documento efetivamente lido),
com o número do artigo marcado como pendente.

**3. Consequência prática para o advogado:** antes de qualquer uso externo desta análise
(recurso, petição, parecer ao cliente), **os números de artigo devem ser conferidos na
fonte oficial e inseridos manualmente**. A tabela do item 12 lista exatamente quais
dispositivos precisam ser confirmados e onde cada um se aplica.

**4. Nenhuma jurisprudência é citada por número.** A pasta `jurisprudencia-vinculante/`
está vazia. Nenhum número de súmula ou de tema repetitivo foi inferido, deduzido ou
criado.

**5. Nenhum período de contribuição foi presumido.** Todos os períodos apurados decorrem
exclusivamente do CNIS e da CTPS juntados aos autos.

---

## 1. Identificação do caso e do benefício pretendido

| Item | Dado |
|---|---|
| Cliente | MARIA APARECIDA DA SILVA |
| Data de nascimento | 12/05/1968 |
| Idade na DER (15/08/2025) | 57 anos, 3 meses e 3 dias |
| Idade hoje (19/09/2026) | 58 anos, 4 meses e 7 dias |
| NIT | 123.45678.90-1 |
| Profissão declarada | Costureira (em todos os vínculos) |
| Benefício pretendido | Aposentadoria por tempo de contribuição — RGPS |
| Fundamento constitucional | Constituição Federal — rubrica *"Aposentadoria por tempo de contribuição"* (INDICE.md, item 1) — `[NÚMERO DE ARTIGO A CONFIRMAR NA BASE]` |
| Fundamento legal | Lei 8.213/1991 — rubrica *"Aposentadoria por tempo de contribuição"* (INDICE.md, item 4) — `[NÚMEROS A CONFIRMAR NA BASE]` |
| Regra de acesso | EC 103/2019 — regras de transição de 2026 (INDICE.md, item 2) |
| Requerimento administrativo | NB 123.456.789-0 — DER 15/08/2025 |
| Decisão | **INDEFERIDO** em 20/11/2025 |
| Motivo declarado pelo INSS | 28 anos, 4 meses e 12 dias — *"inferiores aos 30 anos exigidos"* |

**Documentos analisados integralmente:** `documentos/cnis.txt`, `documentos/ctps.txt`,
`documentos/carta-indeferimento.txt`. Não há laudos médicos no caso, e nenhum é necessário
ao benefício pretendido. Não se afirma neste relatório nenhum diagnóstico médico.

---

## 2. Quadro de vínculos consolidado

**Método de contagem.** Os documentos registram admissão e demissão apenas em
**mês/ano**, sem indicação de dia. A contagem adota **meses civis completos, do mês de
admissão ao mês de demissão, ambos inclusive**. É aproximação de triagem: a contagem
definitiva exige as **datas exatas (dia/mês/ano)**, a extrair do CNIS analítico e das
folhas da CTPS (diligências 9.3 e 9.4).

| # | Período | Empregador / Qualidade | CNPJ | Fonte | Tempo apurado | Status / Divergência |
|---|---|---|---|---|---|---|
| 1a | 03/1988 – 12/1995 | CONFECÇÕES ALFA LTDA | 12.345.678/0001-90 | CNIS | 7a 10m (94 meses) | **DIVERGÊNCIA 1** — CNIS aponta admissão em **03/1988** |
| 1b | 02/1988 – 12/1995 | CONFECÇÕES ALFA LTDA | 12.345.678/0001-90 | CTPS | 7a 11m (95 meses) | **DIVERGÊNCIA 1** — CTPS aponta admissão em **02/1988**. Delta: **+1 mês** em favor da segurada |
| 2 | 01/1998 – 06/2005 | TÊXTEIS BETA S.A. | 98.765.432/0001-10 | CNIS **e** CTPS | 7a 6m (90 meses) | Convergente — sem divergência |
| 3 | 07/2005 – 12/2005 | CONFECÇÕES DELTA ME | 55.666.777/0001-88 | **Somente CTPS** | 0a 6m (6 meses) | **DIVERGÊNCIA 2** — anotado em CTPS e **ausente do CNIS**. Delta: **+6 meses** |
| 4 | 03/2006 – 07/2010 | Contribuinte individual / autônoma | — | **Somente CNIS** (comprovação por carnê) | 4a 5m (53 meses) | **DIVERGÊNCIA 3** — consta do CNIS, mas **aparentemente não computado pelo INSS** (item 3.3) |
| 5 | 08/2010 – 12/2024 | MODAS GAMA ME | 11.222.333/0001-44 | CNIS **e** CTPS | 14a 5m (173 meses) | Convergente — sem divergência |

**Ausência de sobreposição:** o vínculo DELTA encerra-se em 12/2005 e os carnês iniciam em
03/2006; os carnês encerram-se em 07/2010 e a MODAS GAMA inicia em 08/2010. Cada período é
contado uma única vez.

### 2.1 Hiatos identificados (períodos sem cobertura documental)

| Hiato | Duração | Observação |
|---|---|---|
| 01/1996 – 12/1997 | 24 meses | Sem registro em CNIS nem em CTPS. Investigar trabalho informal, vínculo não anotado ou recolhimento como facultativa |
| 01/2006 – 02/2006 | 2 meses | Entre o fim do vínculo DELTA (12/2005) e o início dos carnês (03/2006) |
| 01/2025 – 19/09/2026 | ~20 meses | Sem contribuição após a saída da MODAS GAMA. **Impacto direto sobre a regra de pontos** — ver item 5.3 |

### 2.2 Detalhamento das divergências, uma a uma

#### DIVERGÊNCIA 1 — CONFECÇÕES ALFA: 02/1988 (CTPS) *vs.* 03/1988 (CNIS)

Diferença de **1 mês**. Causas prováveis: (i) o empregador iniciou os recolhimentos no mês
seguinte ao da admissão; (ii) erro de digitação no cadastro. O período é **anterior à
informatização do CNIS**, o que tende a conferir maior confiabilidade à anotação em CTPS
quanto à data real de início do contrato. A anotação em CTPS goza de presunção de
veracidade `[JURISPRUDÊNCIA A CONFIRMAR — a pasta jurisprudencia-vinculante/ está vazia;
nenhum número de súmula é indicado por ausência de fonte na base]`.

**Impacto:** +1 mês. Irrelevante para os pedágios; **relevante para a regra de pontos**.

#### DIVERGÊNCIA 2 — CONFECÇÕES DELTA ME (07/2005 a 12/2005): na CTPS, ausente do CNIS

É a divergência mais relevante em termos de **ônus probatório**. Tratando-se de
**empregada celetista**, a responsabilidade pelo recolhimento das contribuições é do
**empregador**, e não da segurada — de modo que a omissão do empregador não deveria, por
si só, prejudicar a contagem do tempo `[DISPOSITIVO A CONFIRMAR NA BASE — a matéria situa-
se na Lei 8.212/1991, rubrica "Contribuições e arrecadação" (INDICE.md, item 4), sem texto
integral disponível]`.

**Agravante prático:** trata-se de uma **microempresa de 2005**, provavelmente já baixada,
o que dificulta a produção de prova complementar (diligência 9.5).

**Impacto:** +6 meses. Irrelevante para os pedágios; **decisivo para a regra de pontos**.

#### DIVERGÊNCIA 3 — Contribuinte individual (03/2006 a 07/2010): CNIS *vs.* contagem do INSS

Esta divergência **não é entre CNIS e CTPS**, mas entre o **CNIS e a própria contagem
administrativa**. O período consta expressamente do CNIS ("Contribuições como autônoma:
03/2006 a 07/2010 — comprovadas por carnê") e, ainda assim, a contagem de 28a 4m 12d é
aritmeticamente incompatível com o seu cômputo (demonstração no item 3.3).

**Impacto:** 53 meses (4a 5m). **É o núcleo do caso.**

---

## 3. Contagem de tempo de contribuição

### 3.1 Cenário CONSERVADOR — somente o que consta do CNIS

Exclui o mês de 02/1988 (Divergência 1) e todo o vínculo DELTA (Divergência 2). **Inclui**
o período de autônoma, porque ele consta do **próprio CNIS**.

| Período | Meses |
|---|---|
| ALFA 03/1988 – 12/1995 | 94 |
| BETA 01/1998 – 06/2005 | 90 |
| Autônoma 03/2006 – 07/2010 | 53 |
| GAMA 08/2010 – 12/2024 | 173 |
| **TOTAL** | **410 meses** |

> ### CENÁRIO CONSERVADOR: **34 anos e 2 meses** (410 meses)
> Excedente sobre o mínimo de 30 anos: **+4 anos e 2 meses**

### 3.2 Cenário COMPLETO — CNIS + CTPS

Acrescenta o mês de 02/1988 (+1) e o vínculo DELTA (+6).

| Período | Meses |
|---|---|
| ALFA 02/1988 – 12/1995 (CTPS) | 95 |
| BETA 01/1998 – 06/2005 | 90 |
| DELTA 07/2005 – 12/2005 (CTPS) | 6 |
| Autônoma 03/2006 – 07/2010 | 53 |
| GAMA 08/2010 – 12/2024 | 173 |
| **TOTAL** | **417 meses** |

> ### CENÁRIO COMPLETO: **34 anos e 9 meses** (417 meses)
> Excedente sobre o mínimo de 30 anos: **+4 anos e 9 meses**

**Observação temporal relevante:** como o último vínculo cessou em 12/2024 e não há
contribuições posteriores documentadas, **o tempo apurado é idêntico na DER (15/08/2025) e
hoje (19/09/2026)**. A segurada **não ganha tempo de contribuição** com a passagem do
tempo — apenas idade.

### 3.3 Aferição da plausibilidade da contagem do INSS (28a 4m 12d)

**A contagem administrativa não é plausível** diante dos vínculos registrados no próprio
CNIS:

| Contagem | Total | Diferença para a contagem do INSS |
|---|---|---|
| **INSS (28a 4m 12d)** | 340 meses + 12 dias | — |
| Cenário conservador (só CNIS) | 410 meses | **70 meses (5a 10m) a mais** |
| Cenário completo | 417 meses | **77 meses (6a 5m) a mais** |

**Hipótese principal de reconciliação.** A exclusão do período de contribuinte individual
(03/2006 a 07/2010 = 53 meses) explica **a maior parte** do déficit. Subtraído do cenário
conservador: 410 − 53 = **357 meses = 29 anos e 9 meses** — valor que ficaria **logo
abaixo** do patamar de 30 anos, o que é **consistente com a redação do indeferimento**
("inferiores aos 30 anos exigidos"). Restariam, ainda assim, **cerca de 17 meses não
explicados**.

**Hipóteses para os 17 meses residuais** (a investigar, não afirmadas):
- meses sem salário-de-contribuição informado dentro dos vínculos celetistas;
- desconsideração parcial do vínculo ALFA, anterior à informatização do CNIS;
- datas exatas (dia/mês/ano) distintas das presumidas nesta triagem;
- indicadores de pendência no CNIS analítico que glosem competências isoladas.

**Conclusão parcial.** Há **forte indício** de que o INSS não computou o período de carnês,
embora ele conste do CNIS — e essa é a tese central do caso. Contudo, **a reconciliação
completa exige a cópia integral do processo administrativo NB 123.456.789-0**, com a
contagem analítica utilizada pela autarquia (diligência 9.2). Este relatório **não afirma**
qual foi o critério efetivamente adotado pelo INSS: afirma apenas a **incompatibilidade
aritmética** entre a decisão e o CNIS juntado.

---

## 4. Carência

*(Seção correspondente à rubrica "Carência" da Lei 8.213/1991 — INDICE.md, item 4. O
título originalmente solicitado continha os números dos artigos, suprimidos conforme a
Nota Metodológica.)*

A carência da aposentadoria por tempo de contribuição é de **180 contribuições mensais**
`[DISPOSITIVO A CONFIRMAR NA BASE — o INDICE.md refere a rubrica "Carência" da Lei
8.213/1991 sem texto integral; o número de 180 contribuições não está transcrito na base]`.

| Cenário | Contribuições apuradas | Carência exigida | Situação |
|---|---|---|---|
| Conservador | 410 | 180 | **CUMPRIDA** — folga de 230 contribuições |
| Completo | 417 | 180 | **CUMPRIDA** — folga de 237 contribuições |
| *Contagem do próprio INSS* | *340* | *180* | *Também cumprida* |

**A carência não é ponto controvertido neste caso.** Mesmo a contagem restritiva do INSS a
supera com folga — e, com efeito, o indeferimento **não a invocou**: fundou-se
exclusivamente em tempo de contribuição.

**Filiação anterior a 24/07/1991.** A segurada filiou-se ao RGPS em 1988. Para segurados
filiados antes da vigência da Lei 8.213/1991 existe regra de transição de carência em
tabela progressiva `[DISPOSITIVO A CONFIRMAR NA BASE — não consta do INDICE.md]`. A
observação é **irrelevante no resultado prático**, pois a carência está amplamente
cumprida em qualquer leitura.

**Período de graça** (Lei 8.213/1991 — rubrica *"Período de graça"*, INDICE.md item 4): a
qualidade de segurado após 12/2024 deve ser verificada, mas **não condiciona** a
aposentadoria por tempo de contribuição quando os requisitos já foram implementados
`[DISPOSITIVO A CONFIRMAR NA BASE — regra do direito adquirido]`.

---

## 5. Enquadramento em cada regra de transição da EC 103/2019

### 5.0 Premissa comum — tempo de contribuição em 13/11/2019

As regras de pedágio tomam por referência o tempo existente na data de entrada em vigor da
EC 103/2019. Contagem até **13/11/2019** (meses completos até 10/2019, mais 13 dias):

| Cenário | Composição | Total em 13/11/2019 | Faltava para 30 anos |
|---|---|---|---|
| Conservador | 94 + 90 + 53 + 111 (GAMA até 10/2019) | **348 meses = 29a 0m** (+13 d) | **~12 meses** |
| Completo | 95 + 90 + 6 + 53 + 111 | **355 meses = 29a 7m** (+13 d) | **~5 meses** |

Tempo mínimo da mulher: **30 anos** (INDICE.md, item 2 — EC 103/2019).

**Fato decisivo:** a segurada manteve vínculo **ininterrupto** na MODAS GAMA de 08/2010 a
**12/2024**, ou seja, contribuiu continuamente por **mais de 5 anos após 13/11/2019**.
Esse fato, isoladamente, satisfaz com enorme folga qualquer pedágio exigível.

---

### 5.1 PEDÁGIO 50% — **ENQUADRA** (nos dois cenários)

**Requisitos** (INDICE.md, item 2): *"contribuir pelo tempo que faltava + 50%. Sem idade
mínima"*. O acesso pressupõe que, em 13/11/2019, faltassem **2 anos ou menos** para o
tempo mínimo `[DISPOSITIVO A CONFIRMAR NA BASE — o requisito dos "2 anos ou menos" não
está transcrito no INDICE.md]`.

**(a) Porta de entrada (faltar ≤ 2 anos em 13/11/2019):**
- Conservador: faltavam ~12 meses → **≤ 2 anos → CUMPRIDO**
- Completo: faltavam ~5 meses → **≤ 2 anos → CUMPRIDO**

**(b) Cumprimento do pedágio:**

| Cenário | Faltava | Pedágio (50%) | Total a cumprir após 13/11/2019 | Data estimada de cumprimento |
|---|---|---|---|---|
| Conservador | ~12 meses | ~6 meses | **~18 meses** | **~maio/2021** |
| Completo | ~5 meses | ~2,5 meses | **~7,5 meses** | **~julho/2020** |

**(c) Idade mínima:** **não há** (INDICE.md, item 2). Isto **remove o único requisito
etário que a segurada não atende**.

> **CONCLUSÃO: ENQUADRA nos dois cenários. Requisito integralmente implementado já na DER
> de 15/08/2025** — e, na verdade, desde 2020/2021.

**Atenção ao valor:** esta regra é tradicionalmente associada ao cálculo pelo **fator
previdenciário**, e não à fórmula de 60% + 2% `[DISPOSITIVO A CONFIRMAR NA BASE — o
INDICE.md registra apenas "Cálculo RMI: 60% da média + 2% por ano acima de 20/15 anos",
sem disciplinar o cálculo de cada regra de transição]`. Com 57 anos na DER, o fator tende
a ser **redutor**. Isso **não afeta a viabilidade** (direito ao benefício), mas **afeta o
valor** — daí a recomendação de simulação comparativa (item 10.4).

---

### 5.2 PEDÁGIO 100% — **ENQUADRA** (nos dois cenários) — *regra preferencial*

**Requisitos** (INDICE.md, item 2): *"dobrar o tempo que faltava. Idade mínima: 57 M /
60 H"*, mais o tempo mínimo de 30 anos.

**(a) Idade mínima de 57 anos (mulher):**
- Completou 57 anos em **12/05/2025**;
- Na DER (15/08/2025): **57 anos, 3 meses e 3 dias** → **CUMPRIDO** (margem de 3 meses);
- Hoje (19/09/2026): 58 anos, 4 meses e 7 dias → **CUMPRIDO**.

**(b) Pedágio — dobro do tempo faltante em 13/11/2019:**

| Cenário | Faltava | Dobro | Data estimada de cumprimento |
|---|---|---|---|
| Conservador | ~12 meses | **~24 meses** | **~novembro/2021** |
| Completo | ~5 meses | **~10 meses** | **~setembro/2020** |

Cumprido com larga folga pelo vínculo GAMA, que seguiu até 12/2024.

**(c) Tempo mínimo de 30 anos:** 34a 2m (conservador) / 34a 9m (completo) → **CUMPRIDO**.

> **CONCLUSÃO: ENQUADRA integralmente nos dois cenários, já na DER de 15/08/2025.**

Esta regra é usualmente a mais vantajosa em valor, por conduzir a **100% da média dos
salários-de-contribuição**, sem incidência do fator previdenciário `[DISPOSITIVO A
CONFIRMAR NA BASE]`. **É a regra candidata preferencial**, sujeita a confirmação pelo
agente `calculo-previdenciario`.

---

### 5.3 SISTEMA DE PONTOS (93 pontos M em 2026) — **NÃO ENQUADRA no cenário conservador; enquadra por margem mínima no cenário completo**

**Requisitos** (INDICE.md, item 2): *"Pontos: 93 pontos M / 103 pontos H + tempo mínimo
(30 M / 35 H)"*. Pontuação = idade + tempo de contribuição.

| Cenário | Data | Idade | Tempo | Soma (anos) | Pontos | Exigido | Situação |
|---|---|---|---|---|---|---|---|
| Conservador | DER 15/08/2025 | 57a 3m | 34a 2m | 91,42 | **91** | 92 (2025) `[A CONFIRMAR]` | **NÃO** |
| Completo | DER 15/08/2025 | 57a 3m | 34a 9m | 92,00 | **92** | 92 (2025) `[A CONFIRMAR]` | Limítrofe |
| Conservador | Hoje 19/09/2026 | 58a 4m | 34a 2m | 92,50 | **92** | **93** | **NÃO — falta 1 ponto** |
| Completo | Hoje 19/09/2026 | 58a 4m | 34a 9m | 93,08 | **93** | **93** | **SIM — por ~1 mês de margem** |

*O INDICE.md fixa apenas a pontuação de **2026 (93 M)**. As exigências de 2025 e dos anos
seguintes `[DISPOSITIVO A CONFIRMAR NA BASE — tabela progressiva de pontos da
EC 103/2019]`.*

**Três alertas sobre esta regra:**

1. **O tempo mínimo de 30 anos está cumprido** — o obstáculo é **exclusivamente** a
   pontuação.
2. **A diferença entre "não enquadra" e "enquadra" é exatamente o resultado das
   Divergências 1 e 2** (1 mês + 6 meses = 7 meses de CTPS não registrados no CNIS). Ou
   seja: esta regra **depende inteiramente** do reconhecimento dos períodos de CTPS
   ausentes do CNIS, com margem de **aproximadamente um mês**. É base **frágil** para
   sustentar o pedido principal.
3. **A segurada não consegue "esperar" para alcançar os pontos.** Tendo cessado de
   contribuir em 12/2024, seu tempo está congelado; a idade cresce 12 meses por ano, mas
   a exigência de pontos também sobe 1 ponto por ano `[A CONFIRMAR]` — **o saldo é nulo**.
   **Sem voltar a contribuir, a pontuação não evolui em relação à exigência.** Constatação
   relevante para o aconselhamento da cliente.

> **CONCLUSÃO: regra NÃO recomendada como fundamento principal. Cabe, no máximo, como
> pedido sucessivo.**

---

### 5.4 IDADE MÍNIMA PROGRESSIVA (59 anos e 6 meses M em 2026) — **NÃO ENQUADRA**

**Requisitos** (INDICE.md, item 2): *"Idade mínima progressiva: 59 anos e 6 meses M /
64 anos e 6 meses H"*, mais o tempo mínimo de 30 anos.

| Data | Idade da segurada | Idade exigida | Diferença | Situação |
|---|---|---|---|---|
| DER 15/08/2025 | 57a 3m 3d | 59a (2025) `[A CONFIRMAR]` | faltavam ~1a 9m | **NÃO ENQUADRA** |
| Hoje 19/09/2026 | 58a 4m 7d | **59a 6m (2026)** | **faltam 1a 1m 23d** | **NÃO ENQUADRA** |

O tempo de contribuição (34a 2m) está cumprido; **falta apenas idade**. A segurada
completará 59 anos e 6 meses em **12/11/2027** — mas nessa data a exigência já terá subido
`[A CONFIRMAR — tabela progressiva não consta da base]`. Como a idade mínima sobe ~6 meses
por ano e a segurada envelhece 12 meses por ano, ela **alcança** a regra, porém apenas
alguns anos adiante.

> **CONCLUSÃO: é a regra MENOS favorável. Deve ser descartada como fundamento.**

---

### 5.5 Síntese do enquadramento

| Regra de transição EC 103/2019 | Cenário conservador (só CNIS) | Cenário completo (CNIS+CTPS) | Já cumprida na DER 15/08/2025? |
|---|---|---|---|
| **Pedágio 50%** (sem idade mínima) | **ENQUADRA** | **ENQUADRA** | **SIM** |
| **Pedágio 100%** (idade 57 M) | **ENQUADRA** | **ENQUADRA** | **SIM** |
| Pontos (93 M em 2026) | **NÃO** (92 pontos) | Enquadra por ~1 mês | Duvidoso |
| Idade mínima progressiva (59a 6m M) | **NÃO** | **NÃO** | **NÃO** |

> **ACHADO CENTRAL.** A segurada enquadra-se em **duas** regras de transição **mesmo na
> leitura mais restritiva possível — usando apenas o CNIS, sem qualquer período
> controvertido de CTPS**. O direito, portanto, **não depende** do reconhecimento do
> vínculo DELTA nem do ajuste de 02/1988: esses períodos **melhoram** o caso, mas **não
> são condição** para ele.

---

## 6. CLASSIFICAÇÃO DE VIABILIDADE

> # VIABILIDADE: **ALTA**
> *(condicionada às diligências 9.1 a 9.3 — ver ressalva ao final desta seção)*

**Justificativa fundamentada:**

1. **O requisito de tempo está cumprido com folga superior a 4 anos no cenário mais
   conservador.** 34 anos e 2 meses apurados **exclusivamente a partir do CNIS**, contra os
   30 anos exigidos (EC 103/2019 — INDICE.md, item 2). Não é preciso provar nada além do
   que a própria autarquia já registra.

2. **Há enquadramento em duas regras de transição autônomas** — pedágio 50% e pedágio 100%
   da EC 103/2019 (INDICE.md, item 2) — **ambas já implementadas na DER de 15/08/2025**. A
   existência de dois fundamentos independentes reduz substancialmente o risco de
   insucesso.

3. **O pedágio 50% dispensa idade mínima** (INDICE.md, item 2), o que **elimina o único
   requisito que a segurada não atende** (a idade de 59a 6m da regra progressiva).

4. **A carência está amplamente cumprida** — 410 contribuições no cenário conservador
   contra 180 exigidas (Lei 8.213/1991, rubrica *"Carência"* — INDICE.md, item 4) — e
   sequer foi controvertida pelo INSS.

5. **O fundamento do indeferimento é aritmeticamente insustentável.** A contagem de
   28a 4m 12d é **70 meses inferior** ao que o próprio CNIS registra, diferença explicada
   majoritariamente pela não-consideração de período **expressamente lançado no CNIS**. Um
   erro dessa magnitude, documentalmente demonstrável, é o cenário mais favorável possível
   para reversão.

6. **O benefício é de contagem objetiva.** Aposentadoria por tempo de contribuição
   (Constituição Federal e Lei 8.213/1991, rubricas próprias — INDICE.md, itens 1 e 4) não
   depende de perícia médica, de avaliação de incapacidade nem de prova testemunhal
   essencial. A prova é documental e pré-constituída.

**RESSALVA À CLASSIFICAÇÃO.** A contagem do INSS pode apoiar-se em informação não visível
no CNIS **sintético** analisado (p. ex., ausência de salários-de-contribuição em
competências isoladas, ou carnês recolhidos em atraso e não validados). Por isso a
classificação ALTA é emitida **condicionada** à obtenção do processo administrativo e do
CNIS analítico. Confirmada a integridade dos 410 meses, a viabilidade é **ALTA com elevado
grau de segurança**. Caso o período de carnês venha a ser invalidado, o tempo cai para
~29a 9m e **o caso muda de figura** — ver risco 8.3.

---

## 7. Pontos fortes

1. **Margem de tempo confortável:** +4a 2m sobre o mínimo no cenário conservador; +4a 9m no
   completo. **O caso não é limítrofe quanto ao tempo.**
2. **Duas regras de transição disponíveis** (pedágio 50% e pedágio 100%), permitindo pedido
   principal e sucessivo, e escolha pela mais vantajosa em valor.
3. **Requisitos já implementados na DER original (15/08/2025)**, o que sustenta pedido de
   **DIB na DER**, com retroativo superior a 13 meses até a presente data.
4. **Trajetória contributiva coerente e verificável:** mesma profissão (costureira) em
   todos os vínculos, empregadores identificados por CNPJ, sem sobreposições, sem indício
   de vínculo fictício.
5. **Vínculo longo e ininterrupto de 14a 5m na MODAS GAMA (08/2010 a 12/2024)**,
   integralmente registrado em CNIS **e** CTPS — é ele que satisfaz, com enorme sobra,
   ambos os pedágios.
6. **Erro administrativo aritmético e demonstrável**, não mera divergência de interpretação
   jurídica.
7. **Idade de 57 anos já atingida na DER** (em 12/05/2025), satisfazendo o requisito etário
   do pedágio 100% com 3 meses de antecedência sobre o requerimento.
8. **Prova documental pré-constituída** (CNIS + CTPS), dispensando instrução complexa.
9. **Nenhuma parcela prescrita no momento**, dada a proximidade temporal da DER (item 8.9).
10. **A biometria obrigatória não incide sobre o NB originário** (item 8.7).

---

## 8. Riscos e pontos de atenção

### 8.1 RISCO ALTO — Perda do prazo recursal administrativo

A decisão é de **20/11/2025**; hoje é **19/09/2026** — cerca de **10 meses depois**. O
prazo do recurso ordinário ao CRPS é de **30 dias** `[DISPOSITIVO A CONFIRMAR NA BASE — o
prazo recursal não consta do INDICE.md; a matéria situa-se no Decreto 3.048/1999 e no
Regimento Interno do CRPS, cujos textos não estão populados]`, contado da **ciência** da
decisão. **O prazo está amplamente superado**, operando-se a preclusão administrativa.

**Ressalva determinante:** o prazo corre da **ciência**, não da data da decisão. A data em
que a segurada foi efetivamente cientificada **não consta dos autos analisados** — a carta
informa apenas a data da decisão. Se a diligência 9.2 revelar ciência tardia ou ausência de
notificação válida, **a via recursal se reabre**. **Verificar antes de descartá-la.**

### 8.2 RISCO MÉDIO — Reconciliação incompleta dos 17 meses residuais

A hipótese do não-cômputo dos carnês explica 53 dos 70 meses de diferença. Os ~17 meses
restantes **não estão explicados** e podem revelar lacunas reais de recolhimento dentro dos
vínculos celetistas. Isso **não compromete** o enquadramento (a folga é de 50 meses sobre o
mínimo), mas deve ser esclarecido antes do ajuizamento, para evitar surpresa em
contestação.

### 8.3 RISCO MÉDIO-ALTO — Validação dos carnês de contribuinte individual (03/2006 – 07/2010)

**É o risco mais relevante do caso.** Ainda que o período conste do CNIS, o INSS
aparentemente não o computou. Causas possíveis a investigar: (i) recolhimentos **em
atraso**, sujeitos a regra própria de aproveitamento; (ii) recolhimento em **código ou
alíquota** que não gera direito à aposentadoria por tempo de contribuição (p. ex., plano
simplificado, com necessidade de complementação); (iii) **indicadores de irregularidade**
no CNIS analítico `[DISPOSITIVO A CONFIRMAR NA BASE]`.

**Se este período não for validado**, o tempo cai para **~29 anos e 9 meses** — abaixo do
mínimo de 30 anos — e **todas as quatro regras de transição ficam inacessíveis**. As
guias/carnês originais são a **diligência número 1**.

### 8.4 RISCO MÉDIO — Vínculo CONFECÇÕES DELTA ME ausente do CNIS

Ausente do CNIS, o vínculo depende da anotação em CTPS e de prova complementar. Sendo
empregada celetista, a segurada não responde pela omissão do empregador `[DISPOSITIVO A
CONFIRMAR NA BASE]`, e a anotação em CTPS goza de presunção de veracidade `[JURISPRUDÊNCIA
A CONFIRMAR — base vazia; nenhum número indicado]`. Empresa provavelmente baixada, o que
dificulta a prova. **Impacto limitado** (6 meses), **exceto para a regra de pontos**.

### 8.5 RISCO MÉDIO — Escolha da regra e impacto no valor do benefício

A viabilidade é alta, mas **o valor varia significativamente** conforme a regra eleita:

| Regra | Cálculo esperado | Observação |
|---|---|---|
| Pedágio 100% | ~100% da média | `[A CONFIRMAR NA BASE]` — tende a ser a mais vantajosa |
| Pedágio 50% | Média × fator previdenciário | `[A CONFIRMAR]` — fator tende a ser **redutor** aos 57 anos |
| Fórmula geral do INDICE.md | 60% + 2% × (34 − 15) = **98% da média** | INDICE.md, item 2 |

Teto previdenciário vigente: **R$ 8.475,55** (Portaria Interministerial MPS/MF 13/2026 —
INDICE.md, item 7). **Recomenda-se simulação comparativa** antes de definir o pedido
principal.

### 8.6 RISCO BAIXO-MÉDIO — Datas exatas (dia) indisponíveis

Toda a contagem foi feita em meses civis. As datas exatas podem alterar o resultado em
alguns dias por vínculo. **Irrelevante para os pedágios** (folga de anos); **relevante para
a regra de pontos**, cuja margem é de aproximadamente um mês.

### 8.7 PONTO DE ATENÇÃO — Cadastro biométrico (Portaria DIRBEN/INSS 1.347/2026)

Conforme INDICE.md, item 7, a portaria impõe cadastro biométrico obrigatório para
**benefícios requeridos a partir de 21/11/2025**, com prazo de **30 dias** para
regularização.

| Situação | Incide? | Fundamento |
|---|---|---|
| **NB 123.456.789-0 (DER 15/08/2025)** | **NÃO** | Requerimento **anterior** a 21/11/2025 — e note-se que a própria decisão, de 20/11/2025, é de **um dia antes** do marco |
| **Novo requerimento protocolado hoje** | **SIM** | Data posterior a 21/11/2025 |
| Isenção por idade (80+) | **NÃO se aplica** | A segurada tem 58 anos |
| Isenção por área de difícil acesso | A verificar | Sem informação nos autos |
| Exceção por espécie de benefício | **NÃO se aplica** | As exceções do INDICE.md (auxílio-doença, auxílio-acidente, pensão por morte, salário-maternidade, aposentadoria por incapacidade permanente) **não incluem** a aposentadoria por tempo de contribuição |

**Consequência prática:** optando-se por novo requerimento, a cliente deve ser orientada a
**realizar a biometria previamente, ou dentro de 30 dias**, sob pena de sobrestamento
(diligência 9.11).

### 8.8 PONTO DE ATENÇÃO — Vedação de novo requerimento com processo em curso

A IN PRES/INSS 128/2022 contém dispositivo que **veda novo requerimento enquanto houver
processo em curso**; a IN PRES/INSS 208/2026 afastou a aplicação automática dessa vedação
**para benefícios por incapacidade** (INDICE.md, item 6) `[NÚMERO DO DISPOSITIVO A
CONFIRMAR NA BASE — o texto integral da IN 128/2022 não está populado; ver INDICE.md,
"Pendências desta base", item 2]`.

Como (i) o benefício pretendido **não é por incapacidade** e (ii) o processo administrativo
foi **concluído** por indeferimento, a vedação **provavelmente não incide**. Ainda assim,
**confirmar antes de protocolar** novo requerimento, sobretudo se houver algum recurso ou
pedido pendente não informado pela cliente.

### 8.9 PONTO DE ATENÇÃO — Prescrição quinquenal

*(Lei 8.213/1991 — rubrica "Prescrição quinquenal", INDICE.md, item 4.)*

DER em **15/08/2025**. Eventual ação ajuizada ainda em 2026 estará a **menos de 5 anos** da
DER: **não há parcelas prescritas neste momento**. O risco é **futuro e progressivo** — a
cada mês de inércia aproxima-se o marco quinquenal, que se completaria em **15/08/2030**.

Há ainda prazo **decadencial decenal** para revisão `[DISPOSITIVO A CONFIRMAR NA BASE — o
INDICE.md associa a rubrica apenas à "Prescrição quinquenal", sem mencionar decadência]`.

### 8.10 PONTO DE ATENÇÃO — Ausência de contribuições após 12/2024

Sem contribuição desde 01/2025 (~20 meses). Consequências: (i) **a pontuação não evolui**
(item 5.3); (ii) a qualidade de segurado pode ter-se perdido após o período de graça — o
que é **irrelevante** se os requisitos já estavam implementados, mas deve ser consignado na
inicial. Se a cliente estiver exercendo atividade informal, avaliar recolhimentos que
fortaleçam o caso.

---

## 9. Lacunas documentais e diligências necessárias

**Lista acionável — a solicitar à cliente e aos órgãos.**

### PRIORIDADE MÁXIMA

**9.1 — Carnês / guias (GPS) do período 03/2006 a 07/2010.**
Solicitar à cliente **todas** as guias originais ou comprovantes bancários dos 53 meses. É
a prova que sustenta o núcleo do caso (risco 8.3). Verificar em cada guia: **código de
recolhimento, alíquota, competência, data de vencimento e data efetiva de pagamento**
(para identificar recolhimentos em atraso).

**9.2 — Cópia integral do processo administrativo NB 123.456.789-0.**
Obter via Meu INSS ou por requerimento formal. Deve conter: **contagem analítica de tempo
de contribuição** utilizada pelo INSS, despacho fundamentado e — **essencial** —
**comprovante de ciência da decisão pela segurada, com data**. Este documento (i)
reconcilia os 17 meses residuais (risco 8.2) e (ii) **define se o prazo recursal está de
fato precluso** (risco 8.1).

**9.3 — CNIS analítico completo (extrato com salários-de-contribuição mês a mês).**
O CNIS dos autos é **sintético** (apenas admissão/demissão). O analítico é indispensável
para: datas exatas, identificação de competências sem recolhimento, **indicadores de
pendência** e apuração dos salários-de-contribuição para cálculo da RMI.

### PRIORIDADE ALTA

**9.4 — CTPS original — cópia integral e legível.**
Todas as páginas de contrato de trabalho, **inclusive alterações salariais, férias e
anotações gerais**, com foco nas **datas exatas (dia/mês/ano)**, especialmente ALFA
(02 ou 03/1988?) e DELTA.

**9.5 — Prova complementar do vínculo CONFECÇÕES DELTA ME (07/2005 a 12/2005).**
Colher o que a cliente possua: holerites/contracheques, termo de rescisão (TRCT), extratos
e comprovantes de saque de FGTS, vale-transporte, crachá, fotos, e **nomes e contatos de
colegas de trabalho** (para eventual prova testemunhal). Consultar a situação cadastral do
CNPJ **55.666.777/0001-88** na Receita Federal.

**9.6 — Extrato completo de FGTS (todas as contas vinculadas).**
Prova robusta e **independente do CNIS** para os vínculos celetistas — útil para ALFA,
DELTA e para reconciliar os 17 meses residuais.

### PRIORIDADE MÉDIA

**9.7 — Esclarecimento sobre o hiato 01/1996 – 12/1997 (24 meses).**
Entrevistar a cliente: houve trabalho não registrado? Vínculo não anotado? Recolhimento
como facultativa? Havendo prova de atividade, **adiciona até 2 anos** e resolve
definitivamente a regra de pontos.

**9.8 — Esclarecimento sobre o hiato 01/2025 até a presente data.**
Verificar se há atividade em curso, recolhimentos não lançados, e se interessa retomar
contribuições (item 8.10).

**9.9 — Documentos pessoais atualizados.**
RG, CPF, comprovante de residência, certidão de nascimento/casamento — para conferência de
nome e data de nascimento (divergência de nome é causa frequente de glosa no CNIS).

**9.10 — Declaração sobre outros vínculos, rurais ou especiais.**
Confirmar com a cliente se houve trabalho rural, atividade insalubre (a função de costureira
pode envolver exposição a ruído e agentes químicos) ou vínculo em outro regime (RPPS), para
avaliar aposentadoria especial ou contagem recíproca (INDICE.md, item 1 — rubricas
"Aposentadoria especial" e "Contagem recíproca"). **Não há indício nos autos; investigar
por completude.**

**9.11 — Situação do cadastro biométrico.**
Verificar se a cliente já possui biometria válida (TSE ou INSS), em vista do item 8.7,
**antes** de eventual novo requerimento.

**9.12 — Populamento da base legislativa do escritório.**
Diligência **interna**, não do cliente, mas **bloqueante** para a redação das peças: os
textos integrais das normas devem ser carregados em `legislacao/` (ver Nota Metodológica e
item 12).

---

## 10. Recomendação de próximo passo

### 10.1 Via 1 — Recurso ao CRPS: **INVIÁVEL, salvo comprovação de ciência tardia**

Decisão em 20/11/2025; hoje, 19/09/2026 — **cerca de 10 meses**. Sendo de 30 dias o prazo
do recurso ordinário `[DISPOSITIVO A CONFIRMAR NA BASE]`, contado da ciência, o prazo está
superado e houve **preclusão administrativa**. **Não se recomenda como via principal.**

**Ressalva obrigatória:** o prazo corre da **ciência**. Se a diligência 9.2 revelar que a
segurada foi cientificada tardiamente, ou que a notificação foi inválida, **a via recursal
se reabre** e passa a ser a mais rápida e econômica. **Verificar antes de descartar.**

### 10.2 Via 2 — Novo requerimento administrativo (nova DER): **OPÇÃO SECUNDÁRIA / PARALELA**

**Vantagens:** rápido, sem custo, e os requisitos **estão implementados** — há chance real
de concessão administrativa, sobretudo instruindo o pedido com os carnês (9.1) e invocando
expressamente o **pedágio 100%**.

**Desvantagem decisiva:** a **DIB seria fixada na nova DER**, e não em 15/08/2025 —
**sacrificando mais de 13 meses de retroativo**, montante que tende a superar dez salários
de benefício.

**Condicionantes:** (i) **biometria obrigatória** — Portaria DIRBEN/INSS 1.347/2026, prazo
de 30 dias (item 8.7); (ii) confirmar a não-incidência da vedação de novo requerimento da
IN PRES/INSS 128/2022 (item 8.8).

### 10.3 Via 3 — Ação judicial de concessão com DIB em 15/08/2025: **RECOMENDADA COMO VIA PRINCIPAL**

**Fundamentos a invocar** (números a confirmar — item 12):
- Constituição Federal — aposentadoria por tempo de contribuição (INDICE.md, item 1);
- Lei 8.213/1991 — rubrica *"Aposentadoria por tempo de contribuição"* (INDICE.md, item 4);
- EC 103/2019 — **pedágio 100%** como fundamento principal e **pedágio 50%** como
  sucessivo (INDICE.md, item 2);
- Lei 8.213/1991 — rubrica *"Carência"* (INDICE.md, item 4): requisito cumprido;
- Lei 8.213/1991 — rubrica *"Prescrição quinquenal"* (INDICE.md, item 4): nenhuma parcela
  prescrita.

**Pedidos sugeridos (a critério do advogado responsável):**
1. Reconhecimento e cômputo do período de **contribuinte individual de 03/2006 a 07/2010**
   (53 meses), já constante do CNIS e não computado administrativamente;
2. Reconhecimento do vínculo **CONFECÇÕES DELTA ME, 07/2005 a 12/2005** (6 meses), anotado
   em CTPS e ausente do CNIS;
3. Retificação da data de admissão em **CONFECÇÕES ALFA para 02/1988** (1 mês);
4. Concessão da aposentadoria por tempo de contribuição pela regra do **pedágio 100%**;
   sucessivamente pelo **pedágio 50%**; sucessivamente pela regra de **pontos**;
5. **DIB em 15/08/2025** (DER originária), com pagamento das parcelas vencidas, corrigidas
   `[CRITÉRIOS DE CORREÇÃO MONETÁRIA E JUROS A CONFIRMAR NA BASE]`;
6. Tutela de urgência para implantação imediata, se a situação socioeconômica da cliente a
   justificar (a avaliar).

**Por que a via judicial é preferível:**
1. **Preserva a DIB em 15/08/2025**, com retroativo já superior a 13 meses e crescente — é
   a **única via** que recupera esse valor;
2. **Sem risco prescricional atual**, mas com perda potencial em caso de inércia (item 8.9);
3. **Prova pré-constituída** (CNIS + CTPS + carnês), instrução simples;
4. **O erro do INSS é aritmético e demonstrável**, não interpretativo;
5. **Dois fundamentos autônomos de enquadramento** já na DER, o que amplia as chances;
6. **Dispensa nova biometria** quanto ao NB originário (item 8.7).

### 10.4 Estratégia recomendada (a submeter ao advogado responsável)

| # | Ação | Responsável |
|---|---|---|
| 1 | Executar **imediatamente** as diligências **9.1, 9.2 e 9.3** | Escritório / cliente |
| 2 | Ao receber o processo administrativo, **verificar a data de ciência**. Havendo qualquer margem recursal, protocolar **recurso ao CRPS** de imediato | Agente `recurso-crps` |
| 3 | Sendo confirmada a preclusão (cenário esperado), ajuizar **ação de concessão com DIB em 15/08/2025** | Agente `redacao-peticao` |
| 4 | Antes de definir o pedido principal, obter **contagem definitiva com datas exatas** e **simulação comparativa de RMI** entre pedágio 100% e pedágio 50% | Agente `calculo-previdenciario` |
| 5 | Diagnóstico aprofundado da negativa administrativa | Agente `analise-indeferimento` |
| 6 | **Popular a base legislativa** antes da redação de qualquer peça | Escritório (item 9.12) |
| 7 | **Decisão a tomar com a cliente:** novo requerimento em paralelo (recebimento mais rápido, com perda do retroativo) *vs.* aguardar apenas o resultado judicial (mais demorado, retroativo integral). Decisão do advogado, **com ciência expressa da cliente quanto ao trade-off** | Advogado responsável |

---

## 11. Observações finais sobre os limites desta análise

1. Toda a contagem baseia-se em documentos que registram apenas **mês/ano**; os resultados
   são aproximações de triagem, sujeitas a ajuste em dias.
2. A base legislativa local **não contém os textos integrais das normas**; as referências
   limitam-se às rubricas do `INDICE.md`, com os números de artigo suprimidos e listados no
   item 12 para conferência manual.
3. **Nenhum número de súmula, tema repetitivo ou artigo foi inferido ou criado.**
4. **Nenhum período de contribuição foi presumido:** todos decorrem exclusivamente do CNIS
   ou da CTPS juntados.
5. Não há documentação médica no caso e **nenhum diagnóstico é afirmado** — matéria
   inaplicável ao benefício pretendido.
6. A classificação **ALTA** está **condicionada** à confirmação, pelas diligências 9.1 a
   9.3, de que o período de contribuinte individual de 03/2006 a 07/2010 é efetivamente
   computável.

---

## 12. Dispositivos a confirmar antes do uso externo

Checklist para o advogado responsável. **Nenhum número abaixo foi verificado na base** —
todos devem ser conferidos em fonte oficial e inseridos manualmente nas peças.

| # | Norma | Rubrica no INDICE.md | Onde se aplica neste relatório |
|---|---|---|---|
| 1 | Constituição Federal | Aposentadoria por tempo de contribuição | Itens 1, 6, 10.3 |
| 2 | Constituição Federal | Contagem recíproca | Item 9.10 |
| 3 | Lei 8.213/1991 | Aposentadoria por tempo de contribuição | Itens 1, 6, 10.3 |
| 4 | Lei 8.213/1991 | Carência (nº de 180 contribuições) | Itens 4, 6 |
| 5 | Lei 8.213/1991 | Período de graça | Item 4 |
| 6 | Lei 8.213/1991 | Prescrição quinquenal | Itens 8.9, 10.3 |
| 7 | Lei 8.213/1991 | Regra de transição de carência (filiados antes de 24/07/1991) — **não consta do INDICE.md** | Item 4 |
| 8 | Lei 8.212/1991 | Contribuições e arrecadação (responsabilidade do empregador) | Itens 2.2, 8.4 |
| 9 | EC 103/2019 | Pedágio 50% — requisito de "faltar ≤ 2 anos" e forma de cálculo da RMI | Item 5.1 |
| 10 | EC 103/2019 | Pedágio 100% — forma de cálculo da RMI | Item 5.2 |
| 11 | EC 103/2019 | Tabela progressiva de pontos (2025 e anos seguintes) | Item 5.3 |
| 12 | EC 103/2019 | Tabela progressiva de idade mínima (2025 e anos seguintes) | Item 5.4 |
| 13 | Decreto 3.048/1999 e Regimento Interno do CRPS | Prazo de 30 dias para recurso ordinário | Itens 8.1, 10.1 |
| 14 | IN PRES/INSS 128/2022 | Vedação de novo requerimento com processo em curso | Item 8.8 |
| 15 | Jurisprudência | Valor probatório da anotação em CTPS | Itens 2.2, 8.4 |
| 16 | — | Critérios de correção monetária e juros | Item 10.3 |

---

**RASCUNHO — sujeito a revisão do advogado responsável.**
