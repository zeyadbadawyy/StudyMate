from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services import document_store
from app.services.ai_service import generate_revision_notes
from app.services.history_service import (
    save_generation
)

router = APIRouter()


@router.post("/revision-notes")
async def revision_notes(db: Session = Depends(get_db)):

    if not document_store.current_document:
        return {
            "error": "No PDF uploaded"
        }

    result = generate_revision_notes(
        document_store.current_document
    )

    save_generation(
        db=db,
        generation_type="revision-notes",
        content=result,
        document_name=document_store.current_filename
    )

    return {
        "type": "revision-notes",
        "content": result
    }