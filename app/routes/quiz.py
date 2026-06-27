from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services import document_store
from app.services.ai_service import generate_quiz
from app.services.history_service import (
    save_generation
)

from app.models.generation import GenerationRequest

router = APIRouter()


@router.post("/quiz")
async def quiz(
    request: GenerationRequest,
    db: Session = Depends(get_db)
):

    if not document_store.current_document:
        return {
            "error": "No PDF uploaded"
        }

    result = generate_quiz(
        document_store.current_document,
        request.difficulty,
        request.count
    )

    save_generation(
        db=db,
        generation_type="quiz",
        content=result,
        document_name=document_store.current_filename
    )

    return {
        "type": "quiz",
        "content": result
    }