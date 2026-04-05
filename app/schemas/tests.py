from typing import Dict, List, Optional, Union
from uuid import UUID
from pydantic import BaseModel, field_validator


class OptionOut(BaseModel):
    id: UUID
    option_text: str

    class Config:
        from_attributes = True

class QuestionOut(BaseModel):
    id: UUID
    question_text: str
    question_type: str
    marks: float

    # For MCQ/MSQ
    options: Optional[List[OptionOut]] = None

    # For NAT
    numerical_answer: Optional[float] = None
    tolerance: Optional[float] = None

    class Config:
        from_attributes = True

class TestOut(BaseModel):
    id: UUID
    questions: List[QuestionOut]

    class Config:
        from_attributes = True

class SubmitTest(BaseModel):
    answers: Dict[str, Union[List[str], float]]

    @field_validator('answers')
    @classmethod
    def validate_keys_are_uuids(cls, v):
        for key in v:
            try:
                UUID(key)
            except ValueError:
                raise ValueError(f"Invalid UUID key: {key}")
        return v

class TestResult(BaseModel):
    score: int
    total: int
    percentage: float

class GenerateTestRequest(BaseModel):
    test_type: str  # "subject" or "full"
    subject_id: Optional[UUID] = None
    branch_id: Optional[UUID] = None
    num_questions: Optional[int] = 10