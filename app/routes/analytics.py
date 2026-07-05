from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.dependencies import get_db
from app.database.models import (
    Generation,
    Document
)

router = APIRouter()


@router.get(
    "/analytics"
)
def get_analytics(
    db: Session = Depends(
        get_db
    )
):

    generations_count = (
        db.query(
            Generation
        ).count()
    )

    documents_count = (
        db.query(
            Document
        ).count()
    )

    summary_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "summary"
        )
        .count()
    )

    flashcards_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "flashcards"
        )
        .count()
    )

    quiz_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "quiz"
        )
        .count()
    )

    exam_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "exam"
        )
        .count()
    )

    study_guide_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "study-guide"
        )
        .count()
    )

    revision_notes_count = (
        db.query(
            Generation
        )
        .filter(
            Generation.generation_type
            == "revision-notes"
        )
        .count()
    )

    most_used = (
        db.query(
            Generation.generation_type,
            func.count(
                Generation.id
            ).label("count")
        )
        .group_by(
            Generation.generation_type
        )
        .order_by(
            func.count(
                Generation.id
            ).desc()
        )
        .first()
    )

    latest = (
        db.query(
            Generation
        )
        .order_by(
            Generation.id.desc()
        )
        .first()
    )

    return {
        "documents_uploaded":
            documents_count,

        "generations_created":
            generations_count,

        "summary_count":
            summary_count,

        "flashcards_count":
            flashcards_count,

        "quiz_count":
            quiz_count,

        "exam_count":
            exam_count,

        "study_guide_count":
            study_guide_count,

        "revision_notes_count":
            revision_notes_count,

        "most_used_tool":
            most_used[0]
            if most_used
            else None,

        "latest_activity":
            latest.generation_type
            if latest
            else None,

        "latest_activity_time":
            latest.created_at
            if latest
            else None
    }