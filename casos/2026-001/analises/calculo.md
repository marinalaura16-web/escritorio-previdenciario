# CÁLCULO PREVIDENCIÁRIO — CASO 2026-001

> **RASCUNHO PARA REVISÃO DO ADVOGADO.** Documento produzido por sistema de apoio
> (`calculo-previdenciario`). Nenhum número aqui apurado autoriza protocolo de requerimento
> administrativo ou peça processual sem conferência do profissional habilitado.
> Data do cálculo: 20/09/2026 · Cliente: JULIO CESAR DA SILVA (CPF 030.896.214-10)
> Base: `casos/2026-001/analises/triagem.md` + reprocessamento próprio dos documentos originais.

---

## 0. RESSALVA SOBRE A BASE NORMATIVA (obrigatória, conforme protocolo do agente)

`legislacao/leis-ordinarias/lei-8.213-1991.md` e `legislacao/emendas-constitucionais/ec-103-2019.md`
**não existem como arquivos de texto integral** — a pasta `legislacao/` contém apenas
`INDICE.md` e `ATUALIZACAO.md` (confirmado nesta execução; ver também "Pendências desta base",
item 1, do próprio `INDICE.md`). Todos os dispositivos citados abaixo (Lei 8.213/1991, arts.
28-33 e 48-58; EC 103/2019) foram aplicados **com base no `INDICE.md`** e no conhecimento
técnico-jurídico geral do agente, **não em texto legal integral conferido neste ambiente**.
Isso é especialmente sensível em dois pontos:

1. **Redação exata do art. 26 da EC 103/2019** quanto ao piso de anos (15/20/25) usado no
   bônus de 2% ao ano para a **aposentadoria especial** — sinalizado como
   **[BASE NORMATIVA A CONFIRMAR]** na Seção 6.
2. **Redação exata do art. 21 da EC 103/2019** (regra de 86 pontos da especial) quanto a usar
   "tempo de contribuição total" ou "tempo de efetiva exposição" — sinalizado como
   **[BASE NORMATIVA A CONFIRMAR]** na Seção 5.2.

Nenhuma jurisprudência é citada como certa neste documento (STF, ADI 6309/DF, é tratada apenas
como premissa herdada da triagem, cujo trânsito em julgado e modulação **não foram
reexaminados por este agente** — ver `triagem.md`, item 9.2, ainda pendente de confirmação).

---

## 1. DOCUMENTOS VERIFICADOS

| Documento | Presente | Observação |
|---|---|---|
| CNIS.pdf | Sim | Reextraído com `pdftotext -layout`; 13 páginas, texto nativo — íntegra e legível |
| CTPS_1.pdf / CTPS_2.pdf | Sim | Imagem (scan); dados usados são os já transcritos e citados por página/folha na triagem |
| CTPS_DIGITAL.pdf | Sim | Reextraído com `pdftotext`; texto nativo — confirma datas e cargos |
| PPP_COOPSERSA.pdf (dossiê de 6 PPP + LTCAT + ART) | Sim | Formulário majoritariamente escaneado (apenas rótulos de campo em texto extraível); dados usados são os já transcritos e citados por folha na triagem |

CNIS e CTPS **ambos presentes** — não é necessário solicitar documento ao orquestrador.
Não há inconsistência que justifique interrupção do cálculo (regra "PARE se ilegível" não se
aplica: os documentos são legíveis; há **divergências de conteúdo**, que são tratadas na
Seção 4, não um problema de legibilidade).

---

## 2. METODOLOGIA

1. **Recontagem de tempo (Y/M/D):** diferença de calendário entre datas reais, com a
   convenção usual de contagem de tempo de contribuição (ambas as extremidades incluídas,
   i.e., soma-se 1 dia ao resultado da subtração simples de datas). Essa convenção foi
   testada e **reproduz exatamente** os números da triagem (29a5m10d; 22a7m3d; 27a8m0d),
   confirmando que a mesma metodologia foi usada em ambos os relatórios.
2. **Conversão de tempo especial em comum (fator 1,4):** período convertido para dias pela
   convenção administrativa 1 ano = 365 dias / 1 mês = 30 dias, multiplicado pelo fator, e
   reconvertido pela mesma convenção. Essa é a convenção que reproduz os números de
   referência da triagem (≈31a7m e ≈38a6m) e é a usualmente adotada em simulações de CTC.
3. **Cruzamento CNIS × CTPS:** tentou-se rodar `scripts/cruza_cnis_ctps.py` e
   `scripts/calcula_tempo.py` da skill `calculo-tempo-contribuicao`. **Optou-se por não usar
   a saída bruta dos scripts como fonte de tempo líquido**, pelo seguinte motivo técnico,
   registrado para transparência: os scripts fazem *parsing* por regex de pares de datas
   MM/AAAA e **somam vínculos sem tratar concomitância** (não há deduplicação de períodos
   sobrepostos) — o que, neste caso de 10 vínculos com múltiplas sobreposições (SOSERVI ×
   Hospitais Associados × LIBER × FMS × Hospital de Ávila × COOPSERSA), geraria
   **duplicação de tempo**, exatamente a hipótese vedada pela regra 2 da skill
   ("NUNCA calcule o tempo a averbar como tempo líquido e certo") e pelo princípio de que
   dias concomitantes não se somam. Por isso, o cálculo definitivo abaixo foi refeito
   **manualmente, competência a competência**, com apoio de scripts Python auxiliares de
   verificação de datas (não commitados ao caso), usando os dados extraídos diretamente do
   CNIS e cotejados com a CTPS e o PPP. Os scripts da skill permanecem úteis para casos com
   vínculos não concomitantes; **neste caso não são adequados isoladamente**.
