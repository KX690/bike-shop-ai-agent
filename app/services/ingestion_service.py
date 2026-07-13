"""
ingestion_service.py

Responsabilidad:
    Orquestar el pipeline completo de ingesta documental
    para construir y publicar el índice vectorial FAISS.

Pipeline:

    1. Cargar documentos.
    2. Limpiar documentos.
    3. Enriquecer metadatos.
    4. Generar fragmentos.
    5. Generar embeddings.
    6. Construir índice FAISS.
    7. Guardar índice localmente.
    8. Publicar índice en OCI Object Storage.
"""

from __future__ import annotations

import logging
from pathlib import Path

from app.config.settings import settings
from app.loaders.pdf_loader import (
    cargar_documentos,
)
from app.processing.chunking import (
    crear_chunks,
)
from app.services.document_sync_service import (
    sincronizar_documentos,
)
from app.processing.cleaning import (
    limpiar_documentos,
)
from app.processing.embeddings import (
    cargar_embeddings,
)
from app.processing.metadata import (
    enriquecer_metadata,
)
from app.services.oci_storage_service import (
    OCIStorageService,
)
from app.vectorstores.faiss_store import (
    crear_vectorstore,
    guardar_vectorstore,
)

logger = logging.getLogger(__name__)


def construir_vectorstore():
    """
    Construye un nuevo índice vectorial FAISS y lo publica
    en Oracle Cloud Infrastructure Object Storage.

    Returns:
        FAISS:
            Índice vectorial generado.
    """

    logger.info(
        "Iniciando proceso de ingesta documental."
    )

    logger.info(
        "Sincronizando documentos desde OCI."
    )

    sincronizar_documentos()

    documentos = cargar_documentos()

    logger.info(
        "Documentos cargados: %d",
        len(documentos),
    )

    documentos = limpiar_documentos(
        documentos
    )

    logger.info(
        "Limpieza de documentos completada."
    )

    documentos = enriquecer_metadata(
        documentos
    )

    logger.info(
        "Metadatos enriquecidos correctamente."
    )

    chunks = crear_chunks(
        documentos
    )

    logger.info(
        "Chunks generados: %d",
        len(chunks),
    )

    embeddings = cargar_embeddings()

    logger.info(
        "Modelo de embeddings cargado."
    )

    vectorstore = crear_vectorstore(
        chunks,
        embeddings,
    )

    guardar_vectorstore(
        vectorstore
    )

    logger.info(
        "Índice FAISS generado localmente."
    )

    storage = OCIStorageService()

    vector_path = Path(
        settings.VECTOR_DB_PATH
    )

    logger.info(
        "Publicando índice en OCI Object Storage."
    )

    storage.subir_archivo(
        str(vector_path / "index.faiss"),
        "vectorstore/index.faiss",
    )

    storage.subir_archivo(
        str(vector_path / "index.pkl"),
        "vectorstore/index.pkl",
    )

    logger.info(
        "Índice publicado correctamente."
    )

    logger.info(
        "Proceso de ingesta finalizado."
    )

    return vectorstore
