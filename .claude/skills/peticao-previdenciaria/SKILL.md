---
name: peticao-previdenciaria
description: Gera minuta de petição inicial previdenciária com estrutura completa, fundamentos e pedidos.
---

# Petição Previdenciária

## Pré-requisitos
Verifique se existem: casos/{id}/analises/triagem.md, calculo.md, divergencias-cnis-ctps.md, arquivo-medico.md (se aplicável).

## Protocolo
1. Consulte legislacao/INDICE.md para dispositivos aplicáveis.
2. Cite sempre: norma, artigo, parágrafo, inciso.
3. Se não encontrar na base, marque [DISPOSITIVO A CONFIRMAR].
4. Todo output começa com: "# RASCUNHO — PARA REVISÃO DO ADVOGADO"

## Estrutura
I. DOS FATOS, II. DO DIREITO, III. DA JURISPRUDÊNCIA, IV. DOS PEDIDOS, V. DO VALOR DA CAUSA, PROVAS.

## Regras
- NUNCA invente jurisprudência. Se não tiver certeza, [JURISPRUDÊNCIA A CONFIRMAR].

## Entrega final (regra inviolável 6 do CLAUDE.md, desde 15/10/2026)
Esta skill produz só o conteúdo. A entrega final é sempre um `.docx` gerado
pela skill de conta `tallyta-bione-timbre` (timbrado oficial de Tallyta
Bione Advogados) — ver detalhamento e limitação de ferramentas em
`.claude/agents/redacao-peticao.md`.
