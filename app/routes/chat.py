from fastapi import APIRouter
from pydantic import BaseModel

from app.services import document_store
from app.services.ai_service import ask_document
from app.services.retrieval_service import (
    retrieve_relevant_chunks
)

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

    relevant_chunks = (
        retrieve_relevant_chunks(
            document_store.current_chunks,
            request.question
        )
    )

    print(
        f"Retrieved {len(relevant_chunks)} chunks"
    )
    

    context = "\n\n".join(
        relevant_chunks
    )

    result = ask_document(
        context,
        request.question
    )

    return {
        "answer": result
    }