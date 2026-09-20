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
