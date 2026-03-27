from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    subjects = relationship("Subject", back_populates="branch")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    branch_id = Column(Integer, ForeignKey("branches.id"))

    branch = relationship("Branch", back_populates="subjects")
    videos = relationship("VideoResource", back_populates="subject")


class VideoResource(Base):
    __tablename__ = "video_resources"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    playlist_url = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    subject = relationship("Subject", back_populates="videos")