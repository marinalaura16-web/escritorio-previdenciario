# Escritório de Direito Previdenciário — Instruções do Projeto

## Contexto
Sistema multiagente para automatizar tarefas de um escritório de Direito Previdenciário brasileiro.

## Agentes Disponíveis
- orquestrador-prev: coordena todos os subagentes
- triagem-viabilidade: analisa documentos e emite viabilidade
- analise-indeferimento: diagnostica negativas do INSS
- calculo-previdenciario: calcula tempo de contribuição e RMI (cruzamento CNIS × CTPS)
- analise-arquivo-medico: organiza registros médicos
- redacao-peticao: gera minutas de petição
- recurso-crps: gera minutas de recurso administrativo
- triagem-clientes: qualifica potenciais clientes

## Regras Invioláveis
1. Todo output é RASCUNHO para revisão do advogado.
2. NUNCA invente jurisprudência. Se não tiver certeza, marque [JURISPRUDÊNCIA A CONFIRMAR].
3. NUNCA afirme diagnóstico médico sem CID explícito no documento.
4. Sempre leia practice-profile.md e legislacao/INDICE.md antes de executar qualquer skill.
5. Mantenha casos organizados em casos/{numero}/

## Base de Legislação
A pasta legislacao/ contém toda a base normativa. Consulte sempre antes de redigir.

## Atualizações Legislativas Relevantes (2025-2026)
- Lei 15.327/2026: veda descontos associativos no INSS
- Lei 15.371/2026: institui salário-paternidade e amplia licença para 20 dias
- Portaria MPS/MF 13/2026: reajuste de 3,90%, teto R$ 8.475,55
- Portaria DIRBEN 1.347/2026: biometria obrigatória
- IN 208/2026: altera regras de benefícios por incapacidade
- STF ADI 6309/DF (03/06/2026, 6x5): declara inconstitucional APENAS
  a idade mínima para aposentadoria especial (art. 19, § 1º, I, a, b, c,
  EC 103/2019). Vedação à conversão e novo cálculo foram mantidos.
- EC 103/2019 (2026): pontos 93 M / 103 H; idade progressiva 59,5 M / 64,5 H

## Estrutura de Casos
casos/{numero}/documentos, casos/{numero}/analises, casos/{numero}/minutas

## Sessão de 21/09/2026

**Blocos concluídos:**
1. Correção do hook `.claude/hooks/anti-alucinacao.py` — passou a reconhecer
   também o formato "art. N da NORMA" (além de "NORMA, art. N"); testes de
   sanidade adicionados (rodam com `python3 anti-alucinacao.py < /dev/null`).
2. Base de jurisprudência vinculante criada em `legislacao/jurisprudencia-vinculante/`:
   súmulas STF, STJ, TNU e temas de repercussão geral do STF, todos com
   verificação por busca (várias correções de número/tema encontradas —
   ver os próprios arquivos).
3. IN PRES/INSS 128/2022 completa (244 páginas, PDF anexado) resumida em
   `legislacao/instrucoes-normativas/in-128-2022.md`, Livros I-VI.
4. Lei 8.213/1991 resumida em `legislacao/leis-ordinarias/lei-8.213-1991.md`,
   ≈93% de cobertura (76 de ~82 artigos do escopo), fontes majoritariamente
   secundárias (sem WebFetch/curl neste ambiente).

**Pendências — Lei 8.213/1991, artigos não localizados:**
Arts. **4º, 5º, 9º, 12, 78 e 79**. Arts. 54-56 ainda sem pesquisa dedicada.

**Achados a verificar antes de uso em petição:**
- ~~**ADI 6096** — possível fonte da inconstitucionalidade da extensão do
  prazo decadencial a indeferimento/cancelamento/cessação (art. 103 da
  Lei 8.213/91, trazida pela MP 871/2019/Lei 13.846/2019). Não incorporado
  à jurisprudência vinculante — falta ler o acórdão oficial do STF.~~
  **CONFIRMADA e incorporada em 24/09/2026 — ver Sessão de 24/09/2026
  abaixo.** Pendências residuais (ementa completa, votação nominal,
  trânsito em julgado, modulação) seguem `[A CONFIRMAR NA FONTE OFICIAL]`
  em `legislacao/jurisprudencia-vinculante/adi-6096-2021-resumo.md`.
- Toda a base populada nesta sessão (Lei 8.213, IN 128, súmulas, temas,
  EC 103 art. 26) foi montada **sem acesso a WebFetch/curl** — fontes
  majoritariamente secundárias. Conferir na fonte oficial antes de citar
  em petição real.

**Próximos blocos:**
5. Completar demais leis (Lei 8.212/1991 — Custeio; Lei 8.742/1993 — LOAS/BPC;
   textos integrais de Lei 13.846/2019, Lei 15.327/2026, Lei 15.371/2026;
   decretos 3.048/1999, 6.214/2007, 10.410/2020).
