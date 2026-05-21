from app.services.llm.huggingface_service import (
    generate_response
)

from app.services.rag.retriever import (
    retrieve_documents
)


def generate_rag_response(query: str):

    documents = retrieve_documents(query)

    context = "\n".join(documents)

    prompt = f"""
You are an intelligent AI assistant.

Answer the question ONLY from the
provided context.

Context:
{context}

Question:
{query}

Answer:
"""

    response = generate_response(prompt)

    return {
        "question": query,
        "context": documents,
        "response": response
    }