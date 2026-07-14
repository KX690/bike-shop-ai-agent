from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from app.config.settings import settings


def crear_chunks(documentos):

    splitter = (
        RecursiveCharacterTextSplitter
        .from_tiktoken_encoder(
            encoding_name=settings.CHUNKS_TOKENIZER_ENCODING,
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )
    )

    chunks = splitter.split_documents(
        documentos
    )

    return chunks
