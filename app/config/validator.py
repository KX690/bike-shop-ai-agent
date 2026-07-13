"""
validator.py

Responsabilidad:
    Validar la configuración crítica de la aplicación
    antes de iniciar el sistema.

La validación es compatible con:
    - Variables de entorno locales (.env)
    - Docker
    - OCI Vault
    - GitHub Actions
"""

from __future__ import annotations

import logging

from app.config.settings import settings
from app.core.exceptions import ConfigurationError

logger = logging.getLogger(__name__)


def validar_configuracion() -> None:
    """
    Valida que todas las configuraciones críticas
    necesarias para ejecutar la aplicación estén
    presentes.
    """

    configuraciones_requeridas = {
        "GEMINI_API_KEY": settings.GEMINI_API_KEY,
    }

    faltantes = [
        nombre
        for nombre, valor in configuraciones_requeridas.items()
        if not valor
    ]

    if faltantes:

        logger.critical(
            "Configuración inválida. Variables faltantes: %s",
            ", ".join(faltantes),
        )

        raise ConfigurationError(
            "Las siguientes variables de entorno son obligatorias: "
            + ", ".join(faltantes)
        )

    logger.info(
        "Configuración validada correctamente."
    )
