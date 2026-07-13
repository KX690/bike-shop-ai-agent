"""
vectorstore_service.py

Responsabilidad:
    Inicializar el índice vectorial utilizado
    por el sistema RAG.

Flujo:

    1. Descargar el índice desde OCI Object Storage
       si todavía no existe localmente.

    2. Cargar el índice FAISS.

Este servicio nunca genera embeddings
ni reconstruye el índice.
"""

from __future__ import annotations

import logging
from pathlib import Path

from app.config.settings import settings
from app.processing.embeddings import (
    cargar_embeddings,
)
from app.services.oci_storage_service import (
    OCIStorageService,
)
from app.vectorstores.faiss_store import (
    cargar_vectorstore,
)

logger = logging.getLogger(__name__)


def inicializar_vectorstore():
    """
    Inicializa el VectorStore utilizado
    por el sistema RAG.

    Returns:
        FAISS:
            Índice listo para realizar
            búsquedas semánticas.
    """

    logger.info(
        "Inicializando índice vectorial."
    )

    storage = OCIStorageService()

    vector_path = Path(
        settings.VECTOR_DB_PATH
    )

    vector_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    archivos = [
        "index.faiss",
        "index.pkl",
    ]

    for archivo in archivos:

        storage.descargar_si_no_existe(
            object_name=f"vectorstore/{archivo}",
            destino=str(
                vector_path / archivo
            ),
        )

    logger.info(
        "Índice FAISS disponible localmente."
    )

    embeddings = cargar_embeddings()

    logger.info(
        "Cargando índice FAISS."
    )

    return cargar_vectorstore(
        embeddings
    )
