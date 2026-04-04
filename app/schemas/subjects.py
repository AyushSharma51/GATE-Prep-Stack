from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, field_validator
from .branches import BranchResponse


class SubjectCreate(BaseModel):
    name: str
    branch_id: UUID

    model_config = ConfigDict(from_attributes=True)

    @field_validator("name", mode="before")
    def normalize_name_for_SubjectCreate(cls, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip().lower()


class SubjectUpdate(BaseModel):
    name: Optional[str] = None
    branch_id: Optional[UUID] = None

    model_config = ConfigDict(from_attributes=True)


class SubjectResponse(BaseModel):
    id: UUID
    name: str
    branch: BranchResponse

    model_config = ConfigDict(from_attributes=True)
