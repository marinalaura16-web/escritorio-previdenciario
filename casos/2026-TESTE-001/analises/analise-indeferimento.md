# RASCUNHO — PARA REVISÃO DO ADVOGADO

# ANÁLISE DE INDEFERIMENTO — CASO 2026-TESTE-001

**Data da análise:** 15/10/2026
**Protocolo aplicado:** `analise-indeferimento` (`.claude/agents/analise-indeferimento.md`) +
skill `quebra-indeferimento` (`.claude/skills/quebra-indeferimento/SKILL.md`)
**Executado por:** `orquestrador-prev`, **diretamente** — o subagente `analise-indeferimento`
**não pôde ser acionado** nesta execução (a ferramenta de disparo de subagentes não estava
disponível no ambiente do orquestrador; ver `TESTE-ORQUESTRACAO-relatorio.md`, item (a)). O
protocolo do especialista foi seguido passo a passo, sem atalhos.
**Natureza:** RASCUNHO. Não é parecer definitivo. Nenhuma peça deve ser protocolada sem
revisão do advogado responsável.

---

## 0. Convenção de proveniência usada neste documento

| Marcação | Significado |
|---|---|
| `[FONTE OFICIAL — PDF DOU NA BASE]` | Texto conferido **nesta data** por extração mecânica de texto (`pdftotext`) do PDF oficial que está **dentro da base** — `legislacao/instrucoes-normativas/in-128-2022.pdf` (DOU de 29/03/2022, Seção 1) ou `legislacao/emendas-constitucionais/ec-103-2019-oficial.pdf` (Planalto). Maior grau de confiança disponível neste ambiente. |
| `[FONTE OFICIAL CONFIRMADA]` | Marcação já existente em `ec-103-2019.md` (reconciliação de 09/10/2026), aqui **reconferida** por extração mecânica do mesmo PDF. |
| `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` | Dispositivo presente nos resumos `.md` da base, montados por WebSearch, sem conferência byte a byte. |
| `[DISPOSITIVO A CONFIRMAR]` | Dispositivo **ausente da base** (ou presente sem conteúdo). Indicado apenas para orientar a pesquisa do advogado; **não usar em peça sem conferir**. |
| `[JURISPRUDÊNCIA A CONFIRMAR]` | Precedente não incorporado à base `jurisprudencia-vinculante/`. |

**Observação sobre a IN 128/2022:** o resumo `in-128-2022.md` da base registra o Livro IV
apenas por faixas ("fase recursal ... prazo de 30 dias (578-582)"). Os números de artigo
abaixo foram extraídos **do PDF integral**, que integra a base. O hook
`anti-alucinacao.py` só lê os resumos `.md`; por isso ele **não reconhece** como presentes
na base os arts. 547-602 da IN 128, embora estejam no PDF oficial (ver relatório de
orquestração, item (d)).

---

## 1. Documentos analisados

| Documento | Arquivo | Observação |
|---|---|---|
| Comunicação de decisão (carta de indeferimento) | `documentos/carta-indeferimento.txt` | NB 123.456.789-0; DER 15/08/2025; decisão 20/11/2025 |
| CNIS (sintético) | `documentos/cnis.txt` | 3 vínculos + contribuições como autônoma 03/2006-07/2010 "comprovadas por carnê" |
| CTPS | `documentos/ctps.txt` | 4 anotações; vínculo DELTA (07/2005-12/2005) com observação "Periodo NAO consta no CNIS" |
| Triagem anterior | `analises/triagem-viabilidade.md` (19/09/2026) | Contagem de 410 meses (conservador) / 417 meses (completo) — **reconferida nesta análise** (item 4) |

**Documento NÃO disponível:** cópia do processo administrativo NB 123.456.789-0 (contagem
analítica do INSS, despacho fundamentado, comprovante de ciência). A ausência desse
documento limita o diagnóstico (item 3.3) e é a diligência nº 1 (item 8).

---

## 2. Motivo formal (transcrição literal da carta)

