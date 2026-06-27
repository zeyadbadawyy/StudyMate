from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import Document

from app.services import document_store

router = APIRouter()


@router.get("/document/info")
async def document_info():

    if not document_store.current_document:
        return {
            "loaded": False
        }

    return {
        "loaded": True,
        "filename": document_store.current_filename,
        "characters": len(
            document_store.current_document
        ),
        "estimated_pages": len(
            document_store.current_document.split("\n")
        )
    }


@router.post("/document/clear")
async def clear_document(
    db: Session = Depends(get_db)
):

    document_store.current_document = ""
    document_store.current_filename = ""

    db.query(Document).update(
        {
            Document.is_active: False
        }
    )

    db.commit()

    return {
        "success": True,
        "message": "Document cleared"
    }