---
name: analise-arquivo-medico
description: Organiza registros médicos, extrai diagnósticos, medicações, exames e achados funcionais, identifica lacunas probatórias.
---

# Análise de Arquivo Médico

## Protocolo
1. Liste documentos médicos em casos/{id}/documentos/.
2. Para cada documento, extraia: Data, Profissional, CRM, Diagnóstico, CID, Medicação, Exame, Achado Funcional.
3. Construa tabela cronológica.
4. Identifique lacunas: período sem acompanhamento, diagnóstico sem CID, incapacidade não declarada, exame sem laudo.
5. Avalie força probatória: ALTA / MÉDIA / BAIXA.

## Regras
- NUNCA afirme diagnóstico sem CID explícito.
- NUNCA interprete exame sem laudo.
