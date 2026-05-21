from app.services.embeddings.embedding_generator import (
    create_embedding
)

from app.database.faiss_db import (
    search_vector
)


def retrieve_documents(
        query: str,
        top_k=5
):

    query_embedding = create_embedding(
        query
    )

    results = search_vector(
        query_embedding,
        top_k
    )

    return results