import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.utils.pdf_loader import (
    extract_text_from_pdf
)

from app.services.rag.chunking import (
    chunk_text
)

from app.services.embeddings.embedding_generator import (
    create_embedding
)

from app.database.faiss_db import (
    add_vector
)

router = APIRouter()


UPLOAD_DIR = "data/raw_documents"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")


async def upload_pdf(
        file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)

    # Extract Text
    text = extract_text_from_pdf(
        file_path
    )

    # Chunk Text
    chunks = chunk_text(text)

    # Generate Embeddings
    for chunk in chunks:

        embedding = create_embedding(
            chunk
        )

        add_vector(
            embedding,
            chunk
        )

    return {
        "message": "PDF uploaded successfully",
        "chunks_stored": len(chunks)
    }