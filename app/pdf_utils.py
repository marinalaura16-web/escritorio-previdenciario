"""Utilitários de extração de texto de PDF para a interface Streamlit.

Abordagem de tratamento de erro adotada neste módulo (consistente em toda a
função pública): nunca lançamos exceção para o chamador. `extrair_texto_pdf`
sempre devolve uma tupla `(texto, erro)`, onde `erro` é `None` em caso de
sucesso ou uma mensagem de string pronta para ser exibida ao usuário (via
`st.warning`/`st.error`) em caso de falha — incluindo o caso de PDF
escaneado (imagem sem camada de texto), que é tratado como um aviso
específico e não como uma exceção.
"""

from __future__ import annotations

import logging

import pdfplumber

logger = logging.getLogger(__name__)

# Limiar heurístico: se o texto extraído de todas as páginas somado tiver
# menos que este número de caracteres, tratamos como "PDF provavelmente
# escaneado / sem texto extraível" em vez de simplesmente devolver um texto
# vazio silenciosamente.
MIN_CARACTERES_TEXTO_VALIDO = 30


def extrair_texto_pdf(arquivo_pdf) -> tuple[str, str | None]:
    """Extrai o texto de um PDF usando pdfplumber.

    Args:
        arquivo_pdf: um caminho (str/Path) para o PDF, ou um objeto
            file-like (por exemplo, o retorno de `st.file_uploader`).

    Returns:
        Uma tupla `(texto, erro)`:
        - Em caso de sucesso: `(texto_extraido, None)`.
        - Em caso de falha (exceção ao abrir/ler o PDF, ou texto extraído
          vazio/curto demais — sinal de PDF escaneado sem OCR): `("", erro)`,
          onde `erro` é uma mensagem clara para exibir ao usuário.
    """
    try:
        # Objetos file-like do st.file_uploader mantêm um cursor interno;
        # garantimos que a leitura comece do início.
        if hasattr(arquivo_pdf, "seek"):
            arquivo_pdf.seek(0)

        textos_por_pagina = []
        with pdfplumber.open(arquivo_pdf) as pdf:
            if len(pdf.pages) == 0:
                return "", "PDF não contém páginas."
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text() or ""
                textos_por_pagina.append(texto_pagina)
    except Exception as e:  # pdfplumber/pdfminer podem lançar vários tipos
        logger.warning("Falha ao extrair texto do PDF: %s", e)
        return "", f"Erro ao processar PDF: {e}"

    texto_completo = "\n".join(textos_por_pagina).strip()

    if len(texto_completo) < MIN_CARACTERES_TEXTO_VALIDO:
        return (
            "",
            "PDF parece ser escaneado (sem texto extraível) — considere "
            "usar OCR antes de enviar.",
        )

    return texto_completo, None
