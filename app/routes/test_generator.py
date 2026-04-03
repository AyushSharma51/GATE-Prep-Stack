from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import db_models as models
from ..ai_test_service import generate_mcqs
from ..schemas import TestOut, GenerateTestRequest

router = APIRouter(prefix="/resources", tags=["AI Tests"])


@router.post(
    "/generate",
    response_model=TestOut,
    summary="Generate AI-based test",
    description="""
    Generate a test using AI.

    Test Types:
    - subject → requires subject_id + num_questions
    - full → requires branch_id (creates full GATE test)

    Returns:
    - test id
    - list of questions (without answers)
    """
)
def generate_test(
    data: GenerateTestRequest,
    db: Session = Depends(get_db)
):
    """
    API Endpoint to generate AI-based MCQ tests.

    Workflow:
        1. Validate request payload
        2. Fetch subject/branch from database
        3. Call AI service to generate MCQs
        4. Store test and questions in database
        5. Return response without correct answers

    Args:
        data (GenerateTestRequest):
            Request body containing:
                - test_type ("subject" or "full")
                - subject_id (required for subject test)
                - branch_id (required for full test)
                - num_questions (for subject test)

        db (Session):
            SQLAlchemy database session (dependency injected)

    Returns:
        dict:
        {
            "id": test_id,
            "questions": [
                {
                    "id": question_id,
                    "question_text": str,
                    "options": {
                        "A": str,
                        "B": str,
                        "C": str,
                        "D": str
                    }
                }
            ]
        }

    Raises:
        HTTPException:
            - 400 → Missing or invalid input
            - 404 → Subject or Branch not found
    """

    #  SUBJECT TEST FLOW
    if data.test_type == "subject":
        # Validate required field
        if not data.subject_id:
            raise HTTPException(400, "subject_id required")

        # Fetch subject from DB
        subject = db.query(models.Subject).filter(
            models.Subject.id == data.subject_id
        ).first()

        # Handle not found
        if not subject:
            raise HTTPException(404, "Subject not found")

        # Call AI service for subject-based MCQs
        mcq_data = generate_mcqs(
            subject_name=subject.name,
            test_type="subject",
            num_questions=data.num_questions
        )

    #  FULL TEST FLOW
    elif data.test_type == "full":
        # Validate required field
        if not data.branch_id:
            raise HTTPException(400, "branch_id required")

        # Fetch branch from DB
        branch = db.query(models.Branch).filter(
            models.Branch.id == data.branch_id
        ).first()

        # Handle not found
        if not branch:
            raise HTTPException(404, "Branch not found")

        # Call AI service for full-length test
        mcq_data = generate_mcqs(
            branch_name=branch.name,
            test_type="full"
        )

    #  INVALID TEST TYPE
    else:
        raise HTTPException(400, "Invalid test_type")

    #  CREATE TEST ENTRY IN DATABASE
    test = models.Test(
        subject_id=data.subject_id if data.test_type == "subject" else None
    )
    db.add(test)

    #  Flush to get test.id before committing
    db.flush()

    # STORE QUESTIONS IN DATABASE
    for q in mcq_data["questions"]:
        question = models.Question(
            test_id=test.id,
            question_text=q["question"],
            option_a=q["options"]["A"],
            option_b=q["options"]["B"],
            option_c=q["options"]["C"],
            option_d=q["options"]["D"],
            correct_option=q["answer"]
        )
        db.add(question)

    # Commit all changes
    db.commit()

    #  Refresh to load relationships (e.g., test.questions)
    db.refresh(test)

    #  FORMAT RESPONSE (Hide correct answers)
    questions_out = [
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
        for q in test.questions
    ]

    return {
        "id": test.id,
        "questions": questions_out
    }