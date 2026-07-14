# =====================================================
# CicloStore AI Agent - Production Docker Image
# =====================================================

FROM python:3.13-slim

# =====================================================
# Variables de entorno
# =====================================================

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=2000 \
    PIP_RETRIES=20 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    PYTHONWARNINGS=ignore

# =====================================================
# Directorio de trabajo
# =====================================================

WORKDIR /app

# =====================================================
# Dependencias del sistema
# =====================================================

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# =====================================================
# Instalar dependencias de Python
# =====================================================

COPY requirements.txt .

RUN python -m pip install --upgrade pip --retries=20 --timeout=2000 && \
    pip install --no-cache-dir -r requirements.txt --timeout 2000 --retries 20

# =====================================================
# Copiar aplicación
# =====================================================

COPY . .

# =====================================================
# Directorios utilizados por la aplicación
# =====================================================

RUN mkdir -p \
    /app/vector_db/faiss_index \
    /app/data/documentos \
    /app/logs

# =====================================================
# Usuario sin privilegios
# =====================================================

RUN useradd -ms /bin/bash ciclostoreai && \
    chown -R ciclostoreai:ciclostoreai /app

USER ciclostoreai

# =====================================================
# Puerto
# =====================================================

EXPOSE 8501

# =====================================================
# Health Check
# =====================================================

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# =====================================================
# Ejecutar aplicación
# =====================================================

CMD ["streamlit", "run", "streamlit_app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--logger.level=error"]
