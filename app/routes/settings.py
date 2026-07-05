from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import UserSettings

router = APIRouter()


@router.get("/settings")
def get_settings(
    db: Session = Depends(get_db)
):

    settings = (
        db.query(
            UserSettings
        ).first()
    )

    if not settings:

        settings = UserSettings()

        db.add(settings)

        db.commit()

        db.refresh(settings)

    return settings


@router.put("/settings")
def update_settings(
    payload: dict,
    db: Session = Depends(get_db)
):

    settings = (
        db.query(
            UserSettings
        ).first()
    )

    if not settings:

        settings = UserSettings()

        db.add(settings)

        db.commit()

        db.refresh(settings)

    for key, value in payload.items():

        setattr(
            settings,
            key,
            value
        )

    db.commit()

    db.refresh(settings)

    return settings