---
name: calculo-tempo-contribuicao
description: Executa cálculos previdenciários determinísticos a partir do CNIS e da CTPS. Cruza os dois documentos para identificar períodos faltantes, divergências de datas, empregadores e remuneração. Retorna tempo líquido e certo, tempo a averbar, carência, cenários de aposentadoria e RMI estimada.
---

# Cálculo de Tempo de Contribuição (CNIS + CTPS)

## Princípio Central
O CNIS é o registro oficial do INSS, mas NÃO é completo. É comum faltarem vínculos antigos, períodos em que o empregador não recolheu e anotações após rescisão. A CTPS é o documento que prova o vínculo empregatício (art. 40 da CLT). Quando a CTPS registra período que o CNIS ignora, esse período pode ser averbado administrativamente ou reconhecido judicialmente.

## Protocolo
1. Leia o CNIS e a CTPS do caso em casos/{id}/documentos/.
2. Se estiverem em PDF, extraia com pdftotext.
3. Execute scripts/cruza_cnis_ctps.py para gerar divergencias.json.
4. Execute scripts/calcula_tempo.py sobre divergencias.json.
5. Gere Relatório de Divergências CNIS x CTPS.
6. Gere Relatório de Cálculo com DOIS cenários: conservador (só CNIS) e com averbação (CNIS + CTPS).

## Regras Invioláveis
1. NUNCA trate CNIS e CTPS como redundantes. São complementares.
2. NUNCA calcule o tempo a averbar como tempo líquido e certo.
3. NUNCA descarte um período só porque não está no CNIS.
4. NUNCA presuma que autônomo/facultativo/segurado especial apareçam na CTPS.
5. NUNCA estime RMI sem aplicar a fórmula correta.
6. Se o CNIS ou a CTPS estiverem ilegíveis, PARE e reporte ao orquestrador.
