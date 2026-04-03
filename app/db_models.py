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

class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    test_id = Column(UUID(as_uuid=True), ForeignKey("tests.id"), nullable=False)
    question_text = Column(String, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_option = Column(String, nullable=False)

    test = relationship("Test", back_populates="questions")


class Test(Base):
    __tablename__ = "tests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"), nullable=False)

    questions = relationship("Question", back_populates="test", cascade="all, delete")