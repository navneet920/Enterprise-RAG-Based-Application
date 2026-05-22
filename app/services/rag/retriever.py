from app.services.rag.hybrid_search import hybrid_search


def retrieve_documents(
        query: str,
        top_k=5
):


    results = hybrid_search(
        query,
        top_k
    )

    return results