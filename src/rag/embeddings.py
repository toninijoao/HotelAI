import torch
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import EMBEDDING_MODEL


def get_embeddings(model_name: str = EMBEDDING_MODEL) -> HuggingFaceEmbeddings:
    """Cria o modelo de embeddings (HuggingFace/Sentence Transformers sobre PyTorch)."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True},
    )
