from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    ),
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "poolside/laguna-xs.2:free"
)


def ask_ai(prompt: str):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_summary(text: str):

    prompt = f"""
You are an expert academic study assistant.

Task:
Create a concise but comprehensive summary of the provided study material.

Rules:
- Use ONLY information from the document.
- Do not invent information.
- Organize content logically.
- Use headings where appropriate.
- Highlight the most important concepts.
- Keep explanations easy to understand.
- Do not include unnecessary introductions.

Format:

OVERVIEW

KEY CONCEPTS

IMPORTANT DETAILS

FINAL TAKEAWAYS

DOCUMENT:

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
    document: str,
    difficulty="medium",
    count=10
):

    prompt = f"""
You are an expert study assistant.

Create exactly {count} high-quality flashcards.

Difficulty Level: {difficulty}

Rules:
- Use only information from the document.
- Questions should test understanding.
- Answers should be concise.
- Do not use markdown.
- Do not use bullet points.
- Follow the format exactly.

Format:

FLASHCARD 1

Question:
...

Answer:
...

FLASHCARD 2

Question:
...

Answer:
...

DOCUMENT:

{document[:20000]}
"""

    return ask_ai(prompt)


def generate_quiz(
    document: str,
    difficulty="medium",
    count=10
):

    prompt = f"""
Generate exactly {count} multiple-choice questions.

Difficulty Level: {difficulty}

Rules:
- Use only information from the document.
- Four choices per question.
- No explanations.
- Make questions educational and exam-like.
- Provide four choices for every question.
- Provide exactly one correct answer.
- Do not add explanations.

Format exactly:

QUESTION 1
A)
B)
C)
D)

Correct Answer:

QUESTION 2
A)
B)
C)
D)

Correct Answer:

DOCUMENT:

{document[:20000]}
"""

    return ask_ai(prompt)


def generate_study_guide(
    document: str
):

    prompt = f"""
Create a complete study guide.

Rules:
- Use only information from the document.
- Organize content clearly.
- Focus on exam preparation.
- Do not add outside knowledge.

Format:

CHAPTER OVERVIEW

KEY CONCEPTS

IMPORTANT DEFINITIONS

EXAMPLES

COMMON EXAM TOPICS

PRACTICE QUESTIONS

DOCUMENT:

{document[:20000]}
"""

    return ask_ai(prompt)


def generate_exam(
    document: str,
    difficulty="medium"
):

    prompt = f"""
Create a complete examination paper.

Difficulty Level: {difficulty}

Rules:
- Use only the document.
- Make questions educational and realistic.
- Do not provide solutions.
- Follow the format exactly.

Format:

PART A - MULTIPLE CHOICE

PART B - TRUE OR FALSE

PART C - SHORT ANSWER

PART D - ESSAY QUESTIONS

DOCUMENT:

{document[:20000]}
"""

    return ask_ai(prompt)


def generate_revision_notes(
    document: str
):

    prompt = f"""
Create concise revision notes.

Rules:
- Use only the document.
- Focus on high-value exam content.
- Keep notes compact.
- Highlight important facts.
- Do not add outside information.

Format:

MUST KNOW CONCEPTS

IMPORTANT DEFINITIONS

KEY FACTS

IMPORTANT EXAMPLES

EXAM TIPS

LAST MINUTE REVISION

DOCUMENT:

{document[:20000]}
"""

    return ask_ai(prompt)