> "DECISAO: INDEFERIDO
> Motivo: Nao foi comprovado o tempo minimo de contribuicao necessario. Conforme analise do
> CNIS, a segurada possui 28 anos, 4 meses e 12 dias de tempo de contribuicao, inferiores
> aos 30 anos exigidos."
> — `documentos/carta-indeferimento.txt`, linhas 7-9

**O que a carta (tal como transcrita nos autos do escritório) NÃO contém:**
1. nenhum dispositivo legal como fundamento;
2. nenhuma indicação de qual regra de transição da EC 103/2019 foi examinada;
3. nenhuma análise individualizada dos períodos (qual foi computado, qual foi glosado e por quê);
4. nenhuma indicação do **prazo para recurso**.

> Ressalva: o arquivo `.txt` pode ser transcrição parcial do documento original. Os itens
> acima devem ser conferidos contra a carta original e contra o processo administrativo
> antes de serem alegados.

---

## 3. Diagnóstico do motivo real

### 3.1 Erro de cálculo — contagem incompatível com o próprio CNIS citado pela decisão

A decisão diz basear-se na "analise do CNIS". O CNIS dos autos registra, **sem nenhuma
outra prova além dele próprio**, 410 meses (34a 2m) — item 4.

| Contagem | Meses | Diferença para o INSS |
|---|---|---|
| INSS (28a 4m 12d) | 340 (+12 dias) | — |
| Só o CNIS (`documentos/cnis.txt`, vínculos 01-03 + carnês) | 410 | **+70 meses** |
| CNIS + CTPS (`documentos/ctps.txt`, anotações 1 e 3) | 417 | **+77 meses** |

**Erro do INSS demonstrável por documento específico:** `documentos/cnis.txt`, linha
"Contribuicoes como autonoma: 03/2006 a 07/2010 (comprovadas por carne)" — 53 meses
lançados no próprio cadastro que a decisão diz ter analisado. Excluídos esses 53 meses, o
resultado seria 357 meses (29a 9m), abaixo dos 30 anos, o que é **coerente com a redação
do indeferimento** — por isso a hipótese principal é a **glosa do período de contribuinte
individual**.

### 3.2 Falta de análise / motivação insuficiente

A IN 128/2022 exige que a decisão contenha "fundamentação com análise das provas
constantes nos autos", sendo "insuficiente a mera justificativa do indeferimento constante
no sistema corporativo do INSS" (IN 128, art. 574, caput), que a motivação indique
"quais requisitos legais foram ou não atendidos" (§ 1º) e que todos os requisitos sejam
apreciados com "avaliação individualizada de cada requisito legal" (§ 2º). Exige ainda,
em requerimento que envolva CNIS divergente, a análise de "todos os pedidos relativos à
inclusão, alteração, ratificação ou exclusão das informações divergentes, extemporâneas ou
insuficientes" (§ 3º). `[FONTE OFICIAL — PDF DOU NA BASE]`

A carta dos autos traz uma única frase de motivação, sem dizer **qual período foi glosado
nem por quê**, e sem examinar regra de transição alguma. Também não há notícia de que o
INSS tenha emitido carta de exigência para o período de carnês ou para o vínculo DELTA.

Além disso, o INSS deveria, por ocasião da decisão, reconhecer o benefício mais vantajoso
e verificar a implementação posterior de requisitos para eventual reafirmação da DER (IN
128, art. 577, I e II) `[FONTE OFICIAL — PDF DOU NA BASE]`. Nada disso consta da carta.

### 3.3 Por que o INSS pode ter glosado os carnês — hipóteses com base na IN 128/2022

Todas as hipóteses abaixo são **a verificar** no CNIS analítico e nas guias; **nenhuma é
afirmada**:

| Hipótese | Norma (base) | Efeito se confirmada | Como verificar |
|---|---|---|---|
| (a) Recolhimentos **em atraso** | IN 128, art. 208, caput e § 1º: contribuição em atraso de contribuinte individual **pode** ser computada para tempo de contribuição "desde que o recolhimento seja anterior à data do fato gerador"; § 2º: presume-se regular o recolhimento em atraso constante do CNIS "sem indicador de pendências" `[FONTE OFICIAL — PDF DOU NA BASE]` | Se pagos antes da DER (15/08/2025) e sem indicador de pendência, **devem ser computados**. Se pagos após a DER, não contam para este NB (IN 128, art. 216, III) | Datas de pagamento nas guias; indicadores no CNIS analítico |
| (b) **Alíquota reduzida** (5% ou 11%, plano simplificado) | IN 128, art. 216, V, "a": não se computa para aposentadoria por tempo de contribuição o período de CI com alíquota de 5% ou 11%, "salvo se efetuar a complementação das contribuições para o percentual de 20%" `[FONTE OFICIAL — PDF DOU NA BASE]` | Glosa **legítima**, mas **sanável** por complementação. **Se esta hipótese se confirmar, a tese de "erro do INSS" enfraquece** e a via passa a ser complementação + novo pedido | Código de recolhimento nas guias (diligência 8.1) |
| (c) Salário de contribuição **abaixo do mínimo** | IN 128, art. 210: para períodos anteriores a 14/11/2019, o CI só tem computadas as competências com salário de contribuição igual ou superior ao mínimo, admitida complementação (parágrafo único) `[FONTE OFICIAL — PDF DOU NA BASE]` | Glosa parcial, sanável | CNIS analítico |
| (d) **Indicador de pendência** no CNIS | Decreto 3.048, arts. 19 e 19-B (dúvida sobre regularidade → documentos contemporâneos) `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` | Glosa até apresentação das guias | CNIS analítico |

**Observação sobre carência (não sobre tempo):** a IN 128, art. 191, só conta para
carência do CI a partir da "primeira contribuição em dia" `[FONTE OFICIAL — PDF DOU NA
BASE]`. É regra de **carência**, não de tempo de contribuição — e a carência está cumprida
com folga em qualquer cenário (item 4.3).

### 3.4 Os 17 meses residuais — motivo real **INDETERMINADO**