4. **Fonte de dados salariais:** todas as 314 competências com remuneração lançada no CNIS
   foram extraídas e somadas por competência (tratando concomitância de vínculos por soma de
   valores no mesmo mês, não por soma de tempo).

### 2.1 ATUALIZAÇÃO (pós-cálculo) — bug de concomitância na skill corrigido

O bug descrito no item 3 acima (`cruza_cnis_ctps.py` somava vínculos sem excluir
concomitância) **foi corrigido** após a emissão deste relatório — ver
`.claude/skills/calculo-tempo-contribuicao/scripts/cruza_cnis_ctps.py`, função
`unir_periodos()`. O script agora une intervalos sobrepostos antes de somar.

Testado com os 10 vínculos reais deste caso, o script corrigido apurou o tempo comum
total (união, sem duplicar concomitância) em **29a 6m** (dado curado manualmente) e em
**29a 2m** (rodando direto sobre o texto extraído do CNIS/CTPS Digital, usando a última
competência do próprio extrato — 05/2026 — como referência para os vínculos ainda
ativos). Nenhum dos dois bate exatamente com os **29a 5m 10d** apurados manualmente
neste documento (Seção 4, dia a dia).

> ⚠️ **PENDENTE DE RECONCILIAÇÃO ANTES DA PETIÇÃO.** Diferença de aproximadamente
> **20 dias** entre a apuração manual (29a5m10d, precisão de dia, referência 20/09/2026)
> e a saída do script (29a6m ou 29a2m, precisão de mês, referência variável conforme
> execução). Hipóteses prováveis, ainda não verificadas uma a uma: (a) o script trabalha
> em granularidade de **mês** (MM/AAAA), enquanto a apuração manual usa **dia exato**
> (DD/MM/AAAA) — arredondamentos de início/fim de mês podem explicar até ~30 dias de
> diferença por si só; (b) a data de referência para os vínculos ativos difere entre as
> duas execuções (20/09/2026 na apuração manual vs. 05/2026, última competência do CNIS,
> na execução direta do script). **Antes de usar qualquer um dos dois números em petição
> ou requerimento, refazer a conferência linha a linha** (script vs. manual, competência
> a competência) e registrar aqui qual apuração prevalece e por quê.

---

## 3. CRUZAMENTO CNIS × CTPS × PPP — CONFIRMAÇÃO PRÓPRIA

Reextraindo o CNIS e a CTPS Digital diretamente dos PDFs, **confirmo integralmente** o quadro
de 10 vínculos e as 8 divergências already mapeadas na triagem (`triagem.md`, Seções 4.1 e
4.2). Não foram encontradas divergências adicionais na comparação CNIS × CTPS Digital.

**Um ponto adicional, não destacado na triagem, foi identificado nesta reapuração** — relevante
especificamente para o **tempo especial**, não para o tempo comum:

> **Divergência adicional (i): FMS Ipojuca (matr. 12145/1) — fim da exposição especial
> documentada é anterior ao fim do vínculo.**
> O vínculo no CNIS vai de 01/07/2017 a 04/07/2024. O PPP (fls. 15-16, conforme triagem)
> declara **exposição** apenas até **29/02/2024** (lotação até 06/02/2024). Ou seja, os
> últimos ~4 meses desse vínculo (03/2024 a 07/2024) **não têm cobertura documental de
> especialidade por este PPP especificamente**. Isso **não reduz o tempo especial total do
> caso**, porque esse mesmo intervalo está integralmente coberto pelo PPP concomitante dos
> Hospitais Associados de Pernambuco (vínculo contínuo, especial, de 20/09/2010 até
> 10/12/2024) — mas passa a constar do registro para o caso de a tese depender, no futuro,
> de sustentar a especialidade **isoladamente** pelo vínculo do FMS.

Todas as demais 8 divergências (a-h da triagem) foram confirmadas como descritas. O quadro de
impacto por cenário está consolidado na Seção 7.

---

## 4. TEMPO DE CONTRIBUIÇÃO COMUM

### 4.1 Cenário CONSERVADOR (somente CNIS)

Reconstituindo a linha do tempo unicamente a partir dos 10 vínculos do CNIS (datas oficiais,
sem qualquer correção via CTPS):

- Vínculo SOSERVI (seq. 1): 11/04/1997 a 14/09/2011 — contém integralmente os vínculos
  seq. 2 (SOSERVI duplicado) e Unid. de Traumatologia de Boa Viagem (2001).
- Vínculo Hospitais Associados de Pernambuco (seq. 4): 20/09/2010 a **ativo** — inicia
  **antes** do fim do vínculo SOSERVI (14/09/2011), **eliminando qualquer hiato** entre os
  dois. A partir daqui, o vínculo é contínuo e ininterrupto até hoje, absorvendo em seu
  interior LIBER, FMS Ipojuca (ambas as matrículas), Hospital de Ávila e COOPSERSA (todos
  concomitantes com Hospitais Associados).

