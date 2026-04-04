from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.question_services import get_questions_by_subject_service


router = APIRouter(prefix="/questions", tags=["AI Tests"])


@router.get("/subject/{subject_id}", summary="Get questions by subject")
def get_questions_by_subject(subject_id: UUID, db: Session = Depends(get_db)):

    return get_questions_by_subject_service(subject_id, db)
