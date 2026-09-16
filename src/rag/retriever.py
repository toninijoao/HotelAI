from src.config import RETRIEVER_K
from src.rag.vectorstore import load_vectorstore


def get_retriever(k: int = RETRIEVER_K):
    """Cria o retriever a partir do vectorstore existente."""
    vectorstore = load_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": k})
