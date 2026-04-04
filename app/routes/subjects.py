from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.subject_services import (
    create_a_new_subject,
    delete_a_subject,
    get_videos_by_subject,
    update_a_subject,
)
from ..database import get_db
from ..schemas.resources import VideoResponse
from ..schemas.subjects import SubjectCreate, SubjectResponse, SubjectUpdate

router = APIRouter(prefix="/resources")


# -------------------------------
# CREATE SUBJECT
# -------------------------------
@router.post("/subjects", response_model=SubjectResponse, tags=["Admin-Resources"])
def create_subject(data: SubjectCreate, db: Session = Depends(get_db)):

    return create_a_new_subject(data, db)


# -------------------------------
# GET VIDEOS BY SUBJECT
# -------------------------------
@router.get(
    "/videos/{subject_id}", response_model=list[VideoResponse], tags=["User-Resources"]
)
def get_videos(subject_id: UUID, db: Session = Depends(get_db)):

    return get_videos_by_subject(subject_id, db)


# -------------------------------
# UPDATE SUBJECT
# -------------------------------
@router.patch(
    "/subjects/{subject_id}", response_model=SubjectResponse, tags=["Admin-Resources"]
)
def update_subject(
    subject_id: UUID, data: SubjectUpdate, db: Session = Depends(get_db)
):

    return update_a_subject(subject_id, data, db)


# -------------------------------
# DELETE SUBJECT
# -------------------------------
@router.delete("/subjects/{subject_id}", tags=["Admin-Resources"])
def delete_subject(subject_id: UUID, db: Session = Depends(get_db)):

    return delete_a_subject(subject_id, db)
