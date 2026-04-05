import uuid
from sqlalchemy import Column, Float, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID  # Use this for Postgres-specific UUID
from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum 


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



class QuestionType(str,Enum):
    MCQ = "mcq"      # single correct
    MSQ = "msq"      # multiple correct
    NAT = "nat"      # numerical answer


class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    test_id = Column(UUID(as_uuid=True), ForeignKey("tests.id"), nullable=False)

    question_text = Column(String, nullable=False)
    question_type = Column(String, nullable=False)
    marks = Column(Float, nullable=False)

    # For NAT questions 
    numerical_answer = Column(Float, nullable=True)
    tolerance = Column(Float, nullable=True)  # optional (for range answers)

    test = relationship("Test", back_populates="questions")
    options = relationship("Option", back_populates="question", cascade="all, delete")

class Option(Base):
    __tablename__ = "options"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)

    option_text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)

    question = relationship("Question", back_populates="options")

class Test(Base):
    __tablename__ = "tests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"), nullable=False)

    questions = relationship("Question", back_populates="test", cascade="all, delete")