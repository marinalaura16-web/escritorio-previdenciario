# Escritório Previdenciário — Interface Streamlit

Interface web simplificada para análise de casos previdenciários, que chama
a **API Anthropic diretamente** (SDK `anthropic`, sem o Claude Agent SDK).
Permite que o escritório use o sistema sem precisar do Claude Code.

**Todo output gerado é um RASCUNHO para revisão do advogado responsável**
(regra inviolável 1 do projeto — ver `CLAUDE.md` na raiz do repositório). O
Claude Code Web continua sendo a versão completa do sistema multiagente;
este app é uma versão simplificada, de uma única chamada à API, que simula
internamente o fluxo triagem → cálculo → arquivo médico → petição.

## Modelos

Esta interface usa exclusivamente os IDs de modelo vigentes desta família na
API Anthropic:

| Opção na interface | Model ID | Preço (entrada / saída por MTok) |
|---|---|---|
| Sonnet 5 (rápido) | `claude-sonnet-5` | $2.00 / $10.00 |
| Opus 5 (preciso) | `claude-opus-5` | $5.00 / $25.00 |

> Os IDs "claude-sonnet-4-5" e "Opus 4.1", eventualmente citados em
> instruções antigas, **não existem** na API Anthropic atual — foram
> substituídos pelos dois IDs acima em todo o código deste app.

## Como rodar localmente

```bash
cd app
pip install -r requirements.txt

# Configure a API Key
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# edite .streamlit/secrets.toml e cole sua chave (sk-ant-...)

streamlit run streamlit_app.py
```

A interface também aceita a API Key digitada diretamente na barra lateral
(campo do tipo senha) — útil para testar sem editar `secrets.toml`. **Nunca
coloque a chave direto no código.**

## Como hospedar no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte sua
   conta do GitHub.
2. Selecione o repositório `escritorio-previdenciario` e aponte o arquivo
   principal para `app/streamlit_app.py`.
3. Em **Settings → Secrets**, cole o conteúdo de
   `.streamlit/secrets.toml.example` preenchido com a chave real:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
4. Deploy. O tema (`app/.streamlit/config.toml`) e o limite de upload são
   aplicados automaticamente.

## Estrutura de arquivos

```
app/
├── requirements.txt          # dependências (streamlit, anthropic, pdfplumber, ...)
├── streamlit_app.py          # interface (sidebar, Tab "Novo Caso", Tab "Casos Anteriores")
├── anthropic_client.py       # chamada à API Anthropic (streaming, prompt consolidado, parse do JSON)
├── prompts.py                # carrega prompts dos subagentes/skills e o contexto do escritório
├── pdf_utils.py               # extração de texto de PDF via pdfplumber
├── .streamlit/
│   ├── config.toml            # tema (azul escuro #1a3a5c) e limites do servidor
│   └── secrets.toml.example   # modelo do arquivo de segredos (copiar para secrets.toml)
└── README.md                  # este arquivo
```

Casos analisados são salvos na raiz do repositório, em
`casos/{numero}/documentos/` (PDFs enviados) e `casos/{numero}/analises/`
(as 4 seções geradas, uma por arquivo `.md`), no mesmo padrão de
organização usado pelo Claude Code (`CLAUDE.md`, regra 5).

## Custo estimado por análise

Uma análise típica envolve, no prompt consolidado (system + user): o prompt
do agente orquestrador, os prompts dos 3 subagentes relevantes (triagem,
cálculo, arquivo médico), a skill de cálculo, um resumo do perfil do
escritório e do índice de legislação, e o texto extraído dos documentos do
caso (CNIS, CTPS, laudos, carta de indeferimento). Isso soma tipicamente
**15.000–30.000 tokens de entrada**. A resposta (as 4 seções — triagem,
cálculo, arquivo médico e petição) soma tipicamente **4.000–8.000 tokens de
saída** de texto — sem contar os tokens de *thinking* (cobrados como
saída), que podem aumentar esse número dependendo da complexidade do caso.

Cálculo (preços por milhão de tokens — MTok):

| Modelo | Entrada (15k–30k tok) | Saída (4k–8k tok) | Total por caso |
|---|---|---|---|
| Sonnet 5 ($2 / $10 por MTok) | $0.03 – $0.06 | $0.04 – $0.08 | **≈ $0.07 – $0.14** |
| Opus 5 ($5 / $25 por MTok) | $0.075 – $0.15 | $0.10 – $0.20 | **≈ $0.18 – $0.35** |

> Esses valores não incluem o custo dos tokens de *thinking* (adaptive
> thinking com `effort: "high"`), que são cobrados como tokens de saída e
> podem elevar o custo real acima da faixa acima em casos complexos.
> **Os preços podem mudar** — confira sempre os valores atuais em
> [anthropic.com/pricing](https://anthropic.com/pricing) antes de usar
> essas estimativas para orçamento.

## Base legislativa injetada no prompt

Além dos prompts dos agentes/skills (que descrevem o *processo*, não o
*conteúdo normativo*), o prompt enviado à API inclui o texto de 5 arquivos
de `legislacao/` (INDICE.md, EC 103/2019, Lei 8.213/1991, Lei 8.742/1993,
Decreto 3.048/1999 — cada um truncado em 50.000 caracteres) e as últimas
200 linhas de dados das tabelas `inpc-historico.csv` e
`tetos-rgps-historico.csv` (cabeçalho sempre preservado). A instrução ao
modelo é explícita: **usar apenas essa base para citar dispositivos**, e
marcar `[A CONFIRMAR NA FONTE OFICIAL]` para o que não estiver nela — ver
`anthropic_client.carregar_base_legislativa()`.

## Análise em background

A chamada à API roda em uma `threading.Thread` separada (não bloqueia o
script principal do Streamlit), com o status guardado em um dict a nível
de módulo (`_ANALISES_EM_ANDAMENTO`, protegido por lock) em vez de
`st.session_state` diretamente — a Streamlit não garante escrita segura em
`session_state` fora da thread principal do script. Isso evita perder o
resultado se a conexão websocket cair (ex.: o usuário troca de aba do
navegador). Um botão "🔄 Verificar status" força um rerun para checar se a
análise já terminou. **Limitação conhecida:** esse estado é de processo,
não de sessão — sobrevive a uma reconexão, mas não a um reinício completo
do servidor Streamlit (nesse caso raro, a análise em andamento se perde e
o usuário precisa iniciar de novo).

## Limitações conhecidas desta versão simplificada

- **Upload de documentos**: um único `file_uploader` com múltiplos
  arquivos é usado para CNIS, CTPS, PPPs, laudos e carta de indeferimento
  juntos — o Streamlit não segmenta uploads por categoria de forma simples.
  O modelo infere o tipo de cada documento pelo próprio conteúdo.
- **PDF escaneado (sem camada de texto)**: é detectado e sinalizado com um
  aviso na interface ("PDF parece ser escaneado... considere usar OCR"),
  mas esta versão não faz OCR automaticamente.
- **"Copiar para área de transferência"**: o Streamlit não tem, nesta
  versão, um componente nativo robusto de clipboard. É usado `st.code()`,
  que já exibe um ícone de cópia embutido no bloco.
- Todo o processamento é feito em uma única chamada de API (com streaming),
  simulando o fluxo multiagente em vez de orquestrar agentes reais — para
  o fluxo completo com agentes reais, use o Claude Code Web.
