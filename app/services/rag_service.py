def get_generation_context(
    chunks,
    max_chunks=20
):
    """
    Select chunks spread across the document
    instead of only using the beginning.
    """

    if not chunks:
        return ""

    if len(chunks) <= max_chunks:
        return "\n\n".join(chunks)

    step = len(chunks) // max_chunks

    selected_chunks = []

    for i in range(
        0,
        len(chunks),
        step
    ):
        selected_chunks.append(
            chunks[i]
        )

        if len(selected_chunks) >= max_chunks:
            break

    return "\n\n".join(
        selected_chunks
    )