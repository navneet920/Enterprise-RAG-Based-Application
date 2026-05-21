from fastapi import FastAPI

from app.api.routes.chat_routes import (
    router as chat_router
)
from app.api.routes.upload_routes import (
    router as upload_router
)
app = FastAPI(
    title="RAG Enterprise Backend",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    }