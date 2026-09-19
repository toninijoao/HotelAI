from langchain_community.document_loaders import TextLoader


def load_document(document_path: str):
    """Carrega o arquivo Markdown com as informações do hotel."""
    loader = TextLoader(document_path, encoding="utf-8")
    return loader.load()