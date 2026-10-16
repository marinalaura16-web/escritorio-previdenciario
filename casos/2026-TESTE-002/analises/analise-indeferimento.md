# RASCUNHO — PARA REVISÃO DO ADVOGADO

# ANÁLISE DE INDEFERIMENTO — CASO 2026-TESTE-002

**[CASO SIMULADO - DADOS FICTÍCIOS PARA TESTE DO SISTEMA - NÃO É CLIENTE REAL]**

**Data da análise:** 16/10/2026
**Protocolo aplicado:** Especialista em Quebra de Indeferimento (leitura da carta +
processo administrativo disponível; consulta à base de legislação; identificação do
motivo formal x motivo real; verificação de desconsideração de documento / erro de
cálculo / regra revogada / falta de análise; recomendação de via).
**Subagentes:** não foi necessário nem possível acionar outro subagente nesta sessão
(ferramenta de disparo indisponível, mesma limitação já registrada em sessões
anteriores do projeto — ver `CLAUDE.md`, Sessão de 15/10/2026, Bloco 10). Toda a
análise abaixo foi feita diretamente.
**Natureza:** RASCUNHO. Não é parecer definitivo. Nenhuma peça deve ser protocolada
sem revisão do advogado responsável.

---

## 0. Convenção de proveniência usada neste documento

| Marcação | Significado |
|---|---|
| `[FONTE OFICIAL — PDF DOU NA BASE]` | Texto conferido nesta análise por leitura de `legislacao/instrucoes-normativas/in-128-2022.txt` — extração mecânica (`pdftotext`) do PDF oficial `in-128-2022.pdf` (DOU), que integra a base deste projeto. |
| `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` | Dispositivo presente nos resumos `.md` da base, montados por WebSearch, sem conferência byte a byte. |
| `[DISPOSITIVO A CONFIRMAR]` | Dispositivo que a pesquisa não localizou com conteúdo confiável na base. Não usar em peça sem conferir na fonte oficial. |
| `[JURISPRUDÊNCIA A CONFIRMAR]` | Precedente não incorporado (ou incorporado com incerteza) à base `jurisprudencia-vinculante/`. |

---

## 1. Documentos analisados

| Documento | Arquivo | Conteúdo relevante |
|---|---|---|
| Comunicação de decisão | `documentos/carta-indeferimento.txt` | NB 987.654.321-0; espécie 41 (aposentadoria por idade rural); DER 20/08/2026; decisão 25/09/2026; INDEFERIDO |
| CNIS | `documentos/cnis.txt` | Único vínculo: empregada doméstica 03/2016-10/2016 (Recife/PE), recolhimentos regulares, sem pendência; nenhum outro vínculo ou indicador de atividade rural (coerente com a natureza não contributiva do segurado especial) |
| Autodeclaração do segurado especial | `documentos/autodeclaracao-segurada-especial.txt` | Atividade rural desde 1985 (14 anos); interrupção confessada 03/2016-10/2016 por estiagem, com retorno em 11/2016, ininterrupto até hoje; grupo familiar |
| Certidão de casamento | `documentos/certidao-casamento.txt` | Casamento em 18/11/1989; ambos os cônjuges qualificados como "lavrador"/"lavradora" |
| Declaração do sindicato rural | `documentos/declaracao-sindicato-rural.txt` | Filiação desde 14/02/1990; registra o mesmo afastamento temporário 03-10/2016 |
| Notas de produtor rural (amostra) | `documentos/notas-produtor-rural.txt` | Vendas de produção rural de 1991 a 2026, em nome do marido (titular do bloco), com lacuna exatamente entre 03/02/2016 e 14/11/2016 — **coerente** com a interrupção confessada |
| CCIR/ITR | `documentos/ccir-itr-imovel-rural.txt` | Imóvel de 20 ha ≈ 1,43 módulo fiscal (abaixo do limite de 4 módulos); sem empregados permanentes; ITR regular (2025) |
| Ficha escolar dos filhos | `documentos/ficha-escolar-filhos.txt` | Matrículas de 1998 e 2001, pais qualificados como agricultor/agricultora |

