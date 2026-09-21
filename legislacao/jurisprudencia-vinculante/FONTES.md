# Fontes — Base de Jurisprudência Vinculante

## Data desta consolidação

21/09/2026.

## Escopo

Este arquivo documenta as fontes usadas para construir os quatro arquivos de
jurisprudência publicados nesta mesma pasta em 21/09/2026:

- `sumulas-stf.md`
- `sumulas-stj.md`
- `sumulas-tnu.md`
- `temas-repercussao-geral-stf.md`

Não documenta os arquivos da ADI 6.309/DF (`adi-6309-2026-resumo.md`,
`adi-6309-2026-certidao-julgamento.md`, `adi-6309-2026-andamento.pdf`,
`adi-6309-2026-voto-barroso.pdf`), que têm proveniência própria já registrada
em `adi-6309-2026-resumo.md` (baseados em certidão de julgamento e
andamento processual oficiais do STF, salvos localmente).

## Nota de limitação — leia antes de usar qualquer súmula/tese em petição

> Esta é a mesma limitação já documentada em
> `legislacao/emendas-constitucionais/ec-103-2019.md` e em
> `legislacao/jurisprudencia-vinculante/adi-6309-2026-resumo.md`. Repetida
> aqui porque este arquivo consolida quatro documentos novos, não apenas um.

**Este ambiente não possui ferramenta de navegação/download de página web**
(sem WebFetch; acesso de rede via `curl` bloqueado por permissão). Toda a
pesquisa para os quatro arquivos acima foi feita exclusivamente por busca
textual (WebSearch), que retorna resumos e trechos de páginas — nunca o HTML
completo de uma página oficial. Isso significa que:

1. **Nenhum texto de súmula ou tese foi conferido byte a byte contra a
   fonte primária** (portal.stf.jus.br, stj.jus.br/scon.stj.jus.br,
   cjf.jus.br). O que foi possível fazer foi cruzar múltiplas fontes
   secundárias independentes (buscadores jurídicos, sites de doutrina,
   notícias oficiais dos próprios tribunais) e verificar convergência entre
   elas.
2. Quando as fontes convergiam com segurança razoável em torno de uma
   redação, essa redação foi reproduzida entre aspas, com a fonte e a data
   de consulta indicadas.
3. Quando as fontes divergiam entre si, ou quando não foi possível
   encontrar a redação literal completa, o trecho foi marcado
   `[A CONFIRMAR NA FONTE OFICIAL]` (ou, para dispositivos legais citados
   incidentalmente, `[DISPOSITIVO A CONFIRMAR]`), em vez de arriscar uma
   reprodução de memória.
4. **Nenhuma súmula ou tese foi citada apenas porque "geralmente se sabe
   isso"** — cada uma foi pesquisada individualmente e teve seu número,
   tribunal e objeto conferidos antes de ser incluída. Esse processo revelou
   várias vezes que o número sugerido não correspondia ao tema
   originalmente suposto (ver seção "Descobertas" abaixo) — o mesmo tipo de
   erro que já havia ocorrido nesta base com "STF, Tema 1.231" em vez de
   ADI 6.309/DF.

**Antes de usar qualquer súmula ou tese destes quatro arquivos em uma
petição, parecer ou comunicação de valor ao cliente, o advogado responsável
deve conferir a redação exata na fonte oficial correspondente:**

- Súmulas do STF: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp
- Temas de Repercussão Geral do STF: https://portal.stf.jus.br/jurisprudenciaRepercussao/
- Súmulas do STJ: https://scon.stj.jus.br/SCON/sumstj/
- Súmulas da TNU: https://www.cjf.jus.br (lista oficial de súmulas da TNU)

## URLs oficiais consultadas (ou referenciadas nos resultados de busca)

- https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp (súmulas STF e SV — múltiplas páginas, uma por súmula)
- https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp (temas de repercussão geral — múltiplas páginas, uma por tema)
- https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp (andamento processual de temas)
- https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp (notícias oficiais do STF sobre julgamentos)
- https://noticias.stf.jus.br/postsnoticias/ (notícias oficiais do STF)
- https://scon.stj.jus.br/SCON/sumstj/ (súmulas do STJ)
- https://www.stj.jus.br (súmulas e notícias do STJ)
- https://www.cjf.jus.br (notícias e súmulas da TNU)

## Agregadores jurídicos usados como apoio (fontes secundárias)

- buscadordizerodireito.com.br / dizerodireito.com.br
- jusbrasil.com.br
- legjur.com
- modeloinicial.com.br
- tesesesumulas.com.br
- previdenciarista.com
- ieprev.com.br
- jurishand.com
- juris.damasio.com.br
- migalhas.com.br / conjur.com.br (notícias jurídicas sobre julgamentos)
- gov.br/previdencia (Ministério da Previdência Social — notas sobre julgamentos do STF)

## Descobertas relevantes desta pesquisa (números que não eram o que pareciam)

Resumo consolidado — o detalhamento completo está em cada arquivo:

| Item pesquisado | Suposição original | O que a pesquisa confirmou |
|---|---|---|
| Súmula 33 STF | Contagem recíproca de tempo de serviço | Lei 1.741/1952 e autarquias federais — sem relação com Direito Previdenciário |
| Súmula 368 STF | "Descontos INSS" | Embargos infringentes em reclamação — sem relação com Direito Previdenciário |
| Súmula Vinculante 2 STF | Prioridade de idosos | Competência legislativa sobre loterias/bingos/consórcios — sem relação com Direito Previdenciário |
| "Tema 1.125" STF | Revisão da vida toda | O número correto é o Tema 1.102; o Tema 1.125 real trata de auxílio-doença intercalado e carência |
| Tema 1.302 STF | BPC/LOAS | Competência para cobrança de anuidades da OAB — sem relação com BPC. O tema correto sobre BPC é o Tema 27 |
| 7 de 13 números sugeridos de súmulas do STJ | Diversos temas previdenciários | Sem qualquer relação com Direito Previdenciário (ver tabela em `sumulas-stj.md`) |

Esses achados seguem o mesmo padrão do erro já corrigido nesta base para
"STF, Tema 1.231" (que não é o precedente da aposentadoria especial — o
precedente correto é a ADI 6.309/DF). O padrão recorrente é: **um número de
súmula ou de tema, citado de memória, quase nunca deve ser aceito sem
verificação individual — a proximidade numérica ou a familiaridade do
assunto não garante que o número esteja certo.**

## O que este arquivo NÃO garante

- Não garante que a lista de súmulas/temas seja exaustiva. Foram
  pesquisados os números indicados mais alguns adicionais localizados como
  genuinamente relevantes; pode haver outras súmulas/temas previdenciários
  relevantes não cobertos aqui.
- Não garante que os temas com status "em julgamento" ou "repercussão geral
  reconhecida" continuem nesse status na data em que este arquivo for lido
  — a situação processual muda com o tempo.
- Não substitui a consulta ao inteiro teor do acórdão antes de uma citação
  de peso decisivo em uma petição.
