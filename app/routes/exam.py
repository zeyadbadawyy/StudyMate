from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services import document_store
from app.services.ai_service import generate_exam
from app.services.history_service import (
    save_generation
)
from app.services.rag_service import (
    get_generation_context
)

from app.models.generation import GenerationRequest


router = APIRouter()


@router.post("/exam")
async def exam(
    request: GenerationRequest,
    db: Session = Depends(get_db)
):

    if not document_store.current_document:
        return {
            "error": "No PDF uploaded"
        }

    context = get_generation_context(
        document_store.current_chunks
    )
    
    result = generate_exam(
        context,
        request.difficulty
    )

    save_generation(
        db=db,
        generation_type="exam",
        content=result,
        document_name=document_store.current_filename
    )

    return {
        "type": "exam",
        "content": result
    }