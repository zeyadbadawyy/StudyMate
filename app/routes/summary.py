from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services import document_store
from app.services.ai_service import generate_summary
from app.services.history_service import (
    save_generation
)

router = APIRouter()


@router.post("/summary")
async def summary(db: Session = Depends(get_db)):

    if not document_store.current_document:

        return {
            "error":
            "No document uploaded"
        }

    result = generate_summary(
        document_store.current_document
    )

    save_generation(
        db=db,
        generation_type="summary",
        content=result,
        document_name=document_store.current_filename
    )
    
    return {
        "type": "summary",
        "content": result
    }