**Documento não disponível:** cópia do processo administrativo NB 987.654.321-0 (contagem analítica, comprovante e meio exato de ciência da decisão — AR, canal eletrônico, data de disponibilização). Isso limita a precisão do item 5 (tempestividade) e é a diligência nº 1 (item 8).

---

## 2. Motivo formal (transcrição literal da carta)

> "DECISAO: INDEFERIDO
> Motivo: Nao restou comprovado o exercicio de atividade rural, em regime de economia
> familiar, de forma ininterrupta, no periodo de carencia imediatamente anterior ao
> requerimento (180 meses). Consta do CNIS da requerente vinculo empregaticio urbano
> (CNPJ 22.333.444/0001-55, categoria empregada domestica) no periodo de 03/2016 a
> 10/2016, o que descaracteriza a qualidade de segurada especial a partir dessa data.
> Considerando-se apenas o periodo posterior ao referido vinculo urbano (11/2016 a
> 08/2026), a requerente conta com aproximadamente 117 (cento e dezessete) meses de
> efetivo exercicio de atividade rural, numero insuficiente para completar os 180 meses
> exigidos."
> — `documentos/carta-indeferimento.txt`, linhas 15-23

**O que a carta não contém:** nenhum dispositivo legal citado como fundamento (nem Lei
8.213/91, nem IN 128/2022); nenhuma análise dos documentos de início de prova material
eventualmente já apresentados no requerimento (autodeclaração, certidão de casamento,
notas de produtor, CCIR/ITR, ficha escolar, declaração sindical); e, até onde consta
deste arquivo `.txt`, **nenhuma indicação de prazo recursal** — o que a IN 128/2022,
art. 575, exige expressamente da comunicação de decisão (ver item 5.1). Ressalva: o
`.txt` pode ser transcrição parcial; confirmar contra a carta original antes de alegar
a ausência de prazo recursal como vício autônomo.

---

## 3. Diagnóstico do motivo real

### 3.1 O cálculo aritmético do INSS está correto — mas o critério jurídico usado para "zerar" o período anterior é o problema

De novembro/2016 a agosto/2026 são, de fato, 117 meses (10 anos menos 3 meses) — a
conta do INSS confere. **Não há, portanto, erro de cálculo no sentido estrito.** O
problema está em **qual período o INSS decidiu contar**: a decisão trata o vínculo
urbano de 8 meses (03/2016 a 10/2016) como um corte definitivo que **elimina
integralmente**, para fins de carência, os mais de 30 anos de atividade rural
anteriores (desde 1985, pela autodeclaração; desde 1989/1990, por prova contemporânea
— certidão de casamento e filiação sindical) — tratando a requerente, a partir de
11/2016, como se estivesse "zerada".

### 3.2 A tese do INSS contradiz a própria norma regulamentar que ele aplica

A IN PRES/INSS 128/2022 — a norma operacional do próprio INSS, extraída mecanicamente
do PDF oficial que integra esta base (`legislacao/instrucoes-normativas/in-128-2022.pdf`
/ `.txt`) — tem **dois dispositivos diretamente contrários à lógica usada na carta**:

> "Art. 201. Para o segurado especial que não contribui facultativamente, o período de
> carência é contado a partir do início do efetivo exercício da atividade rural,
> mediante comprovação.
> § 1º Considera-se como período de carência o tempo de efetivo exercício de atividade
> rural, **ainda que de forma descontínua**, correspondente ao número de meses
> necessários à concessão do benefício requerido."
> — IN 128/2022, art. 201, caput e § 1º `[FONTE OFICIAL — PDF DOU NA BASE]`

> "Art. 259. Para as aposentadorias por idade dos trabalhadores rurais, **não será
> considerada a perda da qualidade de segurado nos intervalos entre as atividades
> rurícolas**."
> — IN 128/2022, art. 259 `[FONTE OFICIAL — PDF DOU NA BASE]`