**Resultado: união de todos os períodos = 11/04/1997 a 20/09/2026, sem solução de
continuidade.**

| Grandeza | Resultado |
|---|---|
| Tempo de contribuição comum líquido e certo, até 20/09/2026 | **29 anos, 5 meses e 10 dias** |
| Tempo de contribuição comum líquido e certo, até 13/11/2019 (marco EC 103/2019) | **22 anos, 7 meses e 3 dias** |

Ambos os números **conferem exatamente** com a estimativa da triagem, confirmando a
consistência da apuração.

### 4.2 Cenário COM AVERBAÇÃO (CNIS + CTPS)

**Achado central desta apuração: neste caso específico, o cenário "com averbação" não
altera o tempo de contribuição comum líquido total.** Isso ocorre por duas razões
conjugadas, ambas já observadas na triagem (item 4.3) e confirmadas nesta reapuração:

1. **Não há nenhum período que exista somente na CTPS.** Todos os contratos anotados nas
   CTPS física (1 e 2) e na CTPS Digital têm correspondência de datas no CNIS. Portanto, não
   há tempo "a averbar" no sentido de period inédito.
2. **A única divergência de datas entre CNIS e CTPS (Hospital de Ávila: CNIS/PPP encerram em
   15/12/2020; CTPS registra saída em 13/01/2021 por aviso prévio indenizado)** acrescentaria,
   isoladamente, até 29 dias a esse vínculo específico. Mas esse intervalo (16/12/2020 a
   13/01/2021) já está **inteiramente contido** dentro do vínculo contínuo dos Hospitais
   Associados de Pernambuco (que cobre 20/09/2010 até hoje sem interrupção) e também dentro
   do vínculo do FMS Ipojuca (01/07/2017-04/07/2024). Logo, o acréscimo de tempo pela CTPS,
   embora **juridicamente correto de reconhecer** (TRCT e projeção do aviso prévio sustentam
   a data de 13/01/2021 — pendência L6 da triagem), **não move a fronteira da união de
   períodos**, pois esse trecho de calendário já era contado por outro vínculo concomitante.

| Grandeza | Resultado |
|---|---|
| Tempo de contribuição comum líquido e certo, até 20/09/2026 (CNIS + CTPS) | **29 anos, 5 meses e 10 dias** (idêntico ao cenário conservador) |

**Utilidade prática da CTPS neste caso:** não é aumentar o tempo total, e sim (i) corroborar
as datas e cargos (gesseiro/técnico de imobilização) que sustentam o enquadramento especial,
(ii) fixar com precisão a data de saída do Hospital de Ávila para fins de eventual cálculo de
verbas rescisórias ou de isolamento desse vínculo específico, e (iii) confirmar que **nenhum
período do histórico depende de prova exclusivamente testemunhal ou de terceiros** — todo o
tempo já está lastreado por registro no CNIS.

**Nenhuma das 8 divergências (a-h) da triagem, nem a divergência adicional (i) identificada
na Seção 3, altera este total de 29a5m10d de tempo comum**, pelas razões detalhadas na
Seção 7 (quadro de impacto por cenário).

---

## 5. TEMPO ESPECIAL (PPP)

### 5.1 Tempo especial documentado — apuração por união de períodos

Os períodos com PPP apto a sustentar enquadramento (agente biológico, hospitalar, habitual e
permanente, conforme LTCAT/PPP citados na triagem, Seção 6.2) são:

| Período | Empregador | Fonte do limite temporal |
|---|---|---|
| 11/04/1997 – 14/09/2011 | SOSERVI | Fim do vínculo (CNIS/CTPS/PPP convergentes) |
| 20/09/2010 – 10/12/2024 | Hospitais Associados de PE | **Data de emissão do PPP** (10/12/2024) — vínculo segue ativo, mas a exposição só está documentada até essa data (lacuna L1 da triagem) |
| 08/09/2011 – 07/10/2015 | LIBER | Fim do vínculo |
| 01/07/2017 – 29/02/2024 | FMS Ipojuca (matr. 12145/1) | **Data de exposição declarada no PPP**, não a data de fim do vínculo (04/07/2024) — ver divergência adicional (i), Seção 3 |
| 01/02/2020 – 15/12/2020 | Hospital de Ávila | Fim do vínculo (CNIS/PPP) |
| 05/07/2024 – 09/12/2024 | FMS Ipojuca (matr. 12145/2) | Data de lotação declarada no PPP (vínculo segue ativo — lacuna L2) |
| 02/02/2023 – 01/03/2023 | COOPSERSA | **EXCLUÍDO** — sem contrapartida no CNIS (divergência grave, item 4.2.c da triagem); não computável sem PPP retificado |
| 11/2023 | COOPSERSA | **EXCLUÍDO** — sem PPP correspondente |

Fazendo a união desses intervalos (o vínculo dos Hospitais Associados, contínuo de 2010 a
10/12/2024, absorve integralmente LIBER, FMS (ambas as janelas) e Hospital de Ávila; e se
funde com o SOSERVI porque este só termina em 14/09/2011, depois do início daquele):

**União = 11/04/1997 a 10/12/2024, sem interrupção.**

| Grandeza | Resultado |
|---|---|
| **Tempo especial documentado (líquido e certo), até 10/12/2024** | **27 anos e 8 meses** |
| Marco de conclusão dos 25 anos de efetiva exposição | **entre 09 e 10/04/2022** (variação de 1 dia conforme convenção de contagem — não afeta a conclusão) |

Este número confirma exatamente a estimativa da triagem (27a8m0d).

**Ressalva de atualização:** os PPP dos dois vínculos ainda ativos (Hospitais Associados e
FMS matr. 12145/2) foram emitidos em 10/12/2024 e 09/12/2024, respectivamente. Sem PPP
atualizado, os **~21 meses de exposição entre essas datas e 20/09/2026 não estão
documentalmente cobertos**, mesmo que a função e o ambiente de trabalho aparentemente não
tenham mudado (mesma matéria de risco 9.4 da triagem — L1/L2 seguem sendo prioridade máxima
antes de qualquer DER).

### 5.2 Simulação da regra de transição de 86 pontos (EC 103/2019, art. 21) — caso a ADI 6309/DF não seja aplicável ou seja modulada desfavoravelmente

**[BASE NORMATIVA A CONFIRMAR]** — o `INDICE.md` registra que essa regra soma "idade + tempo
de contribuição" (não deixa claro se é o tempo de contribuição *total* do segurado ou apenas o
tempo de *efetiva exposição*). Adoto aqui, como a triagem, a leitura de tempo de contribuição
total, por ser a mais frequentemente aplicada nessa regra de transição; **a redação exata do
art. 21 deve ser conferida antes de qualquer peça.**

| Data | Idade | Tempo de contribuição (total) | Pontos | Situação |
|---|---|---|---|---|
| 20/09/2026 (hoje) | 49,38 | 29,45 | **78,8** | Faltam 7,2 pontos (mínimo de 25 anos de exposição já preenchido) |
| ≈05/2030 (projeção) | ≈52,9 | ≈32,9 | ≈**86,0** | Atingido, mantendo o ritmo atual de contribuição |

Consistente com a estimativa da triagem (≈maio/2030).

---

## 6. TEMPO ESPECIAL CONVERTIDO EM COMUM (fator 1,4) — cenário alternativo, sem uso da especial

A conversão de tempo especial em comum **só é permitida para o período anterior a
13/11/2019** (EC 103/2019, art. 25, § 2º, conforme `INDICE.md`). Todo o tempo de contribuição
do cliente até 13/11/2019 (22a7m3d) é, simultaneamente, tempo especial documentado (o vínculo
SOSERVI e o início dos Hospitais Associados, ambos com PPP, cobrem esse intervalo por
completo).

| Etapa | Valor |
|---|---|
| Tempo especial pré-EC103 (11/04/1997 a 13/11/2019) | 22 anos, 7 meses e 3 dias |
| Convertido por fator 1,4 (homem) | **31 anos, 7 meses e 15 dias** |
| + Tempo comum não convertido (14/11/2019 a 20/09/2026, sem conversão) | 6 anos, 10 meses e 7 dias |
| **= Tempo comum TOTAL com conversão, até 20/09/2026** | **≈ 38 anos, 5 meses e 17 dias** |

Consistente com a estimativa da triagem (≈31a7m e ≈38a6m).

**Pontuação na regra de transição por pontos (103 H + mínimo 35 anos) — Lei 8.213/1991, arts.
52-56 c/c EC 103/2019:**

| Data | Idade | Tempo (com conversão) | Pontos | Situação |
|---|---|---|---|---|
| 20/09/2026 (hoje) | 49,38 | 38,51 | **87,9** | Mínimo de 35 anos já superado; faltam 15,1 pontos |
| ≈04/2034 (projeção) | ≈56,9 | ≈45,9 | ≈**102,8-103** | Atingido, mantendo o ritmo atual |

Consistente com a estimativa da triagem (≈abril/2034). **Confirma-se a conclusão da triagem:
mesmo no cenário mais favorável de tempo de contribuição comum (com conversão), essa rota
chega ~4 anos depois da rota da aposentadoria especial (86 pontos, ≈2030) e muitos anos depois
da tese central do caso (especial sem idade mínima, via ADI 6309/DF, potencialmente já
disponível hoje).**

Demais regras de tempo de contribuição (pedágio 50%, pedágio 100%, idade mínima progressiva,
regra permanente de 65 anos) permanecem **inacessíveis** nos mesmos termos apurados pela
triagem (Seção 8.2 de `triagem.md`) — não recalculadas aqui por não haver qualquer fato novo
que as afete.

---

## 7. CARÊNCIA E QUADRO DE DIVERGÊNCIAS POR CENÁRIO

### 7.1 Carência (Lei 8.213/1991, art. 25, II — 180 contribuições mensais)

Extração própria de todas as competências com remuneração lançada no CNIS (10 vínculos,
somando concomitâncias no mesmo mês) resultou em **314 competências distintas com
contribuição registrada** entre 04/1997 e 05/2026 — praticamente idêntico ao número da
triagem (≈315).

