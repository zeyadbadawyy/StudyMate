import os

from app.services.pdf_service import (
    extract_text_from_pdf
)

from app.services.docx_service import (
    extract_text_from_docx
)

from app.services.txt_service import (
    extract_text_from_txt
)


def extract_text(
    file_path: str
):

    extension = (
        os.path.splitext(file_path)[1]
        .lower()
    )

    if extension == ".pdf":
        return extract_text_from_pdf(
            file_path
        )

    if extension == ".docx":
        return extract_text_from_docx(
            file_path
        )

    if extension == ".txt":
        return extract_text_from_txt(
            file_path
        )

    raise ValueError(
        "Unsupported file type"
    )