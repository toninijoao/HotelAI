import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
import streamlit as st
from langchain_core.messages import HumanMessage
from src.agent.graph import build_graph
from src.config import EMBEDDING_MODEL, GROQ_MODEL, HOTEL

st.set_page_config(page_title=HOTEL, page_icon="🏨")

@st.cache_resource
def get_graph():
    return build_graph()

def main():
    st.title(f"🏨 {HOTEL}")
    st.caption("Assistente virtual do hotel")

    dev_mode = st.sidebar.toggle("Modo desenvolvedor", value=False)

    if "history" not in st.session_state:
        st.session_state.history = []

    for msg in st.session_state.history:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(msg.content)

    question = st.chat_input("Digite sua pergunta...")

    if question:
        st.session_state.history.append(HumanMessage(content=question))
        with st.chat_message("user"):
            st.markdown(question)

        try:
            graph = get_graph()
        except FileNotFoundError as e:
            with st.chat_message("assistant"):
                st.error(str(e))
            return

        result = graph.invoke({"messages": st.session_state.history})
        answer = result["messages"][-1]
        st.session_state.history.append(answer)

        with st.chat_message("assistant"):
            st.markdown(answer.content)

        if dev_mode:
            with st.sidebar.expander("🔍 Debug RAG", expanded=True):
                docs = result.get("retrieved_docs", [])
                st.write(f"**Chunks recuperados:** {len(docs)}")
                st.write(f"**Modelo de embeddings:** {EMBEDDING_MODEL}")
                st.write(f"**Modelo LLM:** {GROQ_MODEL} (groq)")
                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"**Chunk {i}** — página: {doc.get('page', 'N/A')}")
                    st.text(doc["content"])


if __name__ == "__main__":
    main()