O período total do vínculo contínuo (11/04/1997 a 05/2026, última remuneração lançada) soma
**350 competências potenciais**. A diferença (350 − 314 = 36) corresponde exatamente às
lacunas de remuneração já identificadas dentro do vínculo SOSERVI (item 4.4 da triagem).
Por se tratar de **segurado empregado**, cujo recolhimento é dever do empregador
(Lei 8.212/1991, art. 30, I), essas 36 competências **não podem ser descontadas da carência**
— o vínculo formal (comprovado por CNIS, CTPS e PPP) basta.

**Carência apurada: entre 314 (contagem estrita, só competências com valor lançado) e 350
(contagem por vínculo formal) competências — em qualquer hipótese, muito acima das 180
exigidas. NÃO É ÓBICE em nenhum cenário (conservador ou com averbação) nem para nenhum dos
benefícios simulados.**

### 7.2 Quadro-síntese: qual cenário cada divergência afeta

| Divergência (ref. triagem) | Afeta tempo COMUM? | Afeta tempo ESPECIAL? | Afeta CARÊNCIA? | Afeta RMI? | Cenário afetado |
|---|---|---|---|---|---|
| a) SOSERVI vínculo duplicado (seq. 2) | Não (contido no seq. 1) | Não | Não | **Sim** (duplica base de cálculo em 04-09/1997 até esclarecimento) | Ambos (é interno ao CNIS) |
| b) Hospital de Ávila — data de saída | Não (absorvido por vínculo concomitante) | Marginal — só relevante se a especialidade desse vínculo precisar ser sustentada isoladamente | Não | Marginal (eventual verba rescisória) | Só "com averbação" |
| c) COOPSERSA — período do PPP sem contrapartida no CNIS | Não (o período já conta como comum via CNIS, com outra data) | **Sim — exclui ~1 mês de especial em ambos os cenários** até retificação | Não (competência já conta via CNIS) | Não | Ambos |
| d) Hospitais Associados — salário inicial | Não | Não | Não | **Sim** (prevalece o CNIS, Decreto 3.048/99, art. 19-B) | Ambos |
| e) LIBER — razão social | Não | Não | Não | Não | Nenhum (sem efeito numérico) |
| f) FMS Ipojuca — 1ª remuneração em 08/2017 | Não (vínculo já conta desde 01/07/2017) | Não | Não | Marginal (lançamento acumulado) | Ambos |
| g) COOPSERSA 11/2023 sem PPP | Não | **Sim — não conta como especial em nenhum cenário** | Não | Não | Ambos |
| h) Nome da genitora | Não | Não | Não | Não | Nenhum (divergência superada) |
| i) FMS 12145/1 — exposição do PPP termina antes do vínculo (achado desta apuração) | Não | **Sem efeito no total** (absorvido pelo PPP concomitante dos Hospitais Associados) — mas relevante se essa especialidade precisar ser sustentada isoladamente | Não | Não | Ambos |
| Lacunas SOSERVI (~36 competências sem remuneração) | Não (vínculo conta integralmente) | Não (mesma lógica) | Não (mesma lógica, art. 30, I) | **Sim — reduz a base de cálculo do salário de benefício nesse trecho, salvo prova de salário real (fichas/folhas — pendência L7)** | Ambos |

**Conclusão da Seção 7:** nenhuma das divergências mapeadas altera o tempo de contribuição
comum total (29a5m10d) ou o cumprimento da carência. As divergências relevantes para o
**tempo especial** são (c) e (g) — ambas já excluídas do cálculo da Seção 5 — e o efeito líquido
é nulo sobre o total de 27a8m, porque os períodos excluídos (COOPSERSA) já estavam contidos,
para fins de tempo comum, dentro de vínculos concomitantes cobertos por outro PPP válido. As
divergências relevantes para a **RMI** são (a), (d), (f) e as lacunas de remuneração da
SOSERVI — nenhuma delas muda o tempo, mas todas exigem esclarecimento documental antes de se
tomar o CNIS como base definitiva de salários de contribuição.

---

## 8. RMI ESTIMADA

### 8.1 Fórmula aplicável

- **Salário de benefício (SB):** média aritmética simples de **100% dos salários de
  contribuição** apurados desde 07/1994 (ou desde o início da vida contributiva, se posterior)
  até a DER, **corrigidos monetariamente** pelos índices oficiais (Lei 8.213/1991, art. 29-A/
  art. 29, redação pós-Lei 9.876/1999, mantida na sistemática pela EC 103/2019) — conforme
  `INDICE.md`.
- **Coeficiente (RMI = coeficiente × SB):** **60% + 2% por ano que exceder o tempo mínimo**
  exigido para a respectiva modalidade (EC 103/2019, arts. 19 e 26, conforme `INDICE.md`):
  - Tempo de contribuição comum (homem): mínimo de referência = 20 anos.
  - Aposentadoria especial: mínimo de referência = 25 anos (regra geral do art. 19, §1º, I) —
    **[BASE NORMATIVA A CONFIRMAR]: não há, nesta base, o texto integral do art. 26 que
    confirme se o piso do bônus de 2% para a especial é 25, 20 ou 15 anos conforme o grau de
    risco da atividade. Adoto 25 anos por ser o piso da modalidade efetivamente pleiteada
    neste caso (agente biológico, Anexo IV, código 3.0.1).**
