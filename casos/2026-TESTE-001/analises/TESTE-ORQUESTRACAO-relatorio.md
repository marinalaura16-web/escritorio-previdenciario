# RASCUNHO — PARA REVISÃO DO ADVOGADO

# RELATÓRIO DO TESTE DE ORQUESTRAÇÃO — CASO 2026-TESTE-001

**Data:** 15/10/2026
**Autor:** `orquestrador-prev`
**Objeto:** teste deliberado da coordenação multiagente sobre o caso 2026-TESTE-001 (MARIA
APARECIDA DA SILVA — aposentadoria por tempo de contribuição indeferida em 20/11/2025 com
28a 4m 12d apurados). **Não é demanda de cliente nova.** Nenhum `git commit`/`push` foi
feito.

**Arquivos produzidos nesta execução (todos novos — nenhum arquivo existente foi
alterado):**
- `casos/2026-TESTE-001/analises/analise-indeferimento.md`
- `casos/2026-TESTE-001/minutas/peticao-inicial-DRAFT.md` (via principal)
- `casos/2026-TESTE-001/minutas/recurso-crps-DRAFT.md` (via condicional)
- `casos/2026-TESTE-001/analises/TESTE-ORQUESTRACAO-relatorio.md` (este arquivo)

A triagem de 19/09/2026 (`analises/triagem-viabilidade.md`) foi **mantida intacta** como
registro histórico; as atualizações estão na análise de indeferimento.

---

## (a) Quais subagentes foram efetivamente acionados, e em que ordem

**Resposta direta: NENHUM subagente foi efetivamente acionado.**

O arquivo `.claude/agents/orquestrador-prev.md` declara `tools: Read, Write, Glob, Grep,
Bash, Agent`. Nesta execução, porém, o ambiente expôs ao orquestrador **apenas** Read,
Write, Glob, Grep e Bash (mais a ferramenta de devolução do resultado ao agente chamador).
**Não havia ferramenta de disparo de subagente (Agent/Task)**. A causa mais provável é que
o próprio orquestrador rodou como subagente de outra sessão, e esse ambiente não permite
subagentes aninhados. Isso não foi verificado além da constatação de que a ferramenta não
existia. Também **não havia a ferramenta Edit**, embora `settings.json` a permita.

