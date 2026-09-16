from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_OVERLAP, CHUNK_SIZE

def split_documents(documents, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
    """Divide documentos em chunks adequados para indexação no RAG."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_documents(documents)