Ou seja: a própria norma do INSS **autoriza expressamente a descontinuidade** na
contagem da carência rural e determina que **não se considera a perda da qualidade de
segurado nos intervalos entre períodos rurícolas**. A carta, ao excluir
*integralmente* o período anterior a 03/2016 em vez de apenas desconsiderar os 8 meses
efetivamente urbanos (03 a 10/2016) e somar o restante do período rural comprovado,
aplica um critério mais restritivo do que o da própria IN 128/2022.

Veja-se também, quanto ao requisito de exercício de atividade rural na DER:

> "Art. 258. Para fins de concessão de aposentadoria por idade dos trabalhadores
> rurais, o segurado deve estar exercendo a atividade rural ou em período de graça na
> DER ou na data em que implementou todas as condições exigidas para o benefício."
> — IN 128/2022, art. 258, caput `[FONTE OFICIAL — PDF DOU NA BASE]`

A requerente está em atividade rural ininterrupta desde 11/2016 até a DER
(20/08/2026) — mais de 9 anos e 9 meses —, de modo que esse requisito está satisfeito
de sobra, independentemente da controvérsia sobre o período anterior.

**Nuance sobre exclusão temporária da categoria (para não exagerar o argumento):** a
mesma IN 128/2022, art. 113, I, "c", prevê que o segurado especial fica excluído dessa
categoria "a contar do 1º (primeiro) dia do mês em que... enquadrar-se em qualquer
outra categoria de segurado obrigatório do RGPS" `[FONTE OFICIAL — PDF DOU NA BASE]` —
o que é coerente com a exclusão da condição de segurada especial **durante** os 8
meses em que esteve empregada doméstica (categoria de segurado obrigatório distinta).
**O erro do INSS não está em reconhecer essa exclusão temporária** — isso é correto —,
**mas em tratá-la como extintiva de todo o período de carência anterior**, quando os
arts. 201, § 1º, e 259 da mesma IN tratam exatamente da hipótese de descontinuidade e
determinam a soma dos períodos rurícolas, e não o descarte do que veio antes do
intervalo.

### 3.3 A jurisprudência vinculante da base confirma a tese de reversão

> "O exercício de atividade urbana intercalada não impede a concessão de benefício
> previdenciário de trabalhador rural, condição que deve ser analisada no caso
> concreto."
> — **Súmula 46 da TNU** — `legislacao/jurisprudencia-vinculante/sumulas-tnu.md`, item 8

Esta é a súmula diretamente aplicável ao caso: a requerente teve uma única interrupção
de 8 meses, por motivo específico e comprovável (estiagem — autodeclaração e notas de
produtor, com lacuna exatamente nesse intervalo), dentro de uma trajetória rural de
mais de 30 anos antes da interrupção e de quase 10 anos depois dela. A "análise no
caso concreto" que a súmula exige pesa fortemente a favor da requerente: não se trata
de alguém que migrou definitivamente para a cidade e depois alegou retorno oportunista
à zona rural pouco antes do requerimento, mas de um episódio pontual e documentado em
mais de três décadas de atividade rural ininterrupta fora desse intervalo.

