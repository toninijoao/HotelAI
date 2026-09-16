from langchain_core.messages import SystemMessage
from src.agent.prompts import RAG_SYSTEM_PROMPT
from src.agent.state import HotelState
from src.config import HOTEL_NAME
from src.rag.retriever import get_retriever

_retriever = None


def _get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = get_retriever()
    return _retriever


def retrieve_node(state: HotelState) -> dict:
    """Busca os chunks mais relevantes no vectorstore para a última mensagem do usuário."""
    query = state["messages"][-1].content

    retriever = _get_retriever()
    docs = retriever.invoke(query)

    retrieved_docs = [
        {"content": doc.page_content, "page": doc.metadata.get("page")}
        for doc in docs
    ]
    context = "\n\n".join(doc["content"] for doc in retrieved_docs)

    return {"retrieved_context": context, "retrieved_docs": retrieved_docs}


def generate_node(state: HotelState, llm) -> dict:
    """Gera a resposta do assistente com base no contexto recuperado."""
    context = state.get("retrieved_context", "")
    system_prompt = RAG_SYSTEM_PROMPT.format(hotel_name=HOTEL_NAME, context=context)

    messages = [SystemMessage(content=system_prompt), *state["messages"]]
    response = llm.invoke(messages)

    return {"messages": [response]}
