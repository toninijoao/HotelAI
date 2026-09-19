import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCUMENT_PATH = os.path.join(BASE_DIR, "data", "hotel.md")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))

RETRIEVER_K = int(os.getenv("RETRIEVER_K", "4"))

HOTEL = os.getenv("HOTEL", "Hotel AI")