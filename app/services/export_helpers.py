from app.services.pdf_export import export_pdf


def export_generated_content(
    content: str,
    filename: str
):
    return export_pdf(
        content,
        filename
    )