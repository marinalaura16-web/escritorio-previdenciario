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
- **ADI 6096** — possível fonte da inconstitucionalidade da extensão do
  prazo decadencial a indeferimento/cancelamento/cessação (art. 103 da
  Lei 8.213/91, trazida pela MP 871/2019/Lei 13.846/2019). Não incorporado
  à jurisprudência vinculante — falta ler o acórdão oficial do STF.
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

**Próximos blocos:**
5D (restante do bloco 5). Lei 8.742/1993 (LOAS/BPC); textos integrais de
    Lei 13.846/2019, Lei 15.327/2026, Lei 15.371/2026, Lei 12.101/2009
    (CEBAS); decretos 6.214/2007 e 10.410/2020; completar lacunas do
    Decreto 3.048/1999 e da Lei 8.212/1991 (arts. 27, 29, 34-37) sob
    demanda.
6. Substituir os dados de teste em `practice-profile.md` pelos dados reais
   do escritório.
