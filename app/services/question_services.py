from uuid import UUID

from sqlalchemy.orm import Session, joinedload
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

    #  Validate subject
    subject = db.query(models.Subject).filter(models.Subject.id == subject_id).first()

    if not subject:
        raise HTTPException(404, "Subject not found")

    #  JOIN query 
    questions = (
        db.query(models.Question)
        .options(joinedload(models.Question.options))
        .join(models.Test)
        .filter(models.Test.subject_id == subject_id)
        .all()
    )

    if not questions:
        raise HTTPException(404, "No questions found for this subject")

    
    return [
        {
            "id": q.id,
            "question_text": q.question_text,
            "question_type": q.question_type,
            "marks": q.marks,
            "options": [
                {
                    "id": opt.id,
                    "option_text": opt.option_text
                }
                for opt in q.options
            ] if q.question_type in ["mcq", "msq"] else None,
        }
        for q in questions
    ]


def delete_question_service(question_id: UUID, db: Session):
    """
    Service layer function to delete a question by its ID.

    Workflow:
        1. Fetch question by ID
        2. Validate existence
        3. Delete and commit
    """

    #  Fetch question
    question = (
        db.query(models.Question).filter(models.Question.id == question_id).first()
    )

    #  Validate existence
    if not question:
        raise HTTPException(
            status_code=404, detail=f"Question with ID {question_id} not found"
        )

    #  Perform deletion
    try:
        db.delete(question)
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting the question"
        )

    return None