6. Substituir os dados de teste em `practice-profile.md` ("Escritório: Teste",
   "OAB: Teste") pelos dados reais do escritório.

## Sessão de 23/09/2026

**Blocos concluídos:**
5A. EC 103/2019 ampliada (`legislacao/emendas-constitucionais/ec-103-2019.md`):
    arts. 19 (especial, com nota `[INCONSTITUCIONAL - ADI 6309]` restrita às
    alíneas a/b/c do §1º,I), 15-18/20-21 (regras de transição, numeração
    corrigida — não é bloco contínuo), 22-25 (pensão por morte, conversão de
    tempo especial), 27/35/36. Pendentes: arts. 4º-8º, 28-34, segmentação
    fina de 1-3/9-18.
5B. Decreto 3.048/1999 (`legislacao/decretos/decreto-3.048-1999.md`) — **novo**:
    - Cobertura: esqueleto presente nos 8 benefícios pedidos (incapacidade
      permanente, idade, especial, incapacidade temporária, pensão por
      morte, auxílio-reclusão, auxílio-acidente, salário-família,
      salário-maternidade) + segurados/dependentes (arts. 9-33).
    - Lacunas (parágrafos/incisos complementares, não os artigos-âncora):
      arts. 12-15, 18, 20-31, 45-50, 52-63, 67, 69-70, 73-80, 82-92, 94-103,
      107, 109-115, 119-120, além do detalhamento linha a linha dos
      Anexos I-IV (só a estrutura geral foi mapeada).
    - **Status: aceitável para v1 — completar sob demanda**, não bloqueia uso.
    - **Anexo IV, código 3.0.1 (agentes biológicos): CONFIRMADO** por múltiplas
      fontes secundárias, consistente com o uso ativo em `casos/2026-001/`.
    - **Nenhuma marcação `[INCONSTITUCIONAL - ADI 6309]` se aplica ao
      Decreto** — a ADI 6309/DF atingiu apenas o art. 19, §1º, I, da
      EC 103/2019 (idade mínima); os arts. 64-70 do Decreto (especial) não
      têm exigência própria de idade mínima.
    - Numeração "100-120" pedida originalmente para cálculo/decadência/
      prescrição **não corresponde à estrutura real do Decreto** — o
      conteúdo real está nos arts. 32-33 (cálculo) e 347-348
      (decadência/prescrição, 348 só estrutural).

5C. Lei 8.212/1991 (Custeio) — **concluído** nesta sessão
    (`legislacao/leis-ordinarias/lei-8.212-1991.md`, **novo**):
    - Cobertura: 23 artigos/dispositivos com conteúdo nas 5 faixas
      priorizadas — segurados/empresa (arts. 12-15 completos; art. 11 tem
      conteúdo, mas de tema diverso — ver correção de escopo abaixo),
      contribuições (20, 21, 22, 22-A, 23, 24, 25, 26, 28, 30 — pendentes
      27 e 29), fiscalização/obrigações acessórias (32-33 — pendentes
      34-37), arrecadação e recolhimento (43-47, completo) e isenções
      (55-56, completo).
    - **Correções de escopo (o stub anterior do `INDICE.md` estava
      incorreto):** art. 11 não é sobre segurados (é orçamento da
      Seguridade Social); art. 13 não é "segurados facultativos" (é
      exclusão de servidor/militar do RGPS por RPPS); art. 14 não é
      "dependentes" (é o segurado facultativo — Lei 8.212/91 não regula
      dependentes); arts. 32-37 não são "salário-de-contribuição" (essa
      definição está no art. 28) — são fiscalização/obrigações acessórias.
    - **Achado relevante:** arts. 45-46 (decadência/prescrição de 10 anos
      das contribuições) têm eficácia **afastada pelo STF, Súmula
      Vinculante 8** — aplicam-se os prazos de 5 anos do CTN (arts.
      173/174). Não incorporado ainda à jurisprudência vinculante da base
      (pendência, junto com RE 595.838 — art. 22, IV, cooperativas — e RE
      611.601 — art. 22-A, agroindústria).
    - Art. 55 confirmado como **revogado** pela Lei 12.101/2009 (CEBAS).
    - Pendências de conteúdo: arts. 27, 29, 34, 35, 36 e 37.

