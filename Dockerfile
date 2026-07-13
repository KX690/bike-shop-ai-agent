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
    TRANSFORMERS_VERBOSITY=error \
    PYTHONWARNINGS=ignore \
    TF_CPP_MIN_LOG_LEVEL=3 \
    HF_HOME=/app/.cache/huggingface \
    TRANSFORMERS_CACHE=/app/.cache/huggingface \
    TOKENIZERS_PARALLELISM=false

# =====================================================
# Directorio de trabajo
# =====================================================

WORKDIR /app

# =====================================================
# Dependencias del sistema
# =====================================================

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# =====================================================
# Copiar requirements.txt
# =====================================================

COPY requirements.txt .

# =====================================================
# Actualizar pip
# =====================================================

RUN python -m pip install --upgrade pip --retries=20 --timeout=2000

# =====================================================
# INSTALAR DEPENDENCIAS (usando versiones de tu entorno)
# =====================================================

# 1. Instalar numpy primero (base para todo)
RUN pip install --no-cache-dir \
    numpy==2.5.0 \
    --timeout 2000 \
    --retries 20

# 2. Instalar PyTorch (versión CPU)
RUN pip install --no-cache-dir \
    torch==2.12.1 \
    --index-url https://download.pytorch.org/whl/cpu \
    --timeout 2000 \
    --retries 20

# 3. Instalar torchvision (compatible con torch 2.12.1)
RUN pip install --no-cache-dir \
    torchvision==0.27.1 \
    --index-url https://download.pytorch.org/whl/cpu \
    --timeout 2000 \
    --retries 20

# 4. Instalar transformers y sentence-transformers
RUN pip install --no-cache-dir \
    transformers==5.12.1 \
    sentence-transformers==5.6.0 \
    --timeout 2000 \
    --retries 20

# 5. Instalar el resto de dependencias
RUN pip install --no-cache-dir \
    -r requirements.txt \
    --timeout 2000 \
    --retries 20

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
    /app/.cache/huggingface \
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
