from app.database.models import Generation


def save_generation(
    db,
    generation_type,
    content,
    document_name
):

    record = Generation(
        generation_type=generation_type,
        content=content,
        document_name=document_name
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record