5E. Jurisprudência — RE 595.838 e RE 611.601 (`legislacao/jurisprudencia-
    vinculante/temas-repercussao-geral-stf.md`) e Lei 8.742/1993 —
    LOAS/BPC (`legislacao/leis-ordinarias/lei-8.742-1993.md`, **novo**) —
    **concluído** nesta sessão:
    - **RE 595.838 = Tema 166** (Rel. Min. Dias Toffoli, j. 23/04/2014):
      inconstitucionalidade da contribuição de 15% sobre serviços de
      cooperativas de trabalho (art. 22, IV, Lei 8.212/91). **RE 611.601 =
      Tema 281** (mesmo relator, Sessão Virtual 09-16/12/2022):
      constitucionalidade da contribuição substitutiva da agroindústria
      (art. 22-A, Lei 8.212/91). **Nenhum dos dois é Tema 32 nem trata de
      imunidade/CEBAS de entidades beneficentes** — o usuário havia
      levantado essa dúvida corretamente; a matéria de imunidade/CEBAS
      pertence a um terceiro precedente, identificado incidentalmente:
      **Tema 32/RE 566.622** (reserva de lei complementar para requisitos
      de imunidade de entidades beneficentes), **não incorporado** como
      entrada própria (fora do escopo desta tarefa) — fica como pendência.
    - Lei 8.742/1993: 7 artigos cobertos com conteúdo individualizado
      (1-4, 20, 21, 22). Art. 20 (BPC) é o mais detalhado do arquivo:
      caput, definição de pessoa com deficiência pós-LBI, critério de
      renda com evolução legislativa completa até a Lei 14.176/2021,
      impedimento de longo prazo (2 anos), avaliação biopsicossocial/CIF,
      vedação de acumulação. Arts. 23-40 cobertos só em resumo temático
      (fora de escopo prioritário).
    - **Correção de escopo:** o **art. 21** da Lei 8.742/93 **NÃO** é
      "benefícios eventuais" (premissa original da tarefa) — é a
      **revisão bienal do BPC**; benefícios eventuais estão no **art.
      22**.
    - **Achado a verificar:** critério legal de renda do BPC é 1/4 do
      salário-mínimo (art. 20, § 3º; "igual ou inferior" desde a Lei
      14.176/2021), com ampliação condicionada a 1/2 SM pelo art. 20-B
      (mesma lei). O STF, Tema 27 (RE 567.985, já na base), afasta a
      exclusividade desse critério objetivo. Há indícios **não
      confirmados** de tema repetitivo do STJ (possivelmente Tema 185) e
      de prática de tribunais aplicando 1/2 SM por construção
      jurisprudencial — `[JURISPRUDÊNCIA A CONFIRMAR]`, não incorporado
      como entrada própria à base vinculante.

5F. Decreto 6.214/2007 (BPC), Lei 13.846/2019, Lei 15.327/2026 e Lei
    15.371/2026 — **concluído** nesta sessão (23-24/09/2026):
    - **Decreto 6.214/2007** (`legislacao/decretos/decreto-6.214-2007.md`,
      **novo**): correção estrutural essencial — o corpo do próprio
      Decreto tem apenas 4 artigos; todo o conteúdo do BPC (as 4 faixas
      pedidas) está no **Regulamento anexo, com numeração própria**.
      Cobertura: 13 artigos do Regulamento com conteúdo individualizado
      (1, 4, 9, 16, 20, 25, 39-43, 45), mais 2 achados sem número exato
      resolvido (vedação de acumulação; cadastro no CadÚnico). **Não
      ficou completo em nenhuma das 4 faixas pedidas** (20-40% de
      cobertura por faixa). Dois pontos de incerteza estrutural não
      resolvidos: (i) se o critério de renda do art. 20 do Regulamento já
      reflete a Lei 14.176/2021 ("igual ou inferior" a 1/4 SM); (ii) se a
      revisão bienal está só no art. 42 ou também nos arts. 24-25
      (possível sobreposição entre achados de fontes distintas).
    - **Lei 13.846/2019** (`legislacao/leis-ordinarias/lei-13.846-2019.md`,
      **novo**): arts. 1º e 2º da própria Lei (Programa Especial
      "Pente-Fino" e Programa de Revisão de Benefícios por Incapacidade),
      mais índice cruzado das alterações à Lei 8.213/91 já documentadas
      naquele arquivo. **Achado prioritário: convergência sensivelmente
      reforçada sobre a ADI 6096** (STF) — identificado nesta sessão que o
      dispositivo objeto da ação é o **art. 24 da Lei 13.846/2019**
      (alteração ao art. 103, caput, da Lei 8.213/91), com indicação de
      julgamento por maioria de 6x5 e um registro de acórdão de embargos
      de declaração (lexml.gov.br) de 14/06/2021. **Ainda não incorporada
      à jurisprudência vinculante** — nenhuma fonte oficial do STF lida
      diretamente. Recomenda-se que a próxima sessão consulte
      portal.stf.jus.br, processo ADI 6096, como prioridade.
    - **Lei 15.327/2026** (`legislacao/leis-ordinarias/lei-15.327-2026.md`,
      **novo**): os 4 temas pedidos (vedação de descontos associativos,
      busca ativa a lesados, proteção de dados/LGPD, regras de consignado
      biométrico) têm conteúdo confirmado por convergência, mas **sem
      atribuição segura a número de artigo** — lei muito recente (jan/2026),
      cobertura por fontes secundárias naturalmente menor. Nenhuma ADI
      localizada contra esta Lei.
    - **Lei 15.371/2026** (`legislacao/leis-ordinarias/lei-15.371-2026.md`,
      **novo**): **correção de escopo relevante** — a ampliação da
      licença-paternidade é **escalonada em 3 etapas (10 dias em 2027, 15
      em 2028, 20 apenas em 2029)**, não um salto direto a 20 dias em 2027
      como o registro anterior desta base sugeria. Arts. 1º-3º da própria
      Lei e alteração ao art. 71-B da Lei 8.213/91 identificados.
      Pendência relevante: não confirmado se há carência para o
      salário-paternidade de contribuinte individual/facultativo/especial.
    - **Decreto 10.410/2020 (RPPS): decisão deliberada de não incorporar**
      a esta base (escritório atua em RGPS, não RPPS) — registrado no
      `INDICE.md` como "não incorporado por despriorização", não como
      pendência esquecida.
    - **`MAPA_NORMAS` do hook `.claude/hooks/anti-alucinacao.py` ampliado**
      com as entradas `LEI 13.846` e `DECRETO 6.214` (seguindo o padrão já
      existente); testes de sanidade continuam passando
      (`python3 anti-alucinacao.py < /dev/null`).

