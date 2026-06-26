from fastapi import APIRouter

from app.services import document_store
from app.services.ai_service import generate_summary

router = APIRouter()


@router.post("/summary")
async def summary():

    if not document_store.current_document:

        return {
            "error":
            "No document uploaded"
        }

    result = generate_summary(
        document_store.current_document
    )

    return {
        "summary": result
    }