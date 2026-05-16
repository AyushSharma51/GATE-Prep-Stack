from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.db_models import Update


router = APIRouter()


@router.get("/updates", tags=["Updates"])
def get_updates(db: Session = Depends(get_db)):

    updates = db.query(Update).filter(
        Update.is_deleted == False
    ).order_by(
        Update.created_at.desc()
    ).all()

    response = []

    for item in updates:

        response.append({
            "id": str(item.id),
            "title": item.title,
            "source": item.source,
            "source_url": item.source_url,
            "created_at": item.created_at
        })

    return response