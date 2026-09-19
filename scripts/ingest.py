import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.config import DOCUMENT_PATH, VECTORSTORE_DIR
from src.rag.loader import load_document
from src.rag.splitter import split_documents
from src.rag.vectorstore import create_vectorstore


def main():
    print(f"Carregando PDF de: {PDF_PATH}")
    documents = load_pdf(PDF_PATH)
    print(f"{len(documents)} página(s) carregada(s).")

    print("Dividindo documentos em chunks...")
    chunks = split_documents(documents)
    print(f"{len(chunks)} chunk(s) gerado(s).")

    print(f"Criando vectorstore em: {VECTORSTORE_DIR}")
    create_vectorstore(chunks, persist_directory=VECTORSTORE_DIR)
    print("Ingestão concluída com sucesso.")


if __name__ == "__main__":
    main()
