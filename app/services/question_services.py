from uuid import UUID

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import db_models as models


def get_questions_by_subject_service(subject_id: UUID, db: Session):
    """
    Service layer function to fetch questions by subject.

    Workflow:
        1. Validate subject existence
        2. Fetch questions using JOIN (Question → Test)
        3. Return formatted data

    Args:
        subject_id (int): Subject ID
        db (Session): Database session

    Returns:
        List[dict]: List of formatted questions
    """

    # 🔹 Step 1: Validate subject
    subject = db.query(models.Subject).filter(
        models.Subject.id == subject_id
    ).first()

    if not subject:
        raise HTTPException(404, "Subject not found")

    # 🔹 Step 2: JOIN query (IMPORTANT)
    questions = db.query(models.Question).join(models.Test).filter(
        models.Test.subject_id == subject_id
    ).all()

    if not questions:
        raise HTTPException(404, "No questions found for this subject")

    # 🔹 Step 3: Format response
    return [
        {
            "id": q.id,
            "question_text": q.question_text,
            "options": {
                "A": q.option_a,
                "B": q.option_b,
                "C": q.option_c,
                "D": q.option_d,
            }
        }
        for q in questions
    ]