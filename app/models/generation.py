from pydantic import BaseModel


class GenerationRequest(BaseModel):
    difficulty: str = "medium"
    count: int = 10