from fastapi import APIRouter

from app.services import document_store
from app.services.ai_service import generate_flashcards

router = APIRouter()


@router.post("/flashcards")
async def flashcards():

    if not document_store.current_document:

        return {
            "error": "No PDF uploaded"
        }

    result = generate_flashcards(
        document_store.current_document
    )

    return {
        "flashcards": result
    }