from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """Carrega um PDF e retorna a lista de documentos (um por página)."""
    loader = PyPDFLoader(pdf_path)
    return loader.load()