**Próximos blocos:**
6. Completar lacunas do Decreto 6.214/2007 sob demanda (arts. 2-3, 5-8,
   10-15, 17-19, 21-23, 26-28, 32-35, 37-38, 44 do Regulamento, e
   resolução do conflito entre os achados sobre revisão bienal — arts.
   24-25 x 42); confirmar na fonte oficial do STF a ADI 6096 e, se
   confirmada, incorporá-la a `jurisprudencia-vinculante/`; Lei 12.101/2009
   (CEBAS); completar lacunas do Decreto 3.048/1999 e da Lei 8.212/1991
   (arts. 27, 29, 34-37), e da Lei 8.742/1993 (arts. 23-40 artigo a
   artigo, art. 25, demais parágrafos do art. 20) sob demanda; confirmar
   número exato dos parágrafos do art. 115 da Lei 8.213/91 inseridos pela
   Lei 15.327/2026 e o teor das alterações desta à Lei 8.212/1991 e à Lei
   11.770/2008 pela Lei 15.371/2026.
7. Incorporar formalmente à jurisprudência vinculante: Súmula Vinculante 8
   do STF (Lei 8.212/91, arts. 45-46), Tema 32/RE 566.622 (imunidade de
   entidades beneficentes), ~~ADI 6096 (decadência, Lei 13.846/2019 — ver
   Bloco 5F)~~ **concluído em 24/09/2026, ver abaixo** e, se confirmado, o
   tema do STJ sobre o critério de renda do BPC (1/4 x 1/2 SM).
8. Substituir os dados de teste em `practice-profile.md` pelos dados reais
   do escritório.

## Sessão de 24/09/2026

**Bloco concluído — pesquisa e documentação da ADI 6096/DF (decadência,
art. 103 da Lei 8.213/91):**

