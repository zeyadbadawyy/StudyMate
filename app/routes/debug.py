from fastapi import APIRouter
from app.services import document_store

router = APIRouter()


@router.get("/document")
def get_document():

    return {
        "characters":
        len(document_store.current_document)
    }