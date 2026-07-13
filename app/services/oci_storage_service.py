"""
oci_storage_service.py

Responsabilidad:
    Administrar la comunicación con Oracle Cloud
    Infrastructure Object Storage.

Autenticación:

    • Desarrollo local:
        ~/.oci/config

    • Producción (OCI Compute):
        Instance Principals
"""

from __future__ import annotations

import logging
from pathlib import Path

import oci

from app.config.settings import settings

logger = logging.getLogger(__name__)


class OCIStorageService:
    """
    Servicio para administrar Object Storage.
    """

    def __init__(self) -> None:

        self.client = self._crear_cliente()

    def _crear_cliente(
        self,
    ) -> oci.object_storage.ObjectStorageClient:
        """
        Crea el cliente OCI utilizando el mecanismo
        de autenticación adecuado.

        Returns:
            ObjectStorageClient
        """

        try:

            config = oci.config.from_file()

            logger.info(
                "Autenticación OCI mediante archivo de configuración local."
            )

            return oci.object_storage.ObjectStorageClient(
                config
            )

        except Exception:

            logger.info(
                "Autenticación OCI mediante Instance Principals."
            )

            signer = (
                oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            )

            return oci.object_storage.ObjectStorageClient(
                config={
                    "region": settings.OCI_REGION
                },
                signer=signer,
            )

    def listar_objetos(
        self,
        prefix: str,
    ):
        """
        Lista objetos de un prefijo.
        """

        return self.client.list_objects(
            namespace_name=settings.OCI_NAMESPACE,
            bucket_name=settings.OCI_BUCKET_NAME,
            prefix=prefix,
        )

    def descargar_archivo(
        self,
        object_name: str,
        destino: str,
    ) -> None:
        """
        Descarga un archivo desde OCI.
        """

        Path(destino).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(
            "Descargando %s",
            object_name,
        )

        response = self.client.get_object(
            namespace_name=settings.OCI_NAMESPACE,
            bucket_name=settings.OCI_BUCKET_NAME,
            object_name=object_name,
        )

        with open(
            destino,
            "wb",
        ) as archivo:

            archivo.write(
                response.data.content
            )

    def descargar_si_no_existe(
        self,
        object_name: str,
        destino: str,
    ) -> None:
        """
        Descarga un archivo únicamente si no existe
        en el sistema de archivos local.

        Args:
            object_name:
                Ruta del objeto en OCI.

            destino:
                Ruta local donde se almacenará.
        """

        if Path(destino).exists():

            logger.info(
                "El archivo %s ya existe localmente.",
                destino,
            )

            return

        self.descargar_archivo(
            object_name=object_name,
            destino=destino,
        )

    def subir_archivo(
        self,
        origen: str,
        object_name: str,
    ) -> None:
        """
        Sube un archivo a OCI.
        """

        logger.info(
            "Subiendo %s",
            object_name,
        )

        with open(
            origen,
            "rb",
        ) as archivo:

            self.client.put_object(
                namespace_name=settings.OCI_NAMESPACE,
                bucket_name=settings.OCI_BUCKET_NAME,
                object_name=object_name,
                put_object_body=archivo,
            )

    def existe_archivo(
        self,
        object_name: str,
    ) -> bool:
        """
        Verifica si un objeto existe.
        """

        try:

            self.client.head_object(
                namespace_name=settings.OCI_NAMESPACE,
                bucket_name=settings.OCI_BUCKET_NAME,
                object_name=object_name,
            )

            return True

        except oci.exceptions.ServiceError:

            return False
