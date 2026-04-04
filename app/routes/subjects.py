from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import db_models as models
from ..database import get_db
from ..schemas.resources import VideoResponse
from ..schemas.subjects import SubjectCreate, SubjectResponse, SubjectUpdate

router = APIRouter(prefix="/resources")


# -------------------------------
# CREATE SUBJECT
# -------------------------------
@router.post("/subjects", response_model=SubjectResponse, tags=["Admin-Resources"])
def create_subject(data: SubjectCreate, db: Session = Depends(get_db)):

    branch = db.query(models.Branch).filter(models.Branch.id == data.branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    subject = models.Subject(name=data.name, branch_id=data.branch_id)

    db.add(subject)
    db.commit()
    db.refresh(subject)

    return subject


# -------------------------------
# GET VIDEOS BY SUBJECT
# -------------------------------
@router.get(
    "/videos/{subject_id}", response_model=list[VideoResponse], tags=["User-Resources"]
)
def get_videos(subject_id: UUID, db: Session = Depends(get_db)):

    videos = (
        db.query(models.VideoResource)
        .filter(
            models.VideoResource.subject_id == subject_id,
            models.VideoResource.is_deleted.is_(False),
        )
        .all()
    )

    if not videos:
        raise HTTPException(status_code=404, detail="No videos found for this subject")

    return videos


# -------------------------------
# UPDATE SUBJECT
# -------------------------------
@router.patch(
    "/subjects/{subject_id}", response_model=SubjectResponse, tags=["Admin-Resources"]
)
def update_subject(
    subject_id: UUID, data: SubjectUpdate, db: Session = Depends(get_db)
):

    subject = db.query(models.Subject).filter(models.Subject.id == subject_id).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    if data.name is not None:
        subject.name = data.name

    if data.branch_id is not None:
        branch = (
            db.query(models.Branch).filter(models.Branch.id == data.branch_id).first()
        )
        if not branch:
            raise HTTPException(status_code=404, detail="Branch not found")
        subject.branch_id = data.branch_id

    db.commit()
    db.refresh(subject)

    return subject


# -------------------------------
# DELETE SUBJECT
# -------------------------------
@router.delete("/subjects/{subject_id}", tags=["Admin-Resources"])
def delete_subject(subject_id: UUID, db: Session = Depends(get_db)):

    subject = db.query(models.Subject).filter(
        models.Subject.id == subject_id, models.Subject.is_deleted.is_(False)
    )

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # check active videos
    active_videos = [v for v in subject.videos if not v.is_deleted]

    if active_videos:
        # SOFT DELETE
        subject.is_deleted = True
        db.commit()
        return {"message": "Subject soft deleted (has videos)"}
    else:
        # HARD DELETE
        db.delete(subject)
        db.commit()
        return {"message": "Subject permanently deleted"}
