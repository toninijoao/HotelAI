import os
from langchain_chroma import Chroma
from src.config import VECTORSTORE_DIR
from src.rag.embeddings import get_embeddings

def create_vectorstore(documents, persist_directory: str = VECTORSTORE_DIR) -> Chroma:
    """Cria um novo vectorstore Chroma a partir dos documentos e o persiste em disco."""
    embeddings = get_embeddings()
    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory,
    )

def load_vectorstore(persist_directory: str = VECTORSTORE_DIR) -> Chroma:
    """Carrega um vectorstore Chroma já existente em disco."""
    if not os.path.isdir(persist_directory) or not os.listdir(persist_directory):
        raise FileNotFoundError(
            f"Vectorstore não encontrado em '{persist_directory}'. "
            "Execute 'python scripts/ingest.py' antes de iniciar o app."
        )
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )