from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router
from app.routes.summary import router as summary_router
from app.routes.quiz import router as quiz_router
from app.routes.flashcards import router as flashcards_router
from app.routes.debug import router as debug_router


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
    debug_router,
    tags=["Debug"]
)

@app.get("/")
def root():
    return {
        "message": "StudyMate API Running"
    }