340 meses (INSS) ≠ 357 meses (CNIS sem carnês). Há 17 meses que nenhuma hipótese
documentada explica. Conforme a regra da skill `quebra-indeferimento` ("Se o motivo real
não for claro, marque como indeterminado e sugira diligência"): **motivo INDETERMINADO**
quanto a esses 17 meses. Diligência: contagem analítica do processo administrativo (8.2) e
CNIS analítico (8.3).

### 3.5 Desconsideração de documento — vínculo CONFECÇÕES DELTA ME (07/2005-12/2005)

Anotado em CTPS (`documentos/ctps.txt`, anotação 3, com a observação "Periodo NAO consta
no CNIS"). **Não é possível afirmar que o INSS desconsiderou esse documento**, porque não
se sabe se a CTPS foi apresentada no requerimento — **verificar no processo
administrativo**. Fundamento para o cômputo, se não foi analisado:
- presunção de recolhimento das contribuições do segurado **empregado**, "desde que
  comprovado o exercício da atividade" — IN 128, art. 206, § 6º `[FONTE OFICIAL — PDF DOU
  NA BASE]`;
- obrigação da empresa de arrecadar e recolher a contribuição do empregado — Lei 8.212,
  art. 30 `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` (texto não literal na base; inciso
  e alínea exatos `[DISPOSITIVO A CONFIRMAR]`);
- CNIS omisso → prova por documentos contemporâneos — Decreto 3.048, art. 19-B `[FONTE
  SECUNDÁRIA - CONFERIR NO PLANALTO]`;
- valor probatório da CTPS sem rasura — `[JURISPRUDÊNCIA A CONFIRMAR]` (não há enunciado
  sobre CTPS na base `jurisprudencia-vinculante/`; há enunciado da TNU usualmente invocado
  sobre presunção relativa de veracidade da CTPS — **número e redação não verificados**).

**Impacto:** 6 meses. Irrelevante para os pedágios; relevante apenas para a regra de
pontos.

### 3.6 Regra revogada / indeferimento automático

Não há indício de aplicação de regra revogada. A exigência de 30 anos para a mulher está
correta em todas as regras de transição aplicáveis (EC 103, arts. 15, I; 16, I; 17, I; 20,
II) `[FONTE OFICIAL CONFIRMADA]`. O erro está no **tempo apurado**, não no requisito.
Indeferimento automático: **não determinável** sem o processo administrativo.

### 3.7 Síntese do diagnóstico

| Categoria (skill `quebra-indeferimento`) | Conclusão | Documento |
|---|---|---|
| Erro de cálculo | **SIM — provável** (70 meses de diferença para o próprio CNIS) | `cnis.txt` x `carta-indeferimento.txt` |
| Falta de análise / motivação | **SIM — provável** (motivação de uma linha; IN 128, art. 574) | `carta-indeferimento.txt` |
| Desconsideração de documento | **A verificar** (CTPS/DELTA; carnês) | depende do processo administrativo |
| Regra revogada | **NÃO** | — |
| Indeferimento automático | **Indeterminado** | — |
| Motivo dos 17 meses residuais | **INDETERMINADO** | — |

---

## 4. Requisitos — reconferência da contagem da triagem com a base agora disponível

### 4.1 Contagem

Recontagem independente (meses civis, admissão e demissão inclusive — mesmo método da
triagem): ALFA 94 (CNIS) / 95 (CTPS); BETA 90; DELTA 6 (só CTPS); CI 53; GAMA 173.
**Conservador 410 meses (34a 2m); completo 417 meses (34a 9m). Resultados da triagem
confirmados.** Em 13/11/2019: conservador 348 meses (29a 0m + 13 dias); completo 355 meses
(29a 7m + 13 dias).

> A contagem definitiva deve seguir a IN 128, art. 206, § 1º (data a data até 13/11/2019)
> e § 2º (mês integral a partir de 13/11/2019), e art. 207, parágrafo único (mês de 30
> dias, ano de 365 dias) `[FONTE OFICIAL — PDF DOU NA BASE]` — o que exige as datas exatas
> (CNIS analítico). Diferença esperada: dias, não meses.

> O script determinístico da skill (`cruza_cnis_ctps.py`) **não leu** os documentos deste
> caso (formato MM/AAAA, sem NIT por linha): devolveu "0 vínculos / 0a 0m" com código de
> saída 0. A recontagem acima foi feita à parte. Ver relatório de orquestração, item (d).

### 4.2 Enquadramento nas regras de transição — agora com dispositivo e texto oficial

| Regra | Dispositivo | Requisitos (texto oficial) | Conservador | Completo |
|---|---|---|---|---|
| **Pedágio 100%** | EC 103, art. 20, I, II e IV `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 324 `[FONTE OFICIAL — PDF DOU NA BASE]` | 57 anos (M); 30 anos de contribuição; período adicional igual ao tempo que faltava em 13/11/2019 | **ENQUADRA** — 57a em 12/05/2025; faltavam ~11m17d; pedágio cumprido ~11/2021 | **ENQUADRA** |
| **Pedágio 50%** | EC 103, art. 17, caput, I e II `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 323 `[FONTE OFICIAL — PDF DOU NA BASE]` | **mais de 28 anos** de contribuição em 13/11/2019 (M); 30 anos; adicional de 50% do que faltava; sem idade mínima | **ENQUADRA** — 29a 0m em 13/11/2019 (> 28) | **ENQUADRA** |
| Pontos | EC 103, art. 15, I, II e § 1º `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 321 | 86 pontos (M) + 1 ponto/ano desde 01/01/2020 → **92 em 2025**, **93 em 2026** | **NÃO** na DER (91,43) | Limítrofe na DER (92,01 contra 92) |
| Idade progressiva | EC 103, art. 16, I, II e § 1º `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 322 | 56 anos (M) + 6 meses/ano desde 01/01/2020 → **59 em 2025**, **59a 6m em 2026** | **NÃO** (57a 3m na DER) | **NÃO** |

**Antes (triagem de 19/09) estes pontos estavam `[A CONFIRMAR]`:** o requisito de acesso
do pedágio 50% (agora confirmado: "mais de 28 anos", EC 103, art. 17, caput), a pontuação
exigida em 2025 (92) e a idade exigida em 2025 (59) — todos agora extraídos do texto
oficial.

**Ponto de fragilidade, agora quantificado com a norma:** sem os carnês, a segurada teria
24a 7m em 13/11/2019 — **abaixo dos 28 anos** do art. 17 — e 29a 9m no total, abaixo dos 30
anos. **Nenhuma regra fica acessível.** O caso inteiro depende do cômputo do período de CI.

### 4.3 Carência

180 contribuições para aposentadoria por tempo de contribuição — Lei 8.213, art. 25, II
`[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]`; IN 128, arts. 199-200 (resumo da base: "180
contribuições p/ inscritos a partir de 25/07/1991"). Filiada em 1988: regra de transição de
carência da Lei 8.213/1991 (tabela progressiva) `[DISPOSITIVO A CONFIRMAR]` — **não está na
base**; irrelevante na prática (410 ≥ 180, e mesmo os 340 meses do INSS bastam).

### 4.4 Valor do benefício por regra (texto oficial) — por que o pedágio 100% é o pedido principal

| Regra | Cálculo | Dispositivo |
|---|---|---|
| Pedágio 100% | **100% da média** (100% do período contributivo desde 07/1994) | EC 103, art. 20, § 2º, II, c/c art. 26, caput e § 3º, I `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 233, IV, "e" `[FONTE OFICIAL — PDF DOU NA BASE]` |
| Pedágio 50% | média × **fator previdenciário** | EC 103, art. 17, parágrafo único (remete ao art. 29, §§ 7º a 9º, da Lei 8.213/1991); IN 128, art. 233, IV, "d" |
| Pontos / idade progressiva | 60% + 2 p.p. por ano acima de **15 anos** (mulher) → 60% + 2 × 19 = **98%** | EC 103, art. 26, § 2º, I, e § 5º `[FONTE OFICIAL CONFIRMADA]`; IN 128, art. 233, IV, "c" |

O pedágio 100% (100%) supera os pontos (98%) e só perde para o pedágio 50% se o fator
previdenciário for maior que 1 — improvável aos 57 anos de idade, mas **não calculado**: a
base não tem os §§ 7º a 9º do art. 29 da Lei 8.213/1991 nem a tábua de expectativa de
sobrevida do IBGE `[DISPOSITIVO A CONFIRMAR]`. **RMI não estimada:** o CNIS dos autos é
sintético, sem salários de contribuição (regra do `calculo-previdenciario`: "NUNCA estime
RMI sem a fórmula correta").

---

## 5. Tempestividade do recurso ordinário ao CRPS — dispositivo agora confirmado

### 5.1 O dispositivo (antes `[DISPOSITIVO A CONFIRMAR NA BASE]`)

- **Prazo:** "O prazo para interposição dos recursos ordinário e especial, bem como para o
  oferecimento de contrarrazões, é de 30 (trinta) dias a partir da data da intimação da
  decisão [...]" — **IN 128, art. 580, caput** `[FONTE OFICIAL — PDF DOU NA BASE]`.
- **Cabimento:** recurso ordinário às Juntas de Recursos do CRPS — IN 128, art. 578,
  caput; vedado ao INSS recusar o recebimento do recurso — art. 578, § 1º `[FONTE OFICIAL
  — PDF DOU NA BASE]`.
- **Contagem:** dias corridos, "a partir da data da cientificação, excluindo-se da contagem
  o dia do começo e incluindo-se o do vencimento"; prorrogação para o primeiro dia útil —
  IN 128, art. 597 e parágrafo único `[FONTE OFICIAL — PDF DOU NA BASE]`.
- **Ciência:**
  - comunicação preferencialmente eletrônica ou por correspondência — IN 128, art. 548,
    caput;
  - notificação postal válida "a partir da data de recebimento constante do aviso de
    recebimento" — art. 548, § 5º;
  - notificações "consideradas ineficazes quando feitas sem observância das prescrições
    legais", suprida a falta pelo comparecimento do interessado — art. 548, § 7º;
  - a consulta do interessado ao processo eletrônico torna válidas as notificações — art.
    548, § 8º;
  - acompanhamento por canais remotos: notificação presumida após 5 dias da
    disponibilização — art. 549 e art. 599, § 1º;
  - a comunicação da decisão deve conter "a exposição dos motivos, a fundamentação legal e
    o prazo para protocolo de processo administrativo de recurso" — **IN 128, art. 575**.
  `[FONTE OFICIAL — PDF DOU NA BASE]`
- **Camadas superiores, ainda fora da base:** o prazo de 30 dias também está no Decreto
  3.048/1999 (artigo do capítulo de recursos — número **não** está na base) e no Regimento
  Interno do CRPS `[DISPOSITIVO A CONFIRMAR]`. O resumo `decreto-3.048-1999.md` não cobre o
  capítulo de recursos; o Regimento Interno do CRPS não existe na base.

### 5.2 Aplicação ao caso

| Cenário de ciência | Termo inicial | Termo final (IN 128, arts. 580 e 597) | Situação em 15/10/2026 |
|---|---|---|---|
| A — ciência na data da decisão | 20/11/2025 | 20/12/2025 (sábado) → **22/12/2025** | **Vencido há ~10 meses** |
| B — notificação eletrônica presumida (art. 599, § 1º) | 25/11/2025 | 25/12/2025 (feriado) → **26/12/2025** | **Vencido há ~10 meses** |
| C — AR postal com data posterior | data do AR | AR + 30 dias | Vencido, salvo AR posterior a ~15/09/2026 |
| D — **notificação ineficaz** (art. 548, § 7º, c/c art. 575) | **prazo não teria começado a correr**; começaria com o comparecimento ou com a consulta ao processo eletrônico (art. 548, §§ 7º e 8º) | 30 dias a partir desse ato | **Única via de tempestividade** |

**Conclusão de tempestividade:** nos cenários A, B e C (os prováveis), o recurso está
**intempestivo**. A via recursal só é defensável no cenário D, que depende de demonstrar
que a comunicação **não observou a IN 128, art. 575** (sem fundamentação legal e sem
indicação do prazo recursal — exatamente o que falta na carta transcrita nos autos, item 2)
ou que não houve ciência válida.

**Alerta operacional:** pela IN 128, art. 548, § 8º, e art. 599, caput, **a consulta ao
processo eletrônico pelo advogado ou pela segurada torna válida a notificação**. Se o
cenário D for verdadeiro, **a própria diligência de obter cópia do processo (8.2) pode
iniciar o prazo de 30 dias**. Recomenda-se ter a minuta de recurso pronta **antes** do
acesso, e registrar com data e hora o primeiro acesso.

**Risco de efeitos financeiros no recurso:** recurso que traga "novos elementos
extemporâneos à decisão" tem efeitos financeiros fixados na data de apresentação desses
elementos — IN 128, art. 582 — sendo novos elementos os que provem "fato do qual o INSS não
tinha ciência" (art. 587, I) `[FONTE OFICIAL — PDF DOU NA BASE]`. Como o período de carnês
**já constava do CNIS** (`documentos/cnis.txt`), sustenta-se que **não é elemento novo**; a
CTPS do vínculo DELTA pode ser tratada como nova se não foi juntada ao requerimento.

---

## 6. Decadência e prescrição (antes pendentes na triagem, item 8.9)

- **Decadência:** não há prazo decadencial contra a rediscussão de **indeferimento**. O
  STF, na **ADI 6096/DF**, declarou inconstitucional a extensão da decadência decenal do
  art. 103, caput, da Lei 8.213/91 ao indeferimento, cancelamento e cessação —
  `legislacao/jurisprudencia-vinculante/adi-6096-2021-resumo.md`. **Divergência
  encontrada:** a IN 128, art. 592 (texto de 2022, no PDF da base), ainda conta a
  decadência "do dia em que tomar conhecimento da decisão indeferitória definitiva" —
  redação que reflete a parte da Lei 13.846/2019 invalidada pela ADI 6096. Se o INSS
  alegar decadência com base nesse artigo da IN, prevalece a ADI. **Sem impacto prático
  hoje** (11 meses desde a decisão), mas relevante se o caso se arrastar.
- **Prescrição quinquenal:** 5 anos contados de quando cada parcela deveria ter sido paga
  — IN 128, art. 595 `[FONTE OFICIAL — PDF DOU NA BASE]`; Lei 8.213, art. 103, parágrafo
  único `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]`. DER 15/08/2025 → **nenhuma parcela
  prescrita**; a primeira começaria a prescrever por volta de 09/2030.

---

## 7. RECOMENDAÇÃO DE VIA DE REVERSÃO

### 7.1 Via principal — **AÇÃO JUDICIAL DE CONCESSÃO** (JEF), DIB em 15/08/2025

Fundamentos:
1. **Interesse de agir presente:** houve requerimento e indeferimento expresso — STF, Tema
   350 (RE 631.240), na base: a exigência de prévio requerimento "não se confunde com
   exigência de exaurimento da via administrativa".
2. **DIB na DER:** TNU, Súmula 33 (na base) — preenchidos os requisitos na data do
   requerimento administrativo, "esta data será o termo inicial da concessão do
   benefício".
3. Requisitos implementados já na DER pelo pedágio 100% (principal) e pelo pedágio 50%
   (sucessivo) — item 4.2.
4. Nenhum óbice de decadência (ADI 6096) nem de prescrição (item 6).
5. Não depende da tese frágil de tempestividade (item 5).

Minuta: `minutas/peticao-inicial-DRAFT.md`.

### 7.2 Via condicional — **RECURSO ORDINÁRIO AO CRPS**, **somente** no cenário D (item 5.2)

Defensável apenas se o processo administrativo mostrar notificação ineficaz ou ciência
tardia. Minuta condicional: `minutas/recurso-crps-DRAFT.md`.

**Não protocolar recurso e ação ao mesmo tempo sem decisão expressa do advogado.** A regra
usual é que a ação judicial com objeto idêntico importa renúncia ao recurso administrativo
ou desistência do recurso interposto (Decreto 3.048/1999 — artigo do capítulo de recursos,
número **não** na base) `[DISPOSITIVO A CONFIRMAR]`. A escolha é **sequencial**, não
paralela: (i) obter o processo administrativo; (ii) se houver cenário D, decidir entre
recurso (mais rápido, sem custas, mas com o risco do art. 582) e ação; (iii) sem cenário
D, ação.

### 7.3 Via administrativa alternativa — novo requerimento com pedido de reabertura do NB anterior

A triagem (item 10.2) tratou o novo requerimento como perda certa do retroativo. **A base
agora permite matizar isso:** "Constatado erro, ainda que em fase de novo requerimento, o
processo administrativo anterior, já concluído, deverá ser reaberto de ofício para a
concessão do benefício, observada a decadência e a prescrição" — **IN 128, art. 576,
parágrafo único** `[FONTE OFICIAL — PDF DOU NA BASE]`. Ou seja: em tese, um novo
requerimento instruído com as guias, pedindo **expressamente** a reabertura do NB
123.456.789-0, poderia preservar a DIB em 15/08/2025 sem ação judicial. **Riscos:** depende
de o INSS reconhecer "erro" (e não "elemento novo" — arts. 583, § 1º, e 587); incide a
biometria obrigatória (Portaria DIRBEN/INSS 1.347/2026, `INDICE.md`, item 7) e a
verificação de processo em curso (IN 128, art. 576-A, alterado pela IN 208/2026 — **o
artigo 576-A não está no PDF de 2022 da base** `[DISPOSITIVO A CONFIRMAR]`). Decisão
estratégica do advogado, com ciência da cliente.

---

## 8. Diligências (ordem de prioridade)

1. **8.1 Guias/carnês 03/2006-07/2010** — código de recolhimento (alíquota 20% x 11%/5%),
   competência, vencimento e **data efetiva de pagamento** (hipóteses 3.3 a/b/c).
2. **8.2 Cópia integral do processo administrativo** (IN 128, art. 602, §§ 1º e 2º —
   cópia digital; acesso por advogado com procuração `[FONTE OFICIAL — PDF DOU NA BASE]`):
   contagem analítica, despacho, **comprovante e meio da ciência** (AR, canal eletrônico,
   data de disponibilização). **Atenção ao alerta do item 5.2.**
3. **8.3 CNIS analítico** (salários de contribuição, indicadores de pendência, datas
   exatas) — também indispensável para a RMI.
4. **8.4 CTPS integral** e **prova complementar do vínculo DELTA** (holerites, TRCT, FGTS,
   situação do CNPJ 55.666.777/0001-88).
5. **8.5 Carta original de indeferimento** (para confirmar a ausência de fundamentação
   legal e de prazo recursal — itens 2 e 5.2-D).

---

## 9. Quadro de pendências remanescentes desta análise

| Item | Situação |
|---|---|
| Prazo recursal no Decreto 3.048/1999 e no Regimento Interno do CRPS | `[DISPOSITIVO A CONFIRMAR]` — fora da base (a IN 128, art. 580, está confirmada) |
| Renúncia ao recurso pela propositura de ação | `[DISPOSITIVO A CONFIRMAR]` — Decreto 3.048/1999, fora da base |
| Arts. 52-56 da Lei 8.213/1991 (aposentadoria por tempo de contribuição) | Base sem conteúdo confiável (52-53 desatualizados; 54-56 sem pesquisa). Fundamento substituído pela EC 103 (oficial) e IN 128, arts. 320-324 (oficial) |
| Lei 8.213/1991, art. 29, §§ 7º-9º (fator previdenciário) | `[DISPOSITIVO A CONFIRMAR]` |
| Tabela progressiva de carência (filiados antes de 24/07/1991) | `[DISPOSITIVO A CONFIRMAR]` — irrelevante no resultado |
| Valor probatório da CTPS | `[JURISPRUDÊNCIA A CONFIRMAR]` |
| Motivo dos 17 meses residuais | INDETERMINADO — diligência 8.2 |
| RMI | Não calculável sem o CNIS analítico |

> **Observação (16/10/2026, não altera as conclusões desta análise):** o
> Regimento Interno do CRPS (RICRPS) foi localizado e processado na base
> — ver `legislacao/crps/regimento-interno-crps-2026.md`, aprovado pela
> Portaria MPS nº 125/2026. As duas linhas acima ("Prazo recursal no
> Decreto 3.048/1999 e no Regimento Interno do CRPS" e "Renúncia ao
> recurso pela propositura de ação") **deixam de depender do Decreto
> 3.048/1999** (que não contém o Regimento) e passam a ter fundamento no
> RICRPS: prazo de 30 dias no art. 77 (confirma, sem alterar, a conclusão
> já baseada na IN 128, art. 580) e renúncia tácita no art. 86. Isso não
> muda o resultado desta análise (a tempestividade do recurso já estava
> fundamentada na IN 128/2022), mas remove a marcação `[DISPOSITIVO A
> CONFIRMAR]` dessas duas linhas para fins de citação formal.

---

**RASCUNHO — sujeito a revisão do advogado responsável. Nenhum erro do INSS foi afirmado
sem indicação do documento específico; onde o documento não existe nos autos, a conclusão
foi marcada como "a verificar" ou "indeterminada".**
