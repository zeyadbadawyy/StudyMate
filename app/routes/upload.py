from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

import os

from app.services.file_service import (
    extract_text
)

from app.services import document_store
from app.services.chunk_service import (
    chunk_text
)
from app.services import chat_memory

from sqlalchemy.orm import Session

from app.database.models import Document
from app.database.dependencies import get_db


router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    allowed_extensions = [
        ".pdf",
        ".docx",
        ".txt"
    ]

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in allowed_extensions:
        return {
            "error":
            "Only PDF, DOCX and TXT files are allowed"
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

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    text = extract_text(
        file_path
    )

    document_store.current_document = text

    document_store.current_chunks = (
        chunk_text(text)
    )

    document_store.current_filename = (
        file.filename
    )
    
    chat_memory.conversation_history.clear()

    print(
        f"Chunks: {len(document_store.current_chunks)}"
    )

    new_document = Document(
        filename=file.filename,
        filepath=file_path,
        is_active=True
    )

    db.add(new_document)

    db.commit()

    db.refresh(
        new_document
    )

    return {
        "success": True,
        "document_id": new_document.id,
        "filename": file.filename,
        "file_type": extension,
        "characters": len(text),
        "chunks": len(
            document_store.current_chunks
        )
    }