from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import db_models as models
from ..schemas.subjects import SubjectCreate, SubjectUpdate


def create_a_new_subject(data: SubjectCreate, db: Session):
    branch = db.query(models.Branch).filter(models.Branch.id == data.branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    subject = models.Subject(name=data.name, branch_id=data.branch_id)

    db.add(subject)
    db.commit()
    db.refresh(subject)

    return subject


def get_videos_by_subject(subject_id: UUID, db: Session):
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


def update_a_subject(subject_id: UUID, data: SubjectUpdate, db: Session):

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


def delete_a_subject(subject_id: UUID, db: Session):

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
