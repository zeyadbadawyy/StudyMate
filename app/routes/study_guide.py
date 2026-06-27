from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services import document_store
from app.services.ai_service import generate_study_guide
from app.services.history_service import (
    save_generation
)

router = APIRouter()


@router.post("/study-guide")
async def study_guide(db: Session = Depends(get_db)):

    if not document_store.current_document:
        return {
            "error": "No PDF uploaded"
        }

    result = generate_study_guide(
        document_store.current_document
    )

    save_generation(
        db=db,
        generation_type="study-guide",
        content=result,
        document_name=document_store.current_filename
    )

    return {
        "type": "study-guide",
        "content": result
    }