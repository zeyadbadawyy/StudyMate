from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from app.services.pdf_service import extract_text_from_pdf
from app.services import document_store

from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.models import Document
from app.database.dependencies import get_db


router = APIRouter()


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
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
    db.query(Document).update(
        {
            Document.is_active: False
        }
    )

    db.commit()

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
    document_store.current_filename = file.filename

    new_document = Document(
        filename=file.filename,
        filepath=file_path,
        is_active=True
    )

    db.add(new_document)

    db.commit()

    db.refresh(new_document)

    return {
        "success": True,
        "document_id": new_document.id,
        "filename": file.filename,
        "characters": len(text),
        "pages_estimate": len(text.split("\n"))
    }