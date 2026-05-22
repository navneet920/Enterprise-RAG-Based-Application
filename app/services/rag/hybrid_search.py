from rank_bm25 import BM25Okapi

from app.database.faiss_db import (
    document_store
)

from app.services.embeddings.embedding_generator import (
    create_embedding
)

from app.database.faiss_db import (
    search_vector
)


def keyword_search(
        query,
        top_k=5
):

    corpus = [
        doc["text"]
        for doc in document_store
    ]

    tokenized_corpus = [
        doc.split(" ")
        for doc in corpus
    ]

    bm25 = BM25Okapi(
        tokenized_corpus
    )

    tokenized_query = query.split(" ")

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    results = []

    for idx in ranked_indices:

        results.append(
            document_store[idx]
        )

    return results


def hybrid_search(
        query,
        top_k=5
):

    # Semantic Search
    query_embedding = create_embedding(
        query
    )

    semantic_results = search_vector(
        query_embedding,
        top_k
    )

    # Keyword Search
    keyword_results = keyword_search(
        query,
        top_k
    )

    combined_results = []

    seen_texts = set()

    for result in (
        semantic_results +
        keyword_results
    ):

        if result["text"] not in seen_texts:

            combined_results.append(
                result
            )

            seen_texts.add(
                result["text"]
            )

    return combined_results[:top_k]