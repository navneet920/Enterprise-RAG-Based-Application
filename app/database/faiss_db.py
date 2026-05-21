import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

document_store = []


def add_vector(vector, chunk):

    vector = np.array([vector]).astype("float32")

    index.add(vector)

    document_store.append(chunk)


def search_vector(vector, top_k=5):

    vector = np.array([vector]).astype("float32")

    distances, indices = index.search(
        vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(document_store):

            results.append(
                document_store[idx]
            )

    return results