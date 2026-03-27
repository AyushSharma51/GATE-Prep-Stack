from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import db_models as models

router = APIRouter(prefix="/resources", tags=["Resources"])


# Get all branches
@router.get("/branches")
def get_branches(db: Session = Depends(get_db)):
    branches = db.query(models.Branch).all()

    if not branches:
        raise HTTPException(status_code=404, detail="No branches found")

    return branches


#  Get subjects by branch
@router.get("/subjects/{branch_id}")
def get_subjects(branch_id: int, db: Session = Depends(get_db)):

    subjects = (
        db.query(models.Subject).filter(models.Subject.branch_id == branch_id).all()
    )

    if not subjects:
        raise HTTPException(status_code=404, detail="No subjects found for this branch")

    return subjects


#  Get videos by subject
@router.get("/videos/{subject_id}")
def get_videos(subject_id: int, db: Session = Depends(get_db)):

    videos = (
        db.query(models.VideoResource)
        .filter(models.VideoResource.subject_id == subject_id)
        .all()
    )

    if not videos:
        raise HTTPException(status_code=404, detail="No videos found for this subject")

    return videos
