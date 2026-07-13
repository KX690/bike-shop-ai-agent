"""
document_sync_service.py

Responsabilidad:
    Sincronizar los documentos almacenados en
    Oracle Object Storage hacia el entorno local.

Uso:

    OCI Object Storage
            ↓
    documentos/
            ↓
    data/documentos/
"""

from __future__ import annotations

import logging
from pathlib import Path

from app.config.settings import settings
from app.services.oci_storage_service import (
    OCIStorageService,
)

logger = logging.getLogger(__name__)


def sincronizar_documentos() -> None:
    """
    Descarga todos los documentos PDF desde
    OCI Object Storage hacia el directorio local.

    Mantiene la estructura de carpetas:

        documentos/
            productos/
            envios/
            politicas/
    """

    logger.info(
        "Iniciando sincronización de documentos."
    )

    storage = OCIStorageService()

    response = storage.listar_objetos(
        prefix="documentos/"
    )

    cantidad = 0

    for objeto in response.data.objects:

        object_name = objeto.name

        if not object_name.endswith(".pdf"):
            continue

        ruta_relativa = object_name.replace(
            "documentos/",
            "",
            1,
        )

        destino = (
            Path(settings.DOCUMENTS_PATH)
            / ruta_relativa
        )

        storage.descargar_archivo(
            object_name=object_name,
            destino=str(destino),
        )

        cantidad += 1

    logger.info(
        "Sincronización finalizada. PDFs descargados: %d",
        cantidad,
    )
