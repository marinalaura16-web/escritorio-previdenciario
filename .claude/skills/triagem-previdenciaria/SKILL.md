---
name: triagem-previdenciaria
description: Analisa documentos do cliente e gera relatório de viabilidade previdenciária com classificação alta/média/baixa.
---

# Triagem Previdenciária

## Protocolo
1. Leia practice-profile.md.
2. Leia legislacao/INDICE.md.
3. Liste todos os documentos em casos/{id}/documentos/.
4. Extraia dados do CNIS, CTPS, carnês, laudos e carta de indeferimento.
5. Construa linha do tempo de trabalho.
6. Identifique lacunas documentais.
7. Classifique viabilidade: ALTA / MÉDIA / BAIXA (sempre citando dispositivo legal).
8. Gere relatório conforme template do agente triagem-viabilidade.

## Regras
- NUNCA afirme diagnóstico sem CID explícito.
- NUNCA invente períodos de contribuição.