**Súmulas de reforço (sem serem, isoladamente, o fundamento central):**
- **Súmula 149 do STJ** ("A prova exclusivamente testemunhal não basta à comprovação
  da atividade rurícola...") — por isso a autodeclaração e a documentação material já
  reunida são indispensáveis; a prova testemunhal deve ser produzida como
  **complemento**, nunca como prova isolada.
- **Súmula 6 da TNU** (certidão de casamento como início razoável de prova material do
  cônjuge) e **Súmula 34 da TNU** (exigência de contemporaneidade do início de prova
  material) — ambas atendidas: a certidão de casamento é de 1989 e os demais
  documentos (sindicato 1990, notas 1991-2026, escola 1998/2001) são contemporâneos
  aos períodos que pretendem provar.
- **Súmula 30 da TNU** (tamanho do imóvel não afasta, por si só, a condição de
  segurado especial) — **não chega a ser necessária neste caso**, já que o imóvel
  (20 ha ≈ 1,43 módulo fiscal) está bem abaixo do limite de 4 módulos fiscais da IN
  128/2022, art. 110, § 2º `[FONTE OFICIAL — PDF DOU NA BASE]`; citada apenas por
  completude.
- **Súmula 272 do STJ** — **não se aplica a este caso.** Trata de aposentadoria por
  **tempo de serviço/contribuição** do segurado especial (exige contribuições
  facultativas), benefício distinto da aposentadoria por **idade** rural ora
  requerida, cuja carência (IN 128/2022, art. 201) admite comprovação sem
  contribuição. Mencionada aqui apenas para evitar confusão caso apareça em pesquisa
  complementar.

### 3.4 Ressalva sobre a declaração do sindicato rural

A Lei 13.846/2019 revogou o inciso III do art. 106 da Lei 8.213/91, que autorizava a
comprovação da atividade rural **apenas** pela declaração do sindicato da categoria,
ratificada pelo INSS (`legislacao/leis-ordinarias/lei-13.846-2019.md`, bloco sobre o
art. 106, III — `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` quanto à redação exata).
Isso é coerente com a lista de documentos hoje aceitos pela IN 128/2022, art. 116, que
trata a "ficha de inscrição ou registro sindical" (inciso XXIX) e a "contribuição
social ao sindicato" (inciso XXX) como **um item de início de prova material entre
outros**, não como prova autossuficiente `[FONTE OFICIAL — PDF DOU NA BASE]`. **Uso
recomendado:** `documentos/declaracao-sindicato-rural.txt` deve instruir o
recurso/ação como prova **complementar e corroborativa**, somada à autodeclaração e
aos demais documentos materiais (certidão de casamento, notas de produtor, CCIR/ITR,
ficha escolar) — nunca como fundamento isolado.

### 3.5 Síntese do diagnóstico (categorias do protocolo)

| Categoria | Conclusão |
|---|---|
| Erro de cálculo | **NÃO** — a conta de 117 meses (11/2016 a 08/2026) está aritmeticamente correta |
| Desconsideração de documento | **Parcial/indireta** — a carta não demonstra ter analisado nenhum dos 6 documentos de início de prova material do período anterior a 2016; isso **não pode ser afirmado com certeza** sem o processo administrativo (diligência 8.1), mas é coerente com uma decisão de uma única frase, sem fundamentação legal |
| Regra revogada | **NÃO** — a exigência de 180 meses de carência está correta (IN 128/2022, art. 256, § 1º, c/c arts. 201-205) |
| Falta de análise/motivação | **SIM, provável** — decisão de um único parágrafo, sem dispositivo legal citado, sem exame individualizado dos documentos, sem indicação de prazo recursal (ver item 2) |
| **Motivo real — categoria adicional, fora das 4 do protocolo padrão** | **Interpretação jurídica equivocada sobre o efeito do intervalo urbano na carência rural**: o INSS tratou a interrupção temporária (8 meses) como extinção retroativa de toda a carência anterior, em contradição com os arts. 201, § 1º, e 259 da própria IN 128/2022 e com a Súmula 46 da TNU |

---

## 4. Avaliação da tese do INSS à luz da legislação e da jurisprudência — conclusão

**A tese do INSS está incorreta.** Os fundamentos:

1. **Texto da própria norma do INSS (IN 128/2022, arts. 201, § 1º, e 259)** —
   contagem descontínua expressamente admitida; não se considera a perda da qualidade
   de segurado nos intervalos entre atividades rurícolas, para fins de aposentadoria
   por idade rural.
2. **Jurisprudência vinculante da base (Súmula 46 da TNU)** — interrupção urbana
   intercalada não impede, por si só, a concessão do benefício; exige análise do caso
   concreto, que aqui favorece a requerente (interrupção pontual, motivada e
   documentada, dentro de décadas de atividade rural).
3. **Suficiência aritmética do período total:** mesmo descontando os 8 meses urbanos
   (03 a 10/2016) — que de fato não podem ser contados como rurais —, a requerente tem
   mais de 30 anos de atividade rural anterior a 2016 (autodeclaração desde 1985;
   prova contemporânea seguramente a partir de 1989/1990) somados aos 117 meses já
   reconhecidos pelo próprio INSS depois de 11/2016. **Faltam apenas 63 meses (5 anos e
   3 meses) para completar os 180 exigidos** — quantidade amplamente coberta pelo
   período rural anterior a 2016, ainda que se adote um critério conservador de
   contagem a partir da certidão de casamento (1989) ou da filiação sindical (1990).

**Reconhecimento expresso do que falta verificar:** este diagnóstico depende de
confirmar, no processo administrativo, se os documentos de início de prova material
já constavam do requerimento original (DER 20/08/2026) e não foram analisados, ou se
são complementares a serem juntados agora no recurso/ação (diligência 8.1 e 8.2).

---

## 5. Tempestividade do recurso ordinário ao CRPS

### 5.1 Dispositivos aplicáveis (IN PRES/INSS 128/2022, extração do PDF oficial)

- **Cabimento:** "Das decisões proferidas pelo INSS poderão os interessados interpor
  recurso ordinário às Juntas de Recursos do Conselho de Recursos da Previdência
  Social - CRPS" — art. 578, caput; vedado ao INSS recusar o recebimento do recurso —
  art. 578, § 1º `[FONTE OFICIAL — PDF DOU NA BASE]`.
- **Prazo:** "O prazo para interposição dos recursos ordinário e especial, bem como
  para o oferecimento de contrarrazões, é de 30 (trinta) dias a partir da data da
  intimação da decisão [...]" — art. 580, caput `[FONTE OFICIAL — PDF DOU NA BASE]`.
- **Contagem:** "contados em dias corridos, a partir da data da cientificação,
  excluindo-se da contagem o dia do começo e incluindo-se o do vencimento"; prorrogação
  para o primeiro dia útil seguinte se o vencimento cair em dia sem expediente — art.
  597, caput e parágrafo único `[FONTE OFICIAL — PDF DOU NA BASE]`.
- **Ciência:** comunicação preferencialmente eletrônica ou por correspondência (art.
  548, caput); válida, por via postal, a partir da data de recebimento no AR (art. 548,
  § 5º); notificações eletrônicas presumidas válidas 5 dias após a disponibilização
  (arts. 549 e 599, § 1º); notificações sem observância das prescrições legais são
  ineficazes, suprida a falta pelo comparecimento do interessado (art. 548, § 7º); a
  comunicação da decisão deve conter "a exposição dos motivos, a fundamentação legal e
  o prazo para protocolo de processo administrativo de recurso" (art. 575, caput)
  `[FONTE OFICIAL — PDF DOU NA BASE]`.

### 5.2 Aplicação ao caso — hoje é 16/10/2026

| Cenário de ciência | Termo inicial | Termo final (arts. 580 e 597) | Situação em 16/10/2026 |
|---|---|---|---|
| A — ciência na própria data da decisão (hipótese **mais desfavorável** à requerente) | 25/09/2026 | 25/10/2026 (confirmar se é dia útil; se não for, prorroga-se) | **Ainda não vencido — faltam cerca de 9 dias** |
| B — notificação eletrônica presumida 5 dias após disponibilização (art. 599, § 1º), supondo disponibilização em 25/09 | 30/09/2026 | ~30/10/2026 | **Ainda não vencido — margem maior** |
| C — AR postal com data de recebimento alguns dias após a decisão (hipótese mais comum na prática) | data do AR (provavelmente late-09/2026 ou início de 10/2026) | AR + 30 dias | **Ainda não vencido — margem maior que no cenário A** |
| D — notificação ineficaz (art. 548, § 7º, c/c art. 575), se a carta realmente não indicou o prazo recursal nem a fundamentação legal (ver item 2) | prazo não teria nem começado a correr | — | **Também favorável — prazo integral ainda disponível** |

**Conclusão de tempestividade: o recurso administrativo está TEMPESTIVO em qualquer um
dos cenários**, inclusive no mais desfavorável à requerente (cenário A, ciência no
próprio dia da decisão). Isso contrasta com o caso de referência `2026-TESTE-001`
(prazo já vencido) — aqui o indeferimento é recente (25/09/2026) e a análise foi feita
dentro de 3 semanas.

**Diligência indispensável antes de protocolar:** confirmar no processo administrativo
a data e o meio exatos de ciência (AR, canal eletrônico, ou comparecimento), para
fixar o termo final com precisão e, especialmente, para não perder a janela por engano
de contagem. Ainda assim, mesmo no pior cenário, há folga de cerca de 9 dias a partir
de hoje.

**Alerta operacional (mesmo padrão identificado no caso 2026-TESTE-001):** pela IN
128/2022, art. 548, § 8º, e art. 599, caput, a **consulta ao processo eletrônico pelo
advogado ou pela segurada torna válida a notificação**. Se a ciência ainda não tiver
ocorrido de forma inequívoca (cenário D), a própria diligência de obter cópia do
processo (item 8.2) pode antecipar o início do prazo. Recomenda-se ter a minuta de
recurso preparada **antes** desse acesso.

---

## 6. Decadência e prescrição

- **Decadência:** não se aplica. O caso é de **indeferimento** de primeiro
  requerimento, não de revisão de benefício já concedido. A ADI 6096/DF (STF) —
  `legislacao/jurisprudencia-vinculante/adi-6096-2021-resumo.md` — já havia declarado
  inconstitucional a extensão da decadência decenal do art. 103, caput, da Lei
  8.213/91 justamente às hipóteses de indeferimento/cancelamento/cessação, de modo que,
  mesmo antes dessa ADI, o prazo que importa aqui é o prazo recursal de 30 dias (item 5),
  não um prazo decadencial.
- **Prescrição quinquenal:** "Prescreve em 5 (cinco) anos, a contar da data em que
  deveria ter sido paga, toda e qualquer ação para haver prestações vencidas..." — IN
  128/2022, art. 595 `[FONTE OFICIAL — PDF DOU NA BASE]`; Lei 8.213/91, art. 103,
  parágrafo único `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]`. DER 20/08/2026 → nenhuma
  parcela prescrita; irrelevante neste estágio inicial.

---

## 7. RECOMENDAÇÃO DE VIA DE REVERSÃO

### 7.1 Via principal recomendada — RECURSO ORDINÁRIO AO CRPS

Fundamentos para preferir o recurso administrativo, neste caso específico (diferente
do caso 2026-TESTE-001, em que o recurso estava vencido):

1. **Tempestividade confirmada com folga**, em qualquer cenário de ciência (item 5.2).
2. **Sem custas** e **sem necessidade de citação/contestação formal** — via mais rápida
   para preservar a DIB na própria DER (20/08/2026), sem o tempo de tramitação de uma
   ação judicial.
3. **A tese jurídica é sólida e **autofundada na própria norma do INSS** (IN 128/2022,
   arts. 201, § 1º, e 259) e em súmula vinculante específica da TNU (Súmula 46)** — ou
   seja, não depende de reinterpretação constitucional nem de produção de prova nova
   complexa: trata-se de pedir à própria autarquia (em segunda instância, as Juntas de
   Recursos do CRPS) que aplique corretamente sua própria instrução normativa.
4. **Risco limitado:** pela IN 128/2022, art. 582, "no caso de recurso de decisão do
   INSS com apresentação de novos elementos extemporâneos à decisão administrativa [...],
   os efeitos financeiros devem ser fixados na data de apresentação dos novos elementos"
   `[FONTE OFICIAL — PDF DOU NA BASE]`, sendo novos elementos os que provem fato do qual
   o INSS não tinha ciência (art. 587, I). **Diligência crítica:** verificar no
   processo administrativo quais dos 6 documentos de prova material já constavam do
   requerimento original — se já constavam (o que é provável, dado que o INSS citou
   especificamente o período de 03-10/2016, sugerindo que examinou ao menos o CNIS e,
   presumivelmente, a autodeclaração), o recurso não introduz "elemento novo" e a DIB é
   preservada em 20/08/2026 sem risco de redução dos efeitos financeiros.

### 7.2 Via alternativa — AÇÃO JUDICIAL (JEF), se o CRPS mantiver o indeferimento

Caso a Junta de Recursos mantenha a decisão, a ação judicial permanece disponível,
sem prejuízo de prazo (ausência de decadência, item 6) e com a mesma tese de mérito
(arts. 201/258/259 da IN 128/2022 c/c Súmula 46 da TNU, reforçada por prova
testemunhal em audiência — Súmula 149 do STJ). Nesse cenário, atentar para a **Súmula 7
do STJ** ("a pretensão de simples reexame de prova não enseja recurso especial") —
reforça a importância de produzir prova robusta já nas instâncias ordinárias
(administrativa e, se necessário, 1º grau/Turma Recursal), já que eventual reexame em
instância extraordinária tende a ser obstado quando a controvérsia for essencialmente
fático-probatória.

**Não protocolar recurso e ação ao mesmo tempo sem decisão expressa do advogado** — a
escolha é sequencial: (i) obter o processo administrativo (diligência 8.1); (ii)
confirmar a data exata de ciência para computar o prazo com precisão; (iii) protocolar
o recurso ao CRPS dentro do prazo confirmado; (iv) só considerar a via judicial se o
CRPS mantiver o indeferimento, ou antes disso, apenas se o advogado identificar risco
concreto de perda do prazo recursal por informação ainda não disponível nesta análise.

---

## 8. Avaliação do conjunto de início de prova material

**Conjunto robusto, bem alinhado à lista de documentos aceitos pela própria norma do
INSS** (IN 128/2022, art. 116, incisos III, IX, XI, XVII, XXIX e XXX
`[FONTE OFICIAL — PDF DOU NA BASE]`):

| Documento do caso | Dispositivo correspondente (IN 128/2022, art. 116) | Período coberto | Observação |
|---|---|---|---|
| Certidão de casamento (`certidao-casamento.txt`) | Inciso XI | 18/11/1989 | Ambos os cônjuges qualificados como lavrador/lavradora; reforçado pela Súmula 6 da TNU |
| Declaração do sindicato rural (`declaracao-sindicato-rural.txt`) | Incisos XXIX/XXX | 14/02/1990 até hoje (com nota do afastamento 03-10/2016) | Prova **complementar**, não autossuficiente desde a revogação do art. 106, III, da Lei 8.213/91 (item 3.4) |
| Notas de produtor rural (`notas-produtor-rural.txt`) | Inciso III/IV/V | Amostra 1991-2026, com lacuna exatamente em 03-11/2016 | A lacuna **corrobora, em vez de prejudicar**, a autodeclaração da interrupção — mostra coerência interna do conjunto probatório |
| CCIR/ITR (`ccir-itr-imovel-rural.txt`) | Inciso IX | Vigente (ITR 2025 regular) | Também afasta qualquer dúvida sobre módulos fiscais (20 ha ≈ 1,43 módulo, bem abaixo do limite de 4 — IN 128/2022, art. 110, § 2º) |
| Ficha escolar dos filhos (`ficha-escolar-filhos.txt`) | Inciso XVII | 1998 e 2001 | Pais qualificados como agricultor/agricultora; preenche a lacuna temporal entre o casamento (1989) e as notas mais antigas disponíveis (1991) |
| Autodeclaração (`autodeclaracao-segurada-especial.txt`) | Art. 115, caput e § 1º (Anexo VIII) | Desde 1985 | Peça central do processo, mas **não dispensa** corroboração por início de prova material (Súmula 149 do STJ) — função já cumprida pelos demais documentos |

**Pontos fortes:** (i) contemporaneidade quase integral (documentos de 1989 a 2026,
cobrindo praticamente toda a vida adulta da requerente — atende à Súmula 34 da TNU);
(ii) **coerência interna** entre os documentos — a lacuna nas notas fiscais coincide
exatamente com o período confessado de afastamento, o que reforça a credibilidade do
conjunto, em vez de ser uma fragilidade; (iii) área do imóvel bem abaixo do limite
legal, afastando controvérsia sobre módulo fiscal.

**Pontos a reforçar antes do protocolo:** (i) o talonário físico completo de notas do
produtor rural ainda não foi digitalizado (ressalva do próprio documento) — recomenda-se
juntar o talonário integral ou cópia autenticada; (ii) produzir prova testemunhal
(Súmula 149 do STJ exige corroboração testemunhal quando a prova documental, por si só,
deixar dúvida); (iii) confirmar se os documentos (ou ao menos a autodeclaração e o CNIS)
já constavam do requerimento original, para a análise de "elemento novo" do item 7.1,
n. 4.

---

## 9. Diligências (ordem de prioridade)

1. **9.1** Cópia integral do processo administrativo NB 987.654.321-0 — contagem
   analítica do INSS, despacho fundamentado, e **comprovante e meio exato da ciência**
   (data do AR, canal eletrônico, data de disponibilização) — essencial para fixar com
   precisão o termo final do prazo recursal (item 5.2) e para avaliar o risco de
   "elemento novo" (item 7.1, n. 4).
2. **9.2** Carta original de indeferimento (não apenas a transcrição `.txt`) — para
   confirmar se de fato não há fundamentação legal nem indicação de prazo recursal
   (itens 2 e 5.1).
3. **9.3** Talonário físico completo das notas do produtor rural (ou cópia autenticada),
   1985-2026 — o resumo juntado é apenas amostra representativa.
4. **9.4** Arrolamento de testemunhas (vizinhos, presidente do sindicato, membros da
   comunidade rural) para produção de prova testemunhal complementar, em eventual
   justificação administrativa ou em audiência judicial.
5. **9.5** Confirmar, no requerimento original (DER 20/08/2026), quais documentos já
   foram apresentados, para delimitar o que é "elemento novo" para fins do art. 582 da
   IN 128/2022.

---

## 10. Quadro de pendências remanescentes desta análise

| Item | Situação |
|---|---|
| Redação literal exata do art. 48, §§ 1º/2º, e do art. 143 da Lei 8.213/91 (carência rural, comprovação sem contribuição) | `[NÃO LOCALIZADO - PENDENTE]` na base (`lei-8.213-1991.md` registra apenas o art. 48 de forma genérica, sem §§) — não impede a conclusão desta análise, que se apoiou diretamente na IN 128/2022 (fonte oficial, arts. 201/258/259), mas deve ser conferido para a petição final |
| Redação exata do art. 106, III, da Lei 8.213/91 (revogado) e do art. 38-B (CNIS a partir de 2023) | `[FONTE SECUNDÁRIA - CONFERIR NO PLANALTO]` |
| Data exata de ciência da decisão | Não disponível nesta análise — diligência 9.1 |
| Dia da semana de 25/10/2026 (para saber se há prorrogação do termo final no cenário A) | Não verificado nesta análise — conferir antes de protocolar |
| Súmula 85 da TNU, Súmula 291 do STJ e outras não relacionadas a este caso | Não aplicáveis aqui — mencionadas apenas por constarem da base |

---

**RASCUNHO — sujeito a revisão do advogado responsável. Nenhum erro do INSS foi
afirmado sem indicação do documento e do dispositivo específico; onde o documento
necessário não está nos autos (processo administrativo completo), a conclusão foi
marcada como "a verificar" por diligência, não afirmada como certa.**
