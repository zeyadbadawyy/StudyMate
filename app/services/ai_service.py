from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    ),
)


def ask_ai(
    prompt: str
):

    response = client.chat.completions.create(
        model="poolside/laguna-xs.2:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_summary(
    text: str
):

    prompt = f"""
    Summarize the following study material.

    {text[:20000]}
    """

    return ask_ai(prompt)

def ask_document(
    document: str,
    question: str
):

    prompt = f"""
You are a study assistant.

Use ONLY the provided document to answer.

DOCUMENT:
{document[:20000]}

QUESTION:
{question}

Provide a clear and concise answer.
"""

    return ask_ai(prompt)

def generate_flashcards(
    document: str
):

    prompt = f"""
    Create 10 study flashcards from the document.

    Return them in this format:

    Q: Question
    A: Answer

    DOCUMENT:

    {document[:20000]}
    """

    return ask_ai(prompt)

def generate_quiz(
    document: str
):

    prompt = f"""
    Generate 10 multiple-choice questions.

    Format:

    Question:
    A)
    B)
    C)
    D)

    Correct Answer:

    DOCUMENT:

    {document[:20000]}
    """

    return ask_ai(prompt)