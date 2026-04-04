from typing import Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: UUID
    question_text: str
    options: Dict[str, str]

    class Config:
        from_attributes = True


class TestOut(BaseModel):
    id: UUID
    questions: List[QuestionOut]


class SubmitTest(BaseModel):
    answers: Dict[UUID, str]


class TestResult(BaseModel):
    score: int
    total: int
    percentage: float


class GenerateTestRequest(BaseModel):
    test_type: str  # "subject" or "full"
    subject_id: Optional[UUID] = None
    branch_id: Optional[UUID] = None
    num_questions: Optional[int] = 10
