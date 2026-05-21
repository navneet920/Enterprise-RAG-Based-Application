from fastapi import APIRouter

from app.services.llm.huggingface_service import (
    generate_response
)

router = APIRouter()


@router.get("/chat")
def chat(q: str):

    response = generate_response(q)

    return {
        "response": response
    }