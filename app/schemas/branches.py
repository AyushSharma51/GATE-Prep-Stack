from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, field_validator
from .enums import GateBranch


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
    id: UUID
    name: GateBranch

    model_config = ConfigDict(from_attributes=True)
