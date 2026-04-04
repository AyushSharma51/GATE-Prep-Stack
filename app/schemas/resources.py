from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator
from .subjects import SubjectResponse


class VideoCreate(BaseModel):
    title: str
    playlist_url: HttpUrl
    subject_id: UUID

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title", mode="before")
    def normalize_name_for_VideoCreate(cls, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("title cannot be empty")
        return value.strip().lower()


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    playlist_url: Optional[HttpUrl] = None
    subject_id: Optional[UUID] = None

    model_config = ConfigDict(from_attributes=True)


class VideoResponse(BaseModel):
    id: UUID
    title: str
    playlist_url: HttpUrl
    subject: SubjectResponse

    model_config = ConfigDict(from_attributes=True)
