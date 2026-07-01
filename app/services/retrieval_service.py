import re


def normalize_text(text):

    text = text.lower()

    text = re.sub(
        r"[^\w\s]",
        " ",
        text
    )

    return text


def retrieve_relevant_chunks(
    chunks,
    query,
    top_k=5
):

    query_words = set(
        normalize_text(query).split()
    )

    scored_chunks = []

    seen_chunks = set()

    for chunk in chunks:

        normalized_chunk = normalize_text(
            chunk
        )

        chunk_words = set(
            normalized_chunk.split()
        )

        score = len(
            query_words.intersection(
                chunk_words
            )
        )

        if score > 0:

            chunk_key = normalized_chunk[:200]

            if chunk_key not in seen_chunks:

                seen_chunks.add(
                    chunk_key
                )

                scored_chunks.append(
                    (score, chunk)
                )

    scored_chunks.sort(
        key=lambda x: x[0],
        reverse=True
    )

    results = [
        chunk
        for score, chunk
        in scored_chunks[:top_k]
    ]

    if not results:

        results = chunks[:top_k]

    return results