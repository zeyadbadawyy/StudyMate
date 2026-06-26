from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from app.services.pdf_service import extract_text_from_pdf
from app.services import document_store

router = APIRouter()


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed"
        }

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    # Save file FIRST
    with open(
        file_path,
        "wb",
    ) as buffer:
        buffer.write(
            await file.read()
        )

    # Then extract text
    text = extract_text_from_pdf(
        file_path
    )

    document_store.current_document = text

    return {
        "success": True,
        "filename": file.filename,
        "characters": len(text),
        "pages_estimate": len(text.split("\n"))
    }