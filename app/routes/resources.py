from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import db_models as models
from uuid import UUID
from ..schemas.resources import VideoCreate, VideoResponse, VideoUpdate


router = APIRouter(prefix="/resources")


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
        title=data.title,
        playlist_url=str(data.playlist_url),
        subject_id=data.subject_id,
    )

    db.add(video)
    db.commit()
    db.refresh(video)

    return video


# -------------------------------
# UPDATE VIDEO RESOURCE
# -------------------------------
@router.patch(
    "/videos/{video_id}", response_model=VideoResponse, tags=["Admin-Resources"]
)
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
# DELETE VIDEO RESOURCE
# -------------------------------
@router.delete("/videos/{video_id}", tags=["Admin-Resources"])
def delete_video(video_id: UUID, db: Session = Depends(get_db)):

    video = (
        db.query(models.VideoResource)
        .filter(
            models.VideoResource.id == video_id,
            models.VideoResource.is_deleted.is_(False),
        )
        .first()
    )

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    db.delete(video)
    db.commit()

    return {"message": "Video permanently deleted"}