- **Teto:** R$ 8.475,55 (Portaria Interministerial MPS/MF 13/2026, vigente na data deste
  cálculo — o teto vigente na DER real pode ser outro).

### 8.2 Limitação crítica desta apuração — SB não pode ser fechado neste ambiente

Não há, neste ambiente, tabela oficial de correção monetária (INPC) nem tabelas de teto
histórico do RGPS ano a ano. **Por isso, em cumprimento à regra "nunca estimar RMI sem a
fórmula correta", este agente aplica corretamente o coeficiente, mas se abstém de apresentar
uma RMI final em reais** — o que exigiria um SB corrigido monetariamente, tarefa que deve ser
feita com o simulador oficial do INSS (PRISMA/Meu INSS) ou com tabelas de atualização
monetária de que o escritório disponha.

Como referência de **ordem de grandeza apenas** (não corrigida, não utilizável em petição):

| Base de cálculo (nominal, sem correção monetária) | Valor |
|---|---|
| Média nominal de todas as 314 competências com remuneração (04/1997-05/2026) | R$ 2.011,86 |
| Média nominal das últimas 24 competências (06/2024-05/2026) | R$ 4.875,02 |
| Média nominal das últimas 12 competências (06/2025-05/2026) | R$ 5.157,87 |

A primeira linha **subestima grosseiramente** o SB real, porque mistura, sem correção,
salários de 1997 (dezenas/centenas de reais) com salários de 2026 (milhares de reais); a
segunda e a terceira são referências melhores de "salário atual", mas **não substituem** a
média corrigida de toda a vida contributiva exigida por lei.

### 8.3 Coeficientes por cenário (aplicáveis assim que o SB corrigido estiver disponível)

| Cenário | Tempo relevante | Excedente sobre o mínimo | Coeficiente |
|---|---|---|---|
| Tempo de contribuição comum, sem conversão (29a5m10d, mínimo 20a) | 9,42 anos excedentes | 60% + 18,8% | **≈ 78,8%** |
| Tempo de contribuição comum, com conversão do especial pré-2019 (38a5m17d, mínimo 20a) | 18,5 anos excedentes | 60% + 37,0% | **≈ 97,0%** |
| Aposentadoria especial, 25 anos (27a8m documentado, mínimo 25a) — **sujeito à ressalva do item 8.1** | 2,67 anos excedentes | 60% + 5,3% | **≈ 65,3%** |

**Ilustrativamente** (nominal, últimas 24 competências como proxy do salário atual, R$4.875,02
— NÃO utilizável como RMI final): cenário comum sem conversão ≈ R$3.842; com conversão ≈
R$4.729; especial (25 anos) ≈ R$3.184. Todos abaixo do teto (R$8.475,55), confirmando a
observação da triagem de que o teto não é fator limitante neste caso.

---

## 9. QUADRO-RESUMO FINAL

| Item | Cenário conservador (só CNIS) | Cenário com averbação (CNIS + CTPS) |
|---|---|---|
| Tempo comum líquido e certo até 20/09/2026 | 29a 5m 10d | 29a 5m 10d (idêntico — ver Seção 4.2) |
| Tempo comum até 13/11/2019 (marco EC 103) | 22a 7m 3d | 22a 7m 3d |
| Tempo especial documentado (PPP) até 10/12/2024 | 27a 8m 0d | 27a 8m 0d (PPP não é afetado pela CTPS) |
| Marco dos 25 anos de exposição especial | ≈09-10/04/2022 | ≈09-10/04/2022 |
| Tempo comum com conversão do especial pré-2019 | ≈38a 5m 17d | ≈38a 5m 17d |
| Carência | 314-350 competências (≥180 exigidas) | idem |
| Pontos hoje (86 pontos — especial, transição) | 78,8 | 78,8 |
| Pontos hoje (103 pontos — comum, com conversão) | 87,9 | 87,9 |
| RMI | Fórmula aplicada; SB não fechado (ver 8.2) — coeficientes: 78,8% / 97,0% / 65,3% conforme a rota | idem |

**Motivo da identidade entre os dois cenários:** não há nenhum período comprovado
exclusivamente pela CTPS neste caso (triagem, item 4.3, confirmado nesta reapuração), e a
única divergência de data relevante (Hospital de Ávila) está absorvida por vínculo
concomitante contínuo. Isto é, do ponto de vista do **tempo de contribuição total**, o caso
já está no seu "teto documental" com o CNIS isoladamente — a CTPS agrega **qualidade e
robustez probatória** (convergência quase total, cargos técnicos coincidentes com os PPP),
não quantidade adicional de tempo.

---

## 10. PENDÊNCIAS E PRÓXIMOS PASSOS PARA O CÁLCULO DEFINITIVO

1. Obter PPP atualizado dos dois vínculos ativos (Hospitais Associados e FMS matr. 12145/2)
   para incorporar os ~21 meses de exposição especial ainda não documentados (L1/L2 da
   triagem) — isso pode elevar o tempo especial líquido de 27a8m para próximo de 29a5m
   (aproximando-se do próprio tempo comum, dado que praticamente toda a vida laboral do
   cliente é hospitalar).
