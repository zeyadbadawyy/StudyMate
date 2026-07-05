from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.package_service import (
    build_study_package
)

router = APIRouter()


@router.post(
    "/package/download"
)
def download_package(
    db: Session = Depends(
        get_db
    )
):

    zip_path = (
        build_study_package(db)
    )

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="StudyPackage.zip"
    )