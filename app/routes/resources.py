from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import (
    BranchCreate,
    BranchUpdate,
    BranchResponse,
    SubjectCreate,
    SubjectUpdate,
    SubjectResponse,
    VideoCreate,
    VideoUpdate,
    VideoResponse,
)
from app.database import get_db
from app import db_models as models
from uuid import UUID

router = APIRouter(prefix="/resources")


# -------------------------------
# GET ALL BRANCHES
# -------------------------------
@router.get("/branches", response_model=list[BranchResponse], tags=["User-Resources"])
def get_branches(db: Session = Depends(get_db)):
    branches = db.query(models.Branch).filter(models.Branch.is_deleted .is_(False)).all()
    if not branches:
        raise HTTPException(status_code=404, detail="No branches found")
    return branches


# -------------------------------
# GET SUBJECTS BY BRANCH
# -------------------------------
@router.get("/subjects/{branch_id}", response_model=list[SubjectResponse], tags=["User-Resources"])
def get_subjects(branch_id: UUID, db: Session = Depends(get_db)):
    subjects = db.query(models.Subject).filter(
        models.Subject.branch_id == branch_id,
        models.Subject.is_deleted .is_(False)
    ).all()

    if not subjects:
        raise HTTPException(status_code=404, detail="No subjects found for this branch")

    return subjects


# -------------------------------
# GET VIDEOS BY SUBJECT
# -------------------------------
@router.get("/videos/{subject_id}", response_model=list[VideoResponse], tags=["User-Resources"])
def get_videos(subject_id: UUID, db: Session = Depends(get_db)):

    videos = db.query(models.VideoResource).filter(
        models.VideoResource.subject_id == subject_id,
        models.VideoResource.is_deleted .is_(False)
    ).all()

    if not videos:
        raise HTTPException(status_code=404, detail="No videos found for this subject")

    return videos


# -------------------------------
# CREATE BRANCH
# -------------------------------
@router.post("/branches", response_model=BranchResponse, tags=["Admin-Resources"])
def create_branch(data: BranchCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Branch).filter(models.Branch.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Branch already exists")

    branch = models.Branch(name=data.name)

    db.add(branch)
    db.commit()
    db.refresh(branch)

    return branch


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
# CREATE VIDEO RESOURCE
# -------------------------------
@router.post("/videos", response_model=VideoResponse, tags=["Admin-Resources"])
def create_video(data: VideoCreate, db: Session = Depends(get_db)):

    subject = (
        db.query(models.Subject).filter(models.Subject.id == data.subject_id).first()
    )
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    video = models.VideoResource(
        title=data.title, playlist_url=str(data.playlist_url), subject_id=data.subject_id
    )

    db.add(video)
    db.commit()
    db.refresh(video)

    return video


# -------------------------------
# UPDATE BRANCH
# -------------------------------
@router.patch("/branches/{branch_id}", response_model=BranchResponse, tags=["Admin-Resources"])
def update_branch(branch_id: UUID, data: BranchUpdate, db: Session = Depends(get_db)):

    branch = db.query(models.Branch).filter(models.Branch.id == branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    if data.name is not None:
        branch.name = data.name

    db.commit()
    db.refresh(branch)

    return branch


# -------------------------------
# UPDATE SUBJECT
# -------------------------------
@router.patch("/subjects/{subject_id}", response_model=SubjectResponse, tags=["Admin-Resources"])
def update_subject(subject_id: UUID, data: SubjectUpdate, db: Session = Depends(get_db)):

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
# UPDATE VIDEO RESOURCE
# -------------------------------
@router.patch("/videos/{video_id}", response_model=VideoResponse, tags=["Admin-Resources"])
def update_video(video_id: UUID, data: VideoUpdate, db: Session = Depends(get_db)):

    video = (
        db.query(models.VideoResource)
        .filter(models.VideoResource.id == video_id)
        .first()
    )

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    if data.title is not None:
        video.title = data.title

    if data.playlist_url is not None:
        video.playlist_url = str(data.playlist_url)

    if data.subject_id is not None:
        subject = (
            db.query(models.Subject)
            .filter(models.Subject.id == data.subject_id)
            .first()
        )
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        video.subject_id = data.subject_id

    db.commit()
    db.refresh(video)

    return video


# -------------------------------
# DELETE BRANCH
# -------------------------------
@router.delete("/branches/{branch_id}", tags=["Admin-Resources"])
def delete_branch(branch_id: UUID, db: Session = Depends(get_db)):

    branch = db.query(models.Branch).filter(
        models.Branch.id == branch_id,
        models.Branch.is_deleted.is_(False)
    ).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    # check active subjects
    active_subjects = [
        s for s in branch.subjects if not s.is_deleted
    ]

    if active_subjects:
        # SOFT DELETE
        branch.is_deleted = True
        db.commit()
        return {"message": "Branch soft deleted (has subjects)"}
    else:
        # HARD DELETE
        db.delete(branch)
        db.commit()
        return {"message": "Branch permanently deleted"}


# -------------------------------
# DELETE SUBJECT
# -------------------------------
@router.delete("/subjects/{subject_id}", tags=["Admin-Resources"])
def delete_subject(subject_id: UUID, db: Session = Depends(get_db)):

    subject = db.query(models.Subject).filter(
        models.Subject.id == subject_id,
        models.Subject.is_deleted .is_(False))

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # check active videos
    active_videos = [
        v for v in subject.videos if not v.is_deleted
    ]

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


# -------------------------------
# DELETE VIDEO RESOURCE
# -------------------------------
@router.delete("/videos/{video_id}", tags=["Admin-Resources"])
def delete_video(video_id: UUID, db: Session = Depends(get_db)):

    video = db.query(models.VideoResource).filter(
        models.VideoResource.id == video_id,
        models.VideoResource.is_deleted .is_(False)
    ).first()

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    db.delete(video)
    db.commit()

    return {"message": "Video permanently deleted"}