Diante disso, apliquei a **Regra de Ouro** do meu prompt ("Se um subagente falhar [...],
REFAÇA você mesmo a análise"). A exceção virou o caminho principal: executei eu mesmo, em
sequência, o protocolo escrito de cada especialista, lendo antes a definição do agente e a
skill correspondente.

| Ordem | Etapa | Protocolo seguido | Executor real | Saída |
|---|---|---|---|---|
| 0 | Consulta obrigatória da base | `CLAUDE.md`, `practice-profile.md`, `legislacao/INDICE.md`, skill `legislacao-previdenciaria` | orquestrador | — |
| 1 | Releitura dos documentos e da triagem de 19/09 | — | orquestrador | — |
| 2 | Diagnóstico do indeferimento e via de reversão | `analise-indeferimento` + skill `quebra-indeferimento` | **orquestrador** (subagente não acionado) | `analise-indeferimento.md` |
| 3 | Confirmação de contagem e cenários de RMI | `calculo-previdenciario` + skill `calculo-tempo-contribuicao` | **orquestrador**, parcial: rodei o script da skill, ele falhou sem avisar (item d.4), recontei à parte e não calculei RMI (não há salários de contribuição nos autos) | seção 4 de `analise-indeferimento.md` (não gerei `calculo.md`) |
| 4 | Minuta de recurso ordinário (condicional) | `recurso-crps` + skill `recurso-crps` | **orquestrador** (subagente não acionado) | `recurso-crps-DRAFT.md` |
| 5 | Minuta de petição inicial (via principal) | `redacao-peticao` + skill `peticao-previdenciaria` | **orquestrador** (subagente não acionado) | `peticao-inicial-DRAFT.md` |
| 6 | Auditoria das citações depois de gravar os arquivos | lógica do hook `anti-alucinacao.py` rodada sobre os arquivos, ignorando os marcadores | orquestrador | item (d.3) abaixo |
| — | `analise-arquivo-medico` | não se aplica (não há questão médica) | — | — |

---

## (b) A coordenação funcionou como descrita no meu prompt?

**Parcialmente. Classificar e consolidar funcionaram; acionar subagentes não funcionou.**

| Passo do prompt | Resultado |
|---|---|
| 1. Receber a demanda | OK |
| Consultar o `INDICE.md` antes de acionar subagentes | OK |
| 2. Classificar e acionar o subagente correspondente | **Classificação OK** (indeferimento → diagnóstico → recurso e/ou petição; cálculo opcional; arquivo médico não se aplica). **Acionamento: FALHOU** por falta de ferramenta. Substituído pela execução direta dos protocolos. |
| 3. Fluxo de múltiplas etapas "Triagem → Cálculo → (Arquivo Médico) → Redação" | **Não serviu para este caso.** O fluxo do prompt não inclui `analise-indeferimento` nem `recurso-crps`, que eram justamente as etapas centrais aqui. A sequência foi definida pelo pedido do usuário, não pelo prompt. |
| 4. Consolidar em relatório executivo | OK (este relatório e o resumo devolvido ao chamador) |
| Regra de Ouro (nenhum parecer sem consulta à base) | Cumprida. Todas as saídas citam a base e distinguem fonte oficial, fonte secundária e "a confirmar". |

**Achados sobre a arquitetura (valem mesmo quando os subagentes puderem ser acionados):**
1. **As definições dos especialistas são muito curtas** (5 a 15 linhas cada). Na prática, o
   conteúdo útil está nas regras gerais do `CLAUDE.md`, não no "especialista". Acionar um
   subagente acrescentaria pouco além de separar contextos.
2. **As ferramentas dos especialistas não alcançam a fonte primária que resolveu este caso.**
   `analise-indeferimento` (Read, Write, Glob, Grep) e `recurso-crps` (Read, Write, Glob —
   sem Grep) **não têm Bash** e, portanto, não podem rodar `pdftotext` no PDF da IN 128 da
   base. O resumo `.md` da IN registra o Livro IV só por faixas ("prazo de 30 dias
   (578-582)"). Um subagente com essas ferramentas provavelmente teria repetido a pendência
   da triagem ou citado a faixa inteira. Só leria o artigo exato percorrendo o PDF de 244
   páginas com Read, página por página.
3. **Os pré-requisitos de `redacao-peticao` não batem com os nomes reais dos arquivos do
   caso.** O agente exige `analises/triagem.md`, `calculo.md` e `divergencias-cnis-ctps.md`;
   o caso tem `triagem-viabilidade.md` e não tem os outros dois. Seguido ao pé da letra, o
   subagente pararia ou improvisaria.

---

## (c) Comparação: o que a triagem de 19/09 deixou "a confirmar" e o que foi fundamentado agora

Base: tabela do item 12 de `triagem-viabilidade.md` (16 itens), mais os pontos pendentes no
corpo da triagem.

**Legenda:** **OFICIAL** = texto conferido nesta data no PDF oficial que está na base, por
extração mecânica de texto (IN 128/2022; EC 103/2019). **SECUNDÁRIA** = resumo `.md`
montado por WebSearch. **PENDENTE** = continua fora da base.

| # | Item pendente em 19/09 | Situação em 15/10/2026 | Dispositivo | Nível |
|---|---|---|---|---|
| 1 | CF — aposentadoria por tempo de contribuição | Resolvido por outro caminho: depois da EC 103 o benefício só existe pelas regras de transição | EC 103, arts. 15-17 e 20 | **OFICIAL** |
| 2 | CF — contagem recíproca | Número localizado (não usado no caso) | CF, art. 201, § 9º | **OFICIAL** (texto da EC 103, art. 1º) |
| 3 | Lei 8.213 — aposentadoria por tempo de contribuição | **Não resolvido na Lei**: arts. 52-53 da base desatualizados; 54-56 sem pesquisa. Contornado por outra fonte | IN 128, arts. 320-324 + EC 103 | Lei: **PENDENTE**; substituto: **OFICIAL** |
| 4 | Carência de 180 contribuições | Resolvido | Lei 8.213, art. 25, II | SECUNDÁRIA |
| 5 | Período de graça / direito adquirido após perda da qualidade | Parcial: art. 15 identificado (incisos não confirmados); regra do direito adquirido fora da base | Lei 8.213, art. 15 | SECUNDÁRIA / **PENDENTE** |
| 6 | Prescrição quinquenal | Resolvido | IN 128, art. 595; Lei 8.213, art. 103, parágrafo único | **OFICIAL** / SECUNDÁRIA |
| 7 | Tabela de transição de carência (filiados antes de 24/07/1991) | **Pendente** — fora da base (o hook bloqueia o número em teste) | — | **PENDENTE** (irrelevante no resultado) |
| 8 | Lei 8.212 — responsabilidade do empregador | Resolvido em duas camadas | IN 128, art. 206, § 6º; Lei 8.212, art. 30 | **OFICIAL** / SECUNDÁRIA |
| 9 | Pedágio 50% — "faltar até 2 anos" e cálculo | **Resolvido**: "mais de 28 anos" em 13/11/2019 (mulher); média × fator previdenciário | EC 103, art. 17, caput e parágrafo único; IN 128, art. 323 | **OFICIAL** |
| 10 | Pedágio 100% — cálculo | **Resolvido**: 100% da média | EC 103, art. 20, § 2º, II, c/c art. 26, § 3º, I; IN 128, art. 233, IV, "e" | **OFICIAL** |
| 11 | Tabela de pontos 2025+ | **Resolvido**: 86 + 1/ano → 92 (2025), 93 (2026) | EC 103, art. 15, § 1º | **OFICIAL** |
| 12 | Tabela de idade progressiva 2025+ | **Resolvido**: 56 + 6 meses/ano → 59 (2025), 59a 6m (2026) | EC 103, art. 16, § 1º | **OFICIAL** |
| 13 | **Prazo de 30 dias do recurso ordinário** | **Resolvido na camada da IN**: 30 dias da intimação; dias corridos; regras de ciência e notificação ineficaz. Decreto 3.048 e Regimento Interno do CRPS continuam fora da base | IN 128, arts. 580, 597, 548, 549, 575, 599 | **OFICIAL** (IN) / **PENDENTE** (Decreto, Regimento) |
| 14 | Vedação de novo requerimento com processo em curso | Parcial: o art. 576-A citado no `INDICE.md` **não está** no PDF de 2022 (foi inserido depois); a IN 208/2026 não está na base | IN 128, art. 576-A | **PENDENTE** |
| 15 | Jurisprudência — valor probatório da CTPS | **Pendente** — a base `jurisprudencia-vinculante/` não tem nada sobre CTPS | — | **PENDENTE** |
| 16 | Correção monetária e juros | Parcial: só a Súmula 148 do STJ (Lei 6.899/1981); os critérios atuais não estão na base | — | **PENDENTE** |

**Saldo dos 16 itens:** **9 resolvidos com fonte oficial** (o item 13 só na camada da IN),
**2 só com fonte secundária**, **5 pendentes ou parciais**.

**Ganhos que a triagem não tinha nem como pendência:**
- **ADI 6096/DF**: não há decadência para rediscutir o indeferimento. A triagem (item 8.9)
  deixara a decadência "a confirmar". **Divergência encontrada:** a IN 128, art. 592 (texto
  de 2022), ainda conta a decadência a partir da "decisão indeferitória definitiva" —
  redação que a ADI invalidou.
- **STF Tema 350** (interesse de agir), **TNU Súmula 33** (DIB na DER) e **STF Tema 1091**
  (fator previdenciário) — todos na base, usados na petição.
- **Diagnóstico concreto da glosa dos carnês** (IN 128, arts. 207, 208, 210 e 216). Revelou
  uma hipótese que **pode derrubar a tese de "erro do INSS"**: recolhimento com alíquota
  reduzida de 5% ou 11% não conta para aposentadoria por tempo de contribuição sem
  complementação (IN 128, art. 216, V, "a"). A triagem tratava os carnês como quase
  certamente computáveis.
- **Via administrativa que a triagem dava por inviável para o retroativo:** a IN 128, art.
  576, parágrafo único, manda reabrir de ofício o processo anterior "constatado erro, ainda
  que em fase de novo requerimento". Em tese, isso preserva a DIB de 15/08/2025.
- **Alerta operacional sobre o prazo recursal:** a consulta ao processo eletrônico torna a
  notificação válida (IN 128, art. 548, § 8º; art. 599). Se a notificação original foi
  ineficaz, o próprio pedido de cópia do processo pode **iniciar** os 30 dias.
- **Risco de efeitos financeiros no recurso:** se o recurso trouxer elementos novos, os
  efeitos contam da data em que forem apresentados (IN 128, arts. 582 e 587).

**Ressalva de proveniência:** "OFICIAL", para a IN 128, significa o PDF do DOU **que está
na base** (`legislacao/instrucoes-normativas/in-128-2022.pdf`), lido por extração mecânica
(`pdftotext`). Não é o resumo `.md`, que só traz faixas de artigos. Para a EC 103, fiz uma
**conferência mecânica pontual** (arts. 15-17, 20 e 26) contra o PDF oficial. Os números
conferem com `ec-103-2019.md`, mas apareceram **dois erros descritivos nesse arquivo da
base** (item d.6).

---

## (d) Dificuldades, bloqueios do hook e limitações reais

### d.1 Sem ferramenta de subagente
Ver item (a). É a limitação central do teste: **não houve coordenação multiagente real**.
Houve um agente executando quatro protocolos em sequência.

### d.2 Sem ferramenta Edit → nenhuma edição na base
Sem Edit, corrigir arquivos da base exigiria **reescrever o arquivo inteiro** com Write
(`ec-103-2019.md` tem ~60.000 caracteres, com risco de alterar texto sem querer) ou editar
via **Bash**. Editar via Bash **escaparia do hook**, que só intercepta `Write|Edit`.
Decidi **não editar nenhum arquivo de `legislacao/`** e apenas registrar as correções
recomendadas (d.6).

### d.3 Hook `anti-alucinacao.py` — o que aconteceu de fato
- **Nenhuma gravação real foi bloqueada.** Os três arquivos do caso contêm, de propósito, o
  marcador exato `[DISPOSITIVO A CONFIRMAR]` em pontos realmente pendentes. Pelo desenho do
  hook, **um único marcador em qualquer lugar do texto libera todas as citações não
  encontradas**, com aviso. O aviso não apareceu no retorno da ferramenta Write.
- **Os bloqueios que observei vieram de testes deliberados** (entrada JSON simulada no hook,
  antes de gravar):

| Citação de teste | Resultado do hook | Realidade |
|---|---|---|
| `Decreto 3.048, art. 305` | BLOQUEADO | Correto: não está na base |
| `Decreto 3.048/1999, art. 305` | passa (exit 0) | **Não detectado**: o "/1999" quebra o padrão |
| `Decreto nº 3.048, art. 305` | passa | **Não detectado**: o "nº" quebra o padrão |
| `art. 20, § 2º, II, da EC 103` | passa | **Não detectado**: o "§" no meio quebra o padrão |
| `CF, art. 5` | passa | **Falso "na base"**: o arquivo da CF só cobre os arts. 193-204; passa porque o caractere "5" aparece no arquivo |
| `Lei 8.213, art. 54` | passa | **Falso "na base"**: o art. 54 só aparece como título "não pesquisado" |
| `IN 128, art. 580` | **BLOQUEADO** | **Falso "fora da base"**: o artigo está no PDF da base; o resumo `.md` só tem a faixa "578-582" |
| `IN 128, art. 578` | passa | Passa só porque a faixa "578-582" contém o texto "578" |
| `Lei 8.213, art. 142` | BLOQUEADO | Correto: não está na base |

- **Auditoria depois da gravação** (lógica do hook rodada sobre os três arquivos, ignorando
  os marcadores): 44, 20 e 27 citações detectadas. As **únicas** que o hook considera fora
  da base são artigos da IN 128 (577, 580, 548, 575, 576, 592, 595, 208, 233, 321-323,
  581, 587, 207). **Todos foram conferidos por mim no PDF oficial da base.** Os demais
  dispositivos realmente pendentes (Decreto 3.048 — recursos; Regimento Interno do CRPS;
  CPC; Lei 10.259/2001; tabela de carência da Lei 8.213) foram escritos **sem número de
  artigo** ou com o marcador explícito.
- **Mais dois defeitos:**
  1. Uma citação quebrada em duas linhas ("IN" no fim de uma linha, "128" na seguinte) não
     casa com a chave `"IN 128"` do `MAPA_NORMAS`. Resultado: falso "fora da base", e o
     mesmo artigo é tratado de forma diferente conforme a quebra de linha.
  2. O marcador que a própria tarefa sugere, `[DISPOSITIVO A CONFIRMAR NA BASE]`, **não
     ativa a liberação**: o hook exige o texto exato `[DISPOSITIVO A CONFIRMAR]`.
- **Síntese honesta:** o hook confere apenas se o número aparece como texto em algum lugar
  do resumo `.md`. Ele não confirma que o dispositivo citado existe. Ignora os formatos mais
  comuns ("Lei 8.213/1991, art. 52", "Lei nº", citações com "§"), ignora os PDFs da base e
  não intercepta gravações feitas via Bash. **Nesta execução ele não impediu nenhuma
  citação errada e teria impedido uma citação correta (IN 128, art. 580).** A proteção
  real veio da disciplina de marcação e da conferência manual na fonte, não do hook.

### d.4 Script da skill de cálculo falhou sem avisar
`cruza_cnis_ctps.py`, rodado sobre `cnis.txt` e `ctps.txt` deste caso, retornou "Vínculos
CNIS: 0 / Vínculos CTPS: 0 / Tempo total 0a 0m" com **código de saída 0** (sucesso). O
parser exige datas DD/MM/AAAA e o NIT no início de cada linha de vínculo; os documentos do
caso usam MM/AAAA. Um subagente `calculo-previdenciario` que confiasse no código de saída
poderia ter registrado "0 anos". Recontei os períodos com um script à parte: **410 / 417
meses, iguais aos da triagem**.

### d.5 Lacunas reais da base que afetaram este caso
- Decreto 3.048/1999 — capítulo de recursos (prazo; renúncia ao recurso pela ação
  judicial): ausente de `decreto-3.048-1999.md`.
- Regimento Interno do CRPS: ausente. Afeta a possível relevação de intempestividade e a
  competência para determinar reabertura.
  > **Observação (16/10/2026, não altera as conclusões deste relatório):**
  > esta lacuna foi preenchida — o Regimento Interno do CRPS (RICRPS),
  > aprovado pela Portaria MPS nº 125/2026, está em
  > `legislacao/crps/regimento-interno-crps-2026.md`. Ele confirma o prazo
  > de 30 dias (art. 77, mesma regra da IN 128, art. 580), traz a regra de
  > relevação de intempestividade (art. 112, §§ 1º-2º — aplicável só a
  > recursos de benefícios/CNIS, com liquidez e certeza do direito
  > demonstradas) e a renúncia tácita por ação judicial idêntica (art.
  > 86). **Não investigado se a competência para "determinar reabertura"
  > citada acima muda com o Regimento** — ficaria para conferência
  > específica se o caso for reaberto. O Decreto 3.048/1999 continua sem
  > esse capítulo (ele nunca o teve — o Regimento está na Portaria MPS
  > 125/2026, não no Decreto).
- Lei 8.213/1991: arts. 52-56 sem conteúdo confiável; ausentes o art. 29, §§ 7º-9º (fator
  previdenciário), a tabela de transição de carência e a regra do direito adquirido após a
  perda da qualidade de segurado.
- CPC e Lei 10.259/2001 (JEF): fora da base, embora presentes em toda petição de JEF.
- Jurisprudência sobre valor probatório da CTPS e sobre efeitos financeiros de prova nova
  em juízo: ausente.
- IN 128, art. 576-A e IN 208/2026: só a menção no `INDICE.md`; o PDF da base é o texto
  original de 2022.
- **RMI não calculável:** o CNIS dos autos é sintético. O fator previdenciário também não é
  calculável (sem tábua do IBGE na base).

### d.6 Erros encontrados na base (não corrigidos — ver d.2)
Conferência mecânica de `ec-103-2019.md` contra o texto extraível de
`ec-103-2019-oficial.pdf`:
1. **Art. 15, § 3º:** o arquivo diz professor com "25 anos de contribuição (ambos os
   sexos)". O texto oficial diz **25 anos, se mulher, e 30 anos, se homem**.
2. **Art. 26, § 2º, I:** o arquivo descreve o inciso como "hipóteses de professor". O texto
   oficial remete ao inciso II do § 6º do art. 4º, ao § 4º do art. 15, ao § 3º do art. 16
   e ao § 2º do art. 18. São as **cláusulas gerais de valor** das regras de pontos, idade
   progressiva e idade urbana, **não específicas de professor**. Isso importa para todo
   caso de mulher nessas regras (60% + 2 p.p. acima de 15 anos, pelo § 5º). Uma leitura
   apressada do resumo levaria a conclusão errada.

Também registro: o PDF oficial da EC 103 **tem camada de texto** (`pdftotext` funciona). A
ressalva de 09/10/2026, de transcrição "por leitura de imagem", pode ser substituída por
uma conferência mecânica integral.

### d.7 Outras ressalvas
- Os documentos do caso são `.txt`, possivelmente transcrições. As afirmações sobre o que a
  carta "não contém" (fundamento legal, prazo recursal) estão condicionadas à carta
  original.
- O motivo real de 17 dos 70 meses de diferença continua **indeterminado** sem o processo
  administrativo.
- `practice-profile.md` continua com dados de teste; as minutas têm campos
  `[A PREENCHER]`.

---

## Recomendações ao responsável pelo sistema (fora do escopo do caso)

1. Verificar por que a ferramenta de subagente não está disponível ao orquestrador nesta
   modalidade de execução. Sem ela, o desenho multiagente não é exercitado.
2. Dar Bash (ou pelo menos Grep e acesso a `pdftotext`) aos especialistas que precisam
   ler os PDFs da base.
3. Hook: (i) aceitar "/ano", "nº" e "§" no padrão de citação; (ii) checar o número do
   artigo como cabeçalho ou com delimitação, não como texto solto; (iii) indexar também os
   PDFs da base (por exemplo, um `.txt` extraído ao lado de cada PDF); (iv) aplicar o
   marcador por citação, não ao documento inteiro; (v) normalizar espaços e quebras de
   linha na norma; (vi) considerar também gravações feitas via Bash.
4. `cruza_cnis_ctps.py`: terminar com erro quando encontrar 0 vínculos.
5. Completar na base: capítulo de recursos do Decreto 3.048/1999, Regimento Interno do
   CRPS, detalhamento do Livro IV da IN 128 (artigo a artigo, a partir do PDF já presente),
   arts. 29 e 52-56 da Lei 8.213/1991; corrigir os dois pontos de d.6.
6. Alinhar os pré-requisitos de `redacao-peticao` aos nomes de arquivo realmente usados
   nos casos.

---

**RASCUNHO — relatório técnico interno. Nada aqui é peça definitiva.**
