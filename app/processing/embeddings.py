from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)
from app.config.settings import settings


def cargar_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GEMINI_API_KEY,
    )

    return embeddings
