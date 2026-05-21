from app.services.embeddings.embedding_model import (
    embedding_model
)


def create_embedding(text: str):

    embedding = embedding_model.encode(text)

    return embedding.tolist()