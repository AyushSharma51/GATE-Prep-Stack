from uuid import UUID
from pydantic import BaseModel, HttpUrl, field_validator, ConfigDict
from typing import Dict, List, Optional
from enum import Enum

# -------------------------------
# ENUM
# -------------------------------


class GateBranch(str, Enum):
    CSE = "cse"
    DA = "da"
    ME = "me"
    EE = "ee"
    CE = "ce"
    EC = "ec"

# Mapping for display
BRANCH_FULL_FORM = {
    "cse": "Computer Science and Engineering",
    "da": "Data Science and Artificial Intelligence",
    "me": "Mechanical Engineering",
    "ee": "Electrical Engineering",
    "ce": "Civil Engineering",
    "ec": "Electronics and Communication Engineering"
}

# -------------------------------
# BRANCH
# -------------------------------
class BranchCreate(BaseModel):
    name: GateBranch

    model_config = ConfigDict(from_attributes=True)

    @field_validator("name", mode="before")
    def normalize_name_for_BranchCreate(cls, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip().lower()

class BranchUpdate(BaseModel):
    name: Optional[GateBranch] = None

    model_config = ConfigDict(from_attributes=True)

class BranchResponse(BaseModel):
    id: UUID # Changed to UUID
    name: GateBranch

    model_config = ConfigDict(from_attributes=True)

# -------------------------------
# SUBJECT
# -------------------------------
class SubjectCreate(BaseModel):
    name: str
    branch_id: UUID # Changed to UUID

    model_config = ConfigDict(from_attributes=True)

    @field_validator("name", mode="before")
    def normalize_name_for_SubjectCreate(cls, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip().lower()

class SubjectUpdate(BaseModel):
    name: Optional[str] = None
    branch_id: Optional[UUID] = None # Changed to UUID

    model_config = ConfigDict(from_attributes=True)

class SubjectResponse(BaseModel):
    id: UUID # Changed to UUID
    name: str
    branch: BranchResponse

    model_config = ConfigDict(from_attributes=True)

# -------------------------------
# VIDEO RESOURCE
# -------------------------------
class VideoCreate(BaseModel):
    title: str
    playlist_url: HttpUrl
    subject_id: UUID # Changed to UUID

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title", mode="before")
    def normalize_name_for_VideoCreate(cls, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("title cannot be empty")
        return value.strip().lower()

class VideoUpdate(BaseModel):
    title: Optional[str] = None
    playlist_url: Optional[HttpUrl] = None
    subject_id: Optional[UUID] = None # Changed to UUID

    model_config = ConfigDict(from_attributes=True)

class VideoResponse(BaseModel):
    id: UUID # Changed to UUID
    title: str
    playlist_url: HttpUrl
    subject: SubjectResponse

    model_config = ConfigDict(from_attributes=True)

#----------------------------------------------
#------------------TEST------------------------
#----------------------------------------------

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
    test_type: str                  # "subject" or "full"
    subject_id: Optional[UUID] = None
    branch_id: Optional[UUID] = None
    num_questions: Optional[int] = 10