from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph

from src.agent.nodes import generate_node, retrieve_node
from src.agent.state import HotelState
from src.config import GROQ_API_KEY, GROQ_MODEL


def _build_llm():
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
