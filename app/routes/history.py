from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import Generation

router = APIRouter()


@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):

    history = (
        db.query(Generation)
        .order_by(
            Generation.id.desc()
        )
        .all()
    )

    return history

@router.delete(
    "/history/clear"
)
def clear_history(
    db: Session = Depends(
        get_db
    )
):

    db.query(
        Generation
    ).delete()

    db.commit()

    return {
        "success": True
    }