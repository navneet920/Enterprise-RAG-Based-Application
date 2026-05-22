from app.services.llm.huggingface_service import (
    generate_response
)

from app.services.rag.retriever import (
    retrieve_documents
)

from app.services.rag.memory_manager import (
    save_message,
    get_conversation
)

def generate_rag_response(query: str):


    documents = retrieve_documents(query)

    context = "\n".join(
        [doc["text"] for doc in documents]
    )
    memory = get_conversation()
    memory_text=""

    for msg in memory:
        memory_text+=(
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    prompt = f"""
You are an intelligent AI assistant.

Answer the question ONLY from the
provided context.

conversation history:
{memory_text}

Context:
{context}

Question:
{query}

Answer:
"""


    response = generate_response(prompt)

    save_message("user", query)

    save_message("assistant", response)


    return {
        "response": response,
        "sources": documents,
    }