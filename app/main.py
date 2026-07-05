from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router
from app.routes.summary import router as summary_router
from app.routes.quiz import router as quiz_router
from app.routes.flashcards import router as flashcards_router
from app.routes.study_guide import router as study_guide_router
from app.routes.exam import router as exam_router
from app.routes.revision_notes import router as revision_notes_router
from app.routes.export import router as export_router
from app.routes.document import router as document_router
from app.routes.history import (
    router as history_router
)
from app.routes.settings import router as settings_router
from app.routes.package import (
    router as package_router
)
from app.routes.analytics import (
    router as analytics_router
)

from app.database.database import engine
from app.database.models import Base
from app.database.database import SessionLocal
from app.database.models import Document

import os

from app.services import document_store
from app.services.file_service import (
    extract_text
)
from app.services.chunk_service import (
    chunk_text
)

def restore_active_document():

    db = SessionLocal()

    try:

        active_document = (
            db.query(Document)
            .filter(
                Document.is_active == True
            )
            .first()
        )

        if not active_document:
            return

        if not os.path.exists(
            active_document.filepath
        ):
            return

        text = extract_text(
            active_document.filepath
        )

        document_store.current_chunks = (
            chunk_text(text)
        )

        document_store.current_document = text

        document_store.current_filename = (
            active_document.filename
        )

        print(
            f"Loaded: {active_document.filename}"
        )

    finally:

        db.close()

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="StudyMate API",
    description="""
AI-powered study assistant.

Features:
- PDF Upload
- AI Summary
- Flashcards
- Quiz Generation
- Question Answering
""",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

restore_active_document()

@app.get(
    "/health",
    tags=["Health"]
)
def health():

    return {
        "status": "ok"
    }

app.include_router(
    upload_router,
    tags=["Upload"]
)

app.include_router(
    chat_router,
    tags=["Chat"]
)

app.include_router(
    summary_router,
    tags=["Summary"]
)

app.include_router(
    flashcards_router,
    tags=["Flashcards"]
)

app.include_router(
    quiz_router,
    tags=["Quiz"]
)

app.include_router(
    study_guide_router,
    tags=["Study Guide"]
)

app.include_router(
    exam_router,
    tags=["Exam"]
)

app.include_router(
    revision_notes_router,
    tags=["Revision Notes"]
)

app.include_router(
    export_router,
    tags=["Export"]
)

app.include_router(
    document_router,
    tags=["Document"]
)

app.include_router(
    history_router,
    tags=["History"]
)

app.include_router(
    settings_router,
    tags=["Settings"]
)

app.include_router(
    package_router,
    tags=["Package"]
)

app.include_router(
    analytics_router,
    tags=["Analytics"]
)

@app.get("/")
def root():
    return {
        "message": "StudyMate API Running"
    }