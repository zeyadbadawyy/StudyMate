from fastapi import APIRouter
from pydantic import BaseModel

from app.services import document_store
from app.services.ai_service import ask_document

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(
    request: ChatRequest
):

    if not document_store.current_document:
        return {
            "error": "No PDF uploaded"
        }

    result = ask_document(
        document_store.current_document,
        request.question
    )

    return {
        "answer": result
    }