2. Obter PPP retificado da COOPSERSA (L4) ou excluir esse período da instrução (a triagem já
   recomenda a segunda via, dado o impacto irrisório — 1 mês).
3. Obter fichas/folhas de pagamento da SOSERVI (L7) para as ~36 competências sem remuneração
   lançada — impacto direto na composição do SB, não no tempo.
4. Esclarecer a duplicidade cadastral da SOSERVI (seq. 2, item 4.2.a) e a divergência de
   salário inicial dos Hospitais Associados (item 4.2.d) — ambas com impacto em RMI, não em
   tempo.
5. **Apurar o SB definitivo com tabela oficial de correção monetária (INPC) e tetos
   históricos do RGPS** — tarefa fora do alcance deste ambiente; recomenda-se rodar a
   simulação no Meu INSS/PRISMA ou em planilha própria do escritório com os 314 valores
   nominais aqui extraídos (disponíveis no arquivo de trabalho, se solicitados) já
   organizados por competência.
6. Confirmar, na fonte oficial, a redação vigente do art. 26 da EC 103/2019 quanto ao piso do
   bônus de 2% para a aposentadoria especial (Seção 8.1) e do art. 21 quanto à composição dos
   pontos da transição especial (Seção 5.2) — a base `legislacao/` não contém o texto
   integral.
7. Este cálculo **não reexamina** a ADI 6309/DF do STF (trânsito em julgado/modulação); essa
   verificação, já sinalizada como prioritária pela triagem (item 9.2), condiciona qual das
   três rotas simuladas (especial imediata / 86 pontos em 2030 / 103 pontos com conversão em
   2034) é a que efetivamente está disponível hoje.

---

## 11. RESSALVAS FINAIS

1. **Documento é RASCUNHO** sujeito a revisão do advogado responsável (CLAUDE.md, regra 1).
2. Nenhuma jurisprudência é afirmada como definitiva; a **ADI 6309/DF do STF** é tratada como
   premissa herdada da triagem, não reexaminada quanto a trânsito em julgado/modulação por
   este agente.
   **ATUALIZAÇÃO:** a citação foi corrigida de "Tema 1.231" para **ADI 6.309/DF**, confirmada
   por certidão de julgamento oficial (`legislacao/jurisprudencia-vinculante/`); a
   **modulação de efeitos ainda não foi definida** pelo STF — ver `triagem.md`, Seção 9.2, e
   "Observação sobre a ADI 6309" ao final deste documento. Marca-se
   **[JURISPRUDÊNCIA A CONFIRMAR NA FONTE OFICIAL]** quanto à ementa/DJe, modulação e trânsito
   em julgado; este cálculo não precisa ser refeito por conta disso (a data de referência,
   03/06/2026, e o efeito jurídico — idade mínima afastada — permanecem os mesmos), mas a
   **citação usada em qualquer petição deve aguardar essa confirmação**.
3. Nenhum diagnóstico médico é mencionado (não é matéria deste cálculo).
4. Todos os números de tempo (comum, especial, conversão, pontos) foram recalculados de forma
   independente, competência a competência/dia a dia, e **conferem** com as estimativas da
   triagem — o que reforça a confiabilidade dos dois relatórios, mas não dispensa a revisão
   humana antes de qualquer protocolo.
5. A RMI **não foi fechada em valor final** por indisponibilidade, neste ambiente, de tabelas
   oficiais de correção monetária e de teto histórico — os coeficientes (percentuais) estão
   corretos e prontos para aplicação assim que o SB corrigido estiver disponível.
6. A base `legislacao/` carece de textos integrais; dois pontos específicos (Seções 5.2 e 8.1)
   dependem de confirmação do texto integral da EC 103/2019 antes de uso em petição.
7. `practice-profile.md` contém dados de teste ("Escritório: Teste", "OAB: Teste") — substituir
   antes de qualquer uso em produção.

---

## Reanálise Pós-ADI 6309 (04/09/2026)

> Data desta reanálise: 20/09/2026. Base: dados já apurados nas Seções 4-9 deste documento
> (nenhum número de tempo foi recalculado; esta seção interpreta os números existentes à luz
> da ADI 6309/DF).

### a) A cliente já pode requerer aposentadoria especial?

**Sim, quanto ao requisito de tempo.** Tempo especial documentado (Seção 5.1): **27 anos e
8 meses**, até 10/12/2024 — acima do exigido. Enquadramento por agente biológico em ambiente
hospitalar (Decreto 3.048/1999, Anexo IV, cód. 3.0.1) corresponde à categoria de **25 anos de
efetiva exposição**, ou seja, **art. 19, § 1º, I, alínea "c"** da EC 103/2019 (não "a", 15
anos, nem "b", 20 anos). Marco de conclusão dos 25 anos: **entre 09 e 10/04/2022** (Seção 5.1).

### b) A idade mínima ainda era obstáculo?

**Idade atual (20/09/2026): 49 anos, 4 meses e 17 dias** (nascido 04/05/1977). A alínea "c"
exigiria **60 anos de idade** — o cliente está **10,6 anos abaixo** desse patamar. Sem a
ADI 6309/DF, a idade mínima seria óbice **intransponível até aproximadamente 2037**. Com a
ADI 6309/DF, a idade mínima **deixa de ser exigida** — **desde que a modulação de efeitos
(ainda pendente) não a restabeleça** para casos como este (ver ressalva abaixo).

