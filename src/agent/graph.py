from langgraph.graph import END, START, StateGraph

from src.agent.nodes import generate_node, retrieve_node
from src.agent.state import HotelState
from src.config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
    GROQ_API_KEY,
    GROQ_MODEL,
    LLM_PROVIDER,
)


def _build_llm():
    if LLM_PROVIDER == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(model=ANTHROPIC_MODEL, api_key=ANTHROPIC_API_KEY)

    from langchain_groq import ChatGroq

    return ChatGroq(model=GROQ_MODEL, api_key=GROQ_API_KEY)


def build_graph():
    """Constrói o grafo LangGraph: START -> retrieve -> generate -> END."""
    llm = _build_llm()

    graph = StateGraph(HotelState)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", lambda state: generate_node(state, llm))

    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()
