from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.models.export import ExportRequest
from app.services.pdf_export import export_pdf

router = APIRouter()


@router.post("/export/pdf")
async def export_to_pdf(
    request: ExportRequest
):

    pdf_path = export_pdf(
        request.content,
        request.filename
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=request.filename
    )