### c) Data em que os requisitos foram cumpridos pela primeira vez (DIB potencial)

A carência (314-350 competências, Seção 7.1) já estava superada desde o início dos anos 2000.
O único requisito pendente era o tempo de exposição, cumprido em **≈09-10/04/2022**. Essa é a
data-marco material, mas a data que efetivamente pode ser usada como DIB **depende do teor da
modulação de efeitos do STF, ainda não definida**:

| Cenário de modulação | DIB provável | Observação |
|---|---|---|
| Sem modulação (efeito retroativo pleno) | **≈09-10/04/2022** | Sujeito a prescrição quinquenal das parcelas (Lei 8.213/1991, art. 103) — parcelas anteriores a 5 anos do requerimento não seriam pagas, mas o direito ao benefício desde essa data seria reconhecido |
| Modulação a partir do julgamento | **03/06/2026** | Ainda assim posterior ao marco de 04/2022 — o cliente já cumpria os requisitos nessa data |
| Sem reconhecimento de efeito retroativo (via administrativa padrão) | **Data do requerimento administrativo (DER)** | Cenário mais provável na prática administrativa até que haja determinação judicial em contrário |

**Em qualquer um dos três cenários, o cliente já cumpre os requisitos hoje (20/09/2026)** —
a diferença entre eles está apenas em quanto da retroatividade será reconhecida, não em se
o benefício está ou não ao alcance agora.

### d) Comparativo de rotas

| Rota | Base legal | Disponibilidade | Coeficiente RMI (Seção 8.3) | Depende da ADI 6309? |
|---|---|---|---|---|
| **Especial via ADI 6309** | Art. 19, §1º, I, "c" | Potencialmente já disponível (marco ≈04/2022) | ≈65,3% | **Sim — é o fundamento que a viabiliza sem idade mínima** |
| **Especial por pontos (86)** | Art. 21, EC 103/2019 | ≈05/2030 (idade ≈52,9) | Não calculado nesta apuração — usaria a fórmula da especial (mín. 25 anos), com excedente maior que o da rota acima | **Não** — rota alternativa que nunca exigiu idade mínima, disponível independentemente do resultado da ADI |
| **Comum com conversão (103 pontos)** | Arts. 52-56, Lei 8.213/1991, c/c EC 103/2019 | ≈04/2034 (idade ≈56,9) | **≈97,0%** (o mais alto das três rotas calculadas) | **Não** — rota independente |
| **Idade pura (65 anos)** | CF, art. 201, §7º, I | ≈2042 | Não calculado (classificada BAIXA na triagem, Seção 8.2) | Não |

[DISPOSITIVO A CONFIRMAR] — a citação de CF, art. 201, §7º, I acima segue a mesma referência
já usada em `triagem.md` (Seção 8.2), mas o texto integral da Constituição não está na base
`legislacao/` (ver Seção 0 deste documento); confirmar a redação exata antes de uso em petição.

**Mais vantajosa em RMI:** a rota de tempo comum com conversão (103 pontos) tem o maior
coeficiente calculado (**97,0%**), mas só fica disponível em **~2034** — quase 8 anos depois
da rota especial via ADI 6309. Isso cria uma tensão real, não apenas numérica: esperar mais
tempo aumenta o coeficiente da RMI, mas exige que o cliente permaneça exposto ao agente
nocivo por quase mais uma década — precisamente o cenário que a fundamentação da própria
ADI 6309/DF (Min. André Mendonça) qualificou como incompatível com a finalidade protetiva da
aposentadoria especial (ver `adi-6309-2026-resumo.md`). **A maximização de RMI não deve ser
usada como critério isolado de recomendação** — cabe ao advogado apresentar esse trade-off
(valor do benefício × tempo de exposição a agente nocivo) ao cliente, e não decidi-lo por ele.

### Ressalva desta reanálise

Nenhum número de tempo, carência ou coeficiente foi recalculado — todos vêm das Seções 4 a 9
já auditadas. Esta seção apenas interpreta esses números à luz da ADI 6309/DF. A conclusão de
viabilidade **permanece condicionada** à confirmação, na fonte oficial (DJe), de: ementa,
trânsito em julgado e, sobretudo, **modulação de efeitos** — que decide qual das três datas de
DIB do item (c) acima efetivamente se aplica.

---

## Observação sobre a ADI 6309

- A decisão da ADI 6309/DF (03/06/2026) declarou inconstitucional APENAS a idade mínima para
  aposentadoria especial (art. 19, § 1º, I, a, b, c, EC 103/2019).
- Permanecem válidas: a vedação à conversão de tempo especial em comum (art. 25, § 2º) e os
  novos critérios de cálculo (art. 26, § 2º, IV).
- O placar "6x5" é inferência baseada na contagem nominal — aguardar acórdão oficial para
  confirmar.
- Modulação de efeitos e trânsito em julgado ainda pendentes.

---
*Relatório gerado pelo agente `calculo-previdenciario` · Caso 2026-001 · 20/09/2026*
