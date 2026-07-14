"""
settings.py

Configuración centralizada de la aplicación.

Responsabilidades:
- Cargar variables de entorno.
- Validar configuraciones críticas.
- Exponer parámetros globales.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Configuración global de la aplicación.
    """

    # =========================
    # API KEYS
    # =========================

    GEMINI_API_KEY: str | None = os.getenv(
        "GEMINI_API_KEY"
    )

    LANGSMITH_API_KEY: str | None = os.getenv(
        "LANGSMITH_API_KEY"
    )

    # =========================
    # LANGSMITH
    # =========================

    LANGSMITH_TRACING: bool = (
        os.getenv(
            "LANGSMITH_TRACING",
            "false"
        ).lower()
        == "true"
    )

    # =========================
    # MODELOS
    # =========================

    GEMINI_MODEL: str = (
        "gemini-flash-latest"
    )

    TEMPERATURE: float = 0.0

    # =========================
    # EMBEDDINGS
    # =========================

    EMBEDDING_MODEL: str = (
        "models/gemini-embedding-001"
    )

    # =========================
    # CHUNKING
    # =========================

    CHUNKS_TOKENIZER_ENCODING: str = (
        "cl100k_base"
    )

    CHUNK_SIZE: int = 1250

    CHUNK_OVERLAP: int = 150

    # =========================
    # VECTOR STORE
    # =========================

    VECTOR_DB_PATH: str = os.getenv(
        "VECTOR_DB_PATH",
        "./vector_db/faiss_index",
    )

    DOCUMENTS_PATH: str = os.getenv(
        "DOCUMENTS_PATH",
        "./data/documentos",
    )

    # =========================
    # RETRIES
    # =========================

    MAX_RETRIES: int = 3

    RETRY_DELAY_SECONDS: int = 5

    # =========================
    # RETRIEVER
    # =========================

    RETRIEVER_SEARCH_TYPE = 'mmr'
    RETRIEVER_K = 3
    RETRIEVER_FETCH_K = 15
    RETRIEVER_LAMBDA_MULT = 0.3

    # =========================
    # OCI
    # =========================

    OCI_BUCKET_NAME: str = os.getenv(
        "OCI_BUCKET_NAME",
        "",
    )

    OCI_NAMESPACE: str = os.getenv(
        "OCI_NAMESPACE",
        "",
    )

    OCI_REGION: str = os.getenv(
        "OCI_REGION",
        "sa-santiago-1",
    )


settings = Settings()
