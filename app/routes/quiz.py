from fastapi import APIRouter

from app.services import document_store
from app.services.ai_service import generate_quiz

router = APIRouter()


@router.post("/quiz")
async def quiz():

    if not document_store.current_document:

        return {
            "error": "No PDF uploaded"
        }

    result = generate_quiz(
        document_store.current_document
    )

    return {
        "quiz": result
    }