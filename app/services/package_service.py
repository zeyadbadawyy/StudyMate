import os
import zipfile

from app.database.models import Generation
from app.services.pdf_export import export_pdf


def build_study_package(db):

    os.makedirs(
        "exports",
        exist_ok=True
    )

    zip_path = (
        "exports/StudyPackage.zip"
    )

    latest_types = [
        "summary",
        "flashcards",
        "quiz",
        "exam",
        "study-guide",
        "revision-notes"
    ]

    pdf_files = []

    for generation_type in latest_types:

        generation = (
            db.query(Generation)
            .filter(
                Generation.generation_type
                == generation_type
            )
            .order_by(
                Generation.id.desc()
            )
            .first()
        )

        if not generation:
            continue

        pdf_name = (
            f"{generation_type}.pdf"
        )

        pdf_path = export_pdf(
            generation.content,
            pdf_name
        )

        pdf_files.append(
            pdf_path
        )

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for pdf_file in pdf_files:

            zipf.write(
                pdf_file,
                arcname=os.path.basename(
                    pdf_file
                )
            )

    return zip_path