Tarefa de pesquisa jurídica de alta prioridade, motivada pelo achado
pendente registrado nas sessões de 21/09 e 23/09/2026 (ver "Achados a
verificar" acima e `leis-ordinarias/lei-13.846-2019.md`, Bloco 4). Resumo:

1. **Pesquisa via WebSearch (sem WebFetch/curl neste ambiente, mesma
   limitação já documentada nas sessões anteriores)** localizou, pela
   primeira vez nesta base, **páginas do próprio domínio `stf.jus.br`**
   sobre a ADI 6096: a notícia oficial do julgamento
   (`noticias.stf.jus.br` e espelho em `portal.stf.jus.br`) e a página de
   andamento processual (`portal.stf.jus.br/processos/detalhe.asp?incidente=5647251`).
   Também foram localizadas citações de inteiro teor do acórdão (mérito e
   embargos de declaração) via Jusbrasil, e o registro do acórdão no
   LexML (serviço público federal).
2. **Confirmado:** a ADI 6096/DF (Rel. Min. Edson Fachin, requerente CNTI,
   número único 0018723-17.2019.1.00.0000) julgou parcialmente procedente,
   por maioria de 6x5, declarando a inconstitucionalidade do **art. 24 da
   Lei 13.846/2019**, que estendia a decadência decenal do **art. 103,
   caput, da Lei 8.213/91** às hipóteses de **indeferimento, cancelamento e
   cessação** de benefício. Efeito: a decadência de 10 anos **volta a valer
   apenas para a revisão de ato de concessão** de benefício já deferido.
   Embargos de declaração foram opostos e **rejeitados por unanimidade**
   em 14/06/2021 (DJe 24/06/2021), sem indício de terem tratado de
   modulação de efeitos.
3. **Documentação criada/atualizada:**
   - **Novo:** `legislacao/jurisprudencia-vinculante/adi-6096-2021-resumo.md`,
     no mesmo padrão estrutural de `adi-6309-2026-resumo.md`.
   - **Atualizado:** `legislacao/leis-ordinarias/lei-8.213-1991.md` (seção
     "Prescrição e Decadência — Art. 103" e tabela de dispositivos alterados
     por outras normas/jurisprudência).
   - **Atualizado:** `legislacao/leis-ordinarias/lei-13.846-2019.md` (Bloco
     4, com nota de confirmação ao final).
   - **Atualizado:** `legislacao/INDICE.md` (nova entrada na seção 8 —
     Jurisprudência Vinculante — e correção das referências pendentes nas
     seções 4 e "Pendências desta base").
4. **Pendências remanescentes** (não bloqueiam o uso do achado principal,
   mas exigem cautela e conferência antes de petição real): ementa oficial
   completa, composição nominal exata da votação 6x5, confirmação
   definitiva de trânsito em julgado, confirmação definitiva de ausência de
   modulação de efeitos, e redação literal exata (byte a byte, Planalto) do
   art. 103, caput, hoje vigente. Ver `adi-6096-2021-resumo.md` para o
   detalhamento.
5. **Cruzamento com `casos/2026-001/`:** lidos integralmente `triagem.md`,
   `calculo.md`, `calculo-rmi.md` e `peticao-inicial-DRAFT.md`. **Não há,
   neste caso, nenhuma questão de decadência de indeferimento/cancelamento/
   cessação de benefício** — o caso trata de um **primeiro requerimento**
   de aposentadoria especial (tempo de contribuição/exposição), sem DER
   nem indeferimento anterior conhecido (o próprio `triagem.md`, item L11,
   e a minuta de petição, item I.6, já registram expressamente a ausência
   de requerimento administrativo pretérito confirmado). A única menção ao
   art. 103 no caso é à **prescrição quinquenal** (parágrafo único, sobre
   parcelas retroativas), matéria distinta da decadência decenal do caput
   e não afetada pela ADI 6096. **Nenhum arquivo do caso 2026-001 foi
   alterado** por esta tarefa, por não haver fato relevante a registrar.

**Bloco concluído — população da Constituição Federal, Título VIII, arts.
193 a 204 (Bloco 5E):**

1. **Novo arquivo:** `legislacao/constituicao/cf-1988-seguridade-social.md`
   — cobre os 12 pontos do escopo pedido (arts. 193, 194, 195, 196-200
   em conjunto/resumo, 201, 202, 203, 204), montado **sem WebFetch/curl**
   (mesma limitação de ambiente das demais normas desta base) — fontes
   majoritariamente secundárias, com boa proporção de páginas do próprio
   domínio `portal.stf.jus.br` e de estudos da Consultoria Legislativa da
   Câmara dos Deputados (`bd.camara.leg.br`).
2. **Art. 201 (o mais crítico): ficou com 13 dos 16 parágrafos numerados
   cobertos, mais o caput (incisos I-V) e o § 9º-A** — apenas os **§§ 12,
   13 e 14 ficaram `[NÃO LOCALIZADO - PENDENTE]`** (a pesquisa não
   confirmou a premissa original de que esses três parágrafos tratariam de
   salário-maternidade/pensão por morte/cálculo — esses benefícios estão,
   na verdade, nos incisos II, IV e V do próprio *caput*, e o cálculo da
   pensão por morte está nos arts. 23-24 da EC 103/2019, já documentados).
   Foram encontradas e documentadas **13 correções de escopo** em relação
   à numeração presumida originalmente para os parágrafos do art. 201 (ver
   tabela e lista completa no próprio arquivo) — entre elas: o piso está
   no § 2º (não no § 4º); a distinção urbano/rural está no § 7º, II (não
   no § 1º); o § 7º não foi extinto pela EC 103/2019 (é a regra definitiva
   de idade); o § 8º trata de professores, não de aposentadoria especial;
   e a acumulação de benefícios está no § 15 (não no § 6º).
3. **Instrução condicional 1 (marcação `[INCONSTITUCIONAL - ADI 6309]` no
   § 8º do art. 201) — NÃO aplicada, por verificação.** A pesquisa
   confirmou que o § 8º trata da redução de idade para professores, sem
   qualquer relação com a aposentadoria especial por agentes nocivos. Mais
   ainda: **a idade mínima (55/58/60 anos) efetivamente invalidada pela ADI
   6309/DF não está em nenhum parágrafo do art. 201 da CF** — está apenas
   no art. 19, § 1º, I, a/b/c, da própria EC 103/2019, já corretamente
   marcado em `ec-103-2019.md`. O art. 201, § 1º, II (autorização
   constitucional genérica para a aposentadoria especial, sem número de
   idade), recebeu uma **nota de cruzamento**, não uma marcação de
   inconstitucionalidade — para não estender o alcance da decisão do STF
   além do que ela realmente abrange.
4. **Instrução condicional 2 (marcação `[ADMINISTRATIVO 6096]` no caput do
   art. 201) — NÃO criada.** Esse marcador não existe no esquema padrão do
   projeto e não foi adotado. A pesquisa confirmou que o *caput* do art.
   201 trata apenas da estrutura geral do RGPS, sem relação com prazos
   decadenciais; a ADI 6096/DF decidiu sobre o art. 103, *caput*, da Lei
   8.213/91 (norma infraconstitucional), com fundamento no art. 6º da CF
   (fora do Título VIII). O *caput* do art. 201 recebeu apenas uma **nota
   de cruzamento**, deixando claro que a relação é indireta e que nenhuma
   alteração do texto constitucional decorre dessa ADI.
5. **Art. 203 (BPC): ficou completo** — caput e incisos I a VI (o VI,
   redução de vulnerabilidade socioeconômica, incluído por emenda mais
   recente, com confiança um pouco menor), com destaque para o **inciso V**
   (matriz constitucional do BPC) e cruzamento direto com `lei-8.742-1993.md`,
   art. 20, e com o Tema 27/RE 567.985 já na base de jurisprudência
   vinculante.
6. **Marcações finais no arquivo:** predominam `[FONTE SECUNDÁRIA - CONFERIR
   NO PLANALTO]` (grande maioria dos dispositivos) e `[NÃO LOCALIZADO -
   PENDENTE]` (pontual — arts. 201 §§ 12-14, alguns incisos do art. 194,
   parágrafos de detalhe dos arts. 195 e 198-200, § 2º do art. 202,
   parágrafo único do art. 204); `[ALTERADO PELA EC 103/2019]` aplicada aos
   §§ 7º, 8º, 9º-A e 16 do art. 201. **Nenhuma marcação
   `[INCONSTITUCIONAL - ADI 6309]` foi aplicada em nenhum dispositivo deste
   arquivo** (ver item 3 acima).
7. **`legislacao/INDICE.md` atualizado:** seção 1 (Constituição Federal)
   reescrita com a numeração corrigida e as notas de cruzamento; o stub
   antigo (com a numeração incorreta) foi preservado, riscado, dentro de um
   `<details>` apenas como histórico.
8. **Hook `anti-alucinacao.py`:** testes de sanidade continuam passando
   (`python3 anti-alucinacao.py < /dev/null` → "TODOS OS TESTES PASSARAM").
   Nenhuma alteração foi necessária no `MAPA_NORMAS` (a entrada `"CF"` já
   apontava para o arquivo criado nesta sessão).
9. **Pendências residuais** (não bloqueiam o uso do arquivo, mas exigem
   cautela): art. 201, §§ 12-14 (conteúdo real não localizado); arts. 195
   e 198-200 (parágrafos de detalhe fora do escopo priorizado); art. 202,
   § 2º (redação incompleta); art. 204, parágrafo único (não confirmado);
   terminologia exata ("pessoa com deficiência" vs. "portadora de
   deficiência") do art. 203, incisos IV-V, a confirmar no Planalto. Ver a
   lista completa em `constituicao/cf-1988-seguridade-social.md`, seção
   "Pendências desta apuração".

### Encerramento da sessão (24/09/2026)

**Estado geral: sistema estruturalmente completo.** Os blocos fundacionais
de legislação (CF/88, EC 103/2019, Lei 8.213/1991, Lei 8.212/1991, Lei
8.742/1993, Decretos 3.048/1999 e 6.214/2007, IN 128/2022, Leis 13.846/2019,
15.327/2026 e 15.371/2026) e a jurisprudência vinculante crítica (ADI
6309/DF e ADI 6096/DF, súmulas STF/STJ/TNU, temas de repercussão geral)
estão populados e commitados. Todo o conteúdo segue com o aviso padrão de
proveniência (fontes majoritariamente via WebSearch, sem WebFetch/curl
neste ambiente) — nada foi conferido byte a byte no Planalto/STF.

**Correção de numeração aplicada nesta sessão:** 13 correções de escopo na
numeração dos parágrafos do art. 201 da CF em relação à lista originalmente
sugerida (ver bloco "Bloco concluído — população da Constituição Federal"
acima, item 2).

**Pendências sob demanda** (não bloqueiam o uso da base, tratar quando
necessário):
- Parágrafos residuais do art. 201 da CF (§§ 12-14) e demais lacunas de
  detalhe da CF (arts. 195, 198-200, 202 §2º, 204 parágrafo único).
- Lei 12.101/2009 (CEBAS) — texto integral ainda não incorporado; e Tema
  32/RE 566.622 (imunidade de entidades beneficentes) — identificado mas
  não incorporado como entrada própria à jurisprudência vinculante.
- Tema do STJ sobre o critério de renda do BPC (1/4 x 1/2 SM) — indício
  não confirmado (possivelmente Tema 185), não incorporado.
- `practice-profile.md` — dados de teste ("Escritório: Teste", "OAB:
  Teste", "Advogado responsável: Teste") ainda não substituídos pelos
  dados reais do escritório; usuária optou por não fornecê-los nesta
  sessão (24/09/2026).
- Modulação de efeitos da ADI 6309/DF — aguardando confirmação na fonte
  oficial do STF (ver `adi-6309-2026-resumo.md`).
- Lacunas residuais já registradas nos Blocos 5B/5C/5F (Decreto 3.048/1999,
  Lei 8.212/1991 arts. 27/29/34-37, Decreto 6.214/2007, Lei 8.742/1993
  arts. 23-40 artigo a artigo).

**Padrão identificado nesta sessão (relevante para o método de trabalho
deste projeto):** as listas de numeração de artigos/parágrafos fornecidas
pela usuária nas instruções de tarefa apresentam erros recorrentes — não é
um caso isolado. Ocorreu em praticamente todo bloco desta sessão: Decreto
3.048/1999 ("arts. 100-120" → na verdade arts. 32-33 e 347-348), Lei
8.212/1991 (arts. 11/13/14 e 32-37 com tópicos errados), Lei 8.742/1993
(art. 21 presumido "benefícios eventuais", na verdade é revisão bienal),
RE 611.601 (presumido Tema 32/CEBAS, na verdade é Tema 281/agroindústria),
Lei 15.371/2026 (20 dias presumidos imediatos, na verdade escalonados até
2029), e CF/88 art. 201 (13 correções de parágrafo em um único artigo).
**Regra de trabalho consolidada: nunca aplicar a numeração ou o
enquadramento temático sugerido por instrução sem verificação prévia via
pesquisa — mesmo quando a instrução vem com alta confiança aparente.
Divergência confirmada deve ser documentada explicitamente, nunca forçada
para encaixar na expectativa original.**

## Sessão de 24/09/2026 — Bloco 7 (Interface Streamlit)

**Tarefa de engenharia de software (não pesquisa jurídica): criada a
interface `app/` (Streamlit) para o escritório usar o sistema sem precisar
do Claude Code.**

- `app/streamlit_app.py`, `app/anthropic_client.py`, `app/prompts.py`,
  `app/pdf_utils.py`, `app/requirements.txt`, `app/.streamlit/config.toml`,
  `app/.streamlit/secrets.toml.example`, `app/README.md`.
- O app chama a **API Anthropic diretamente** (SDK `anthropic`, sem Claude
  Agent SDK) — monta um prompt consolidado com o prompt do
  `orquestrador-prev`, dos subagentes `triagem-viabilidade`,
  `calculo-previdenciario`, `analise-arquivo-medico`, a skill
  `calculo-tempo-contribuicao` e o contexto do escritório
  (`practice-profile.md` + resumo de `legislacao/INDICE.md`), pede uma
  resposta em JSON único (triagem/calculo/arquivo_medico/peticao) via
  streaming (`thinking: adaptive`, `effort: high`), com a Regra Inviolável 1
  reforçada explicitamente no prompt.
- **Correção de IDs de modelo:** os IDs pedidos originalmente
  ("claude-sonnet-4-5", "Opus 4.1") não existem na API Anthropic atual —
  usados `claude-sonnet-5` e `claude-opus-5` (vigentes) em todo o código.
- Teste local: `pip install -r app/requirements.txt` e
  `streamlit run app/streamlit_app.py` **funcionaram neste ambiente**
  (servidor respondeu HTTP 200); `python3 -m py_compile app/*.py` também
  passou. Nenhum caso real foi processado no teste (não houve chamada à API
  Anthropic).
- Pendências/decisões documentadas em `app/README.md`: lista de 9
  benefícios do selectbox foi inferida de `practice-profile.md` (a
  enumeração original de 9 itens não estava disponível neste contexto —
  conferir se corresponde ao esperado); upload único multi-arquivo em vez
  de campos segregados por tipo de documento; "copiar para área de
  transferência" via `st.code()` (sem componente nativo de clipboard no
  Streamlit); link de documentação na sidebar aponta para
  `github.com/marinalaura16-web/escritorio-previdenciario/blob/main/app/README.md`
  (ajustar se o branch padrão do repositório não for `main`).
- `.gitignore` (raiz) atualizado com `app/.streamlit/secrets.toml`
  (`__pycache__/` e `*.pyc` já estavam presentes).

## Status do Sistema (atualizado em 24/09/2026)

### ✅ Funcional em produção

- **8 agentes** rodando via Claude Code Web (orquestrador + 7 especialistas)
  — confirmado: 8 arquivos em `.claude/agents/`.
- **8 skills** modulares (legislação, cálculo, triagem, indeferimento,
  arquivo médico, petição, recurso, WhatsApp) — confirmado: 8 pastas em
  `.claude/skills/`.
- **Hook anti-alucinação** com regex corrigido (reconhece "Lei X, art. Y"
  e "art. Y da Lei X").
- **Base legislativa** completa: CF/88, EC 103/2019, Lei 8.213/91, Lei
  8.212/91, Lei 8.742/93, Decreto 3.048/99, Decreto 6.214/07, IN 128/2022,
  ADI 6309, ADI 6096 — todos os arquivos confirmados presentes em
  `legislacao/`.
- **Jurisprudência vinculante**: STF, STJ, TNU, temas de repercussão
  geral.
- **Tabelas de cálculo**: INPC (**570 competências**, 03/1979–08/2026) +
  Tetos RGPS (**444 competências**, 01/1990–12/2026).
- **App web Streamlit** — URL informada pela usuária:
  https://escritorio-previdenciario-5jbsbpgq4zuxzp4mkqbb9p.streamlit.app
  (não verificada nesta sessão — `curl`/WebFetch para hosts externos não
  estão disponíveis neste ambiente, mesma limitação documentada em toda a
  base de legislação).

**Duas correções em relação ao rascunho original desta seção:**
1. **Tabelas de INPC e Tetos RGPS estavam trocadas** — o rascunho atribuía
   "444 competências" ao INPC; na verdade o INPC tem 570 linhas de dados
   (`wc -l` confirma 571 linhas no arquivo, menos o cabeçalho) e é a
   tabela de Tetos RGPS que tem 444.
2. **Não há caso "2026-003" processado com sucesso neste repositório.**
   `casos/2026-003` nunca existiu aqui (já verificado em sessão anterior
   via `git log --all`). O caso de teste "José Carlos Teste da Silva" que
   a usuária compartilhou (como arquivo `.md` baixado do app) foi gerado
   pelo próprio app Streamlit com o número **"2026-005"** (visível no
   cabeçalho do arquivo), rodado em outro ambiente (local ou a instância
   do Streamlit Cloud) — nunca foi commitado a este repositório, e
   também não pode ser chamado de "processado com sucesso" sem ressalva:
   o próprio relatório gerado documentava múltiplas lacunas/pendências
   (CNIS truncado, CTC ausente, inconsistência de tempo de contribuição
   entre o INSS e o cálculo do escritório) — foi um teste funcional
   bem-sucedido do fluxo técnico (triagem → cálculo → arquivo médico →
   petição em uma única chamada), não uma análise de mérito fechada.
   Além disso, durante a verificação desta tarefa, uma pasta
   `casos/2026-002/` vazia foi encontrada neste repositório — criada
   acidentalmente por um teste automatizado (`AppTest`) da sessão
   anterior, não por um caso real — e foi removida.

### ⚠️ Limitações conhecidas

- App Streamlit é **síncrono** (bloqueia a tela durante análise — 3-5
  min) — decisão deliberada desta sessão, após remover a versão anterior
  em background (`threading` + estado dividido entre `st.session_state` e
  um dict de módulo) por ter causado um loop de reruns em produção.
- App **não persiste** casos entre reinicializações do servidor (nem, no
  caso do Streamlit Cloud, entre deploys — o sistema de arquivos do
  container não é o mesmo deste repositório Git).
- Citações legais ainda apresentam `[A CONFIRMAR]` / `[FONTE SECUNDÁRIA -
  CONFERIR NO PLANALTO]` em vários pontos — não é um problema do app em
  si, é o estado real da base (nada foi conferido byte a byte no Planalto
  em nenhuma norma desta sessão, dada a ausência de WebFetch/curl neste
  ambiente).
- Falta autenticação (app é público por enquanto).
- Dados de teste ficam no servidor da Streamlit Cloud (atenção LGPD) —
  válido também para qualquer dado real de cliente usado em teste.

### 🎯 Próximos passos

1. Refinar o prompt do app para injetar EC 103 com texto exato.
2. Adicionar CNIS completo do caso real como exemplo de contexto.
3. Reavaliar execução em background (thread ou `@st.cache_resource`) só
   depois que o fluxo síncrono atual estiver validado em produção por um
   período razoável — ver "Limitações conhecidas" acima sobre por que a
   tentativa anterior foi revertida.
4. Implementar autenticação simples (senha) para uso interno.
5. Migrar para servidor brasileiro quando o escritório validar o app.
