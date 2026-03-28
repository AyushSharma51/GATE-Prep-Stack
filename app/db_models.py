import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID  # Use this for Postgres-specific UUID
from sqlalchemy.orm import relationship
from .database import Base

class Branch(Base):
    __tablename__ = "branches"

    # Set primary_key to UUID with a default generator
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, unique=True, index=True)
    is_deleted = Column(Boolean, default=False)

    subjects = relationship("Subject", back_populates="branch")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    
    # ForeignKey updated to UUID type
    branch_id = Column(UUID(as_uuid=True), ForeignKey("branches.id"))
    is_deleted = Column(Boolean, default=False)

    branch = relationship("Branch", back_populates="subjects")
    videos = relationship("VideoResource", back_populates="subject")


class VideoResource(Base):
    __tablename__ = "video_resources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, index=True)
    is_deleted = Column(Boolean, default=False)

    playlist_url = Column(String)
    
    # ForeignKey updated to UUID type
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"))

    subject = relationship("Subject", back_populates="videos")