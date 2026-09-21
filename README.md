Assistente de atendimento hoteleiro via RAG. Responde perguntas dos hóspedes com base em uma fonte de conhecimento local, 
sem alucinar informações fora do contexto recuperado.

🛠️ *Stack:*

Streamlit - interface de chat

LangGraph — orquestração do fluxo (state machine: retrieve → generate)

LangChain — loaders, text splitting, integração com vectorstore e LLM

ChromaDB — vectorstore local, persistido em disco

HuggingFace / Sentence Transformers — modelo de embeddings (all-MiniLM-L6-v2)

PyTorch — engine de inferência dos embeddings (CPU/GPU)

Groq — inferência do LLM (openai/gpt-oss-20b por padrão)
