from fastapi import APIRouter

from app.services.rag.response_generator import (
    generate_rag_response
)

router = APIRouter()


@router.get("/chat")
async def chat(q: str):

    response = generate_rag_response(q)

    return response