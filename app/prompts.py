"""Carregamento de prompts dos subagentes, skills e contexto do escritório
para montar o prompt consolidado enviado à API Anthropic.

Todas as funções deste módulo são tolerantes a arquivo ausente: nunca
lançam exceção que quebre a interface — em caso de erro, devolvem uma
string vazia ou uma mensagem `[não encontrado: ...]` para que o restante
do prompt continue sendo montado normalmente.
"""

from __future__ import annotations

from pathlib import Path

# Raiz do repositório, resolvida de forma robusta a partir deste arquivo
# (app/prompts.py -> app/ -> raiz), independente do diretório de trabalho
# atual de onde o Streamlit for iniciado.
REPO_ROOT = Path(__file__).resolve().parent.parent

AGENTES_DIR = REPO_ROOT / ".claude" / "agents"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
PRACTICE_PROFILE_PATH = REPO_ROOT / "practice-profile.md"
INDICE_LEGISLACAO_PATH = REPO_ROOT / "legislacao" / "INDICE.md"

# Número máximo de linhas do INDICE.md incluídas no contexto (o arquivo
# completo tem centenas de linhas — incluir tudo estouraria o prompt sem
# necessidade; truncamos com aviso explícito em vez de tentar resumir).
MAX_LINHAS_INDICE = 150


def _remover_frontmatter(conteudo: str) -> str:
    """Remove o frontmatter YAML (entre '---' no topo do arquivo), se
    existir, e devolve apenas o corpo do prompt."""
    texto = conteudo.strip()
    if texto.startswith("---"):
        partes = texto.split("---", 2)
        if len(partes) >= 3:
            return partes[2].strip()
    return texto


def _ler_arquivo(caminho: Path) -> str | None:
    try:
        return caminho.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeDecodeError):
        return None


def carregar_prompt(nome_agente: str) -> str:
    """Lê `.claude/agents/{nome_agente}.md` e devolve o corpo do prompt
    (sem frontmatter). Devolve uma mensagem `[não encontrado]` se o arquivo
    não existir."""
    caminho = AGENTES_DIR / f"{nome_agente}.md"
    conteudo = _ler_arquivo(caminho)
    if conteudo is None:
        return f"[não encontrado: {caminho.relative_to(REPO_ROOT)}]"
    return _remover_frontmatter(conteudo)


def carregar_skill(nome_skill: str) -> str:
    """Lê `.claude/skills/{nome_skill}/SKILL.md` e devolve o corpo do
    prompt (sem frontmatter). Devolve uma mensagem `[não encontrado]` se o
    arquivo não existir."""
    caminho = SKILLS_DIR / nome_skill / "SKILL.md"
    conteudo = _ler_arquivo(caminho)
    if conteudo is None:
        return f"[não encontrado: {caminho.relative_to(REPO_ROOT)}]"
    return _remover_frontmatter(conteudo)


def montar_contexto_escritorio() -> str:
    """Monta uma string com o perfil do escritório (practice-profile.md) e
    um resumo (truncado) do índice de legislação (legislacao/INDICE.md)."""
    partes = []

    perfil = _ler_arquivo(PRACTICE_PROFILE_PATH)
    if perfil is None:
        perfil = "[practice-profile.md não encontrado]"
    partes.append("### Perfil do Escritório (practice-profile.md)\n" + perfil.strip())

    indice_bruto = _ler_arquivo(INDICE_LEGISLACAO_PATH)
    if indice_bruto is None:
        resumo_indice = "[legislacao/INDICE.md não encontrado]"
    else:
        linhas = indice_bruto.splitlines()
        if len(linhas) > MAX_LINHAS_INDICE:
            resumo_indice = "\n".join(linhas[:MAX_LINHAS_INDICE])
            resumo_indice += (
                f"\n\n[... ÍNDICE TRUNCADO — arquivo completo tem "
                f"{len(linhas)} linhas; consulte legislacao/INDICE.md na "
                f"íntegra antes de citar dispositivo não listado aqui ...]"
            )
        else:
            resumo_indice = "\n".join(linhas)
    partes.append(
        "### Resumo do Índice de Legislação (legislacao/INDICE.md, truncado)\n"
        + resumo_indice
    )

    return "\n\n".join(partes)
