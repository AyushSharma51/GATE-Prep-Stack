from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from app import db_models as models
from ..ai_test_service import generate_mcqs
from ..schemas.tests import SubmitTest, TestOut, GenerateTestRequest

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
    """,
)
def generate_test(data: GenerateTestRequest, db: Session = Depends(get_db)):

    # SUBJECT TEST FLOW
    if data.test_type == "subject":
        if not data.subject_id:
            raise HTTPException(400, "subject_id required")

        subject = (
            db.query(models.Subject)
            .filter(models.Subject.id == data.subject_id)
            .first()
        )

        if not subject:
            raise HTTPException(404, "Subject not found")

        mcq_data = generate_mcqs(
            subject_name=subject.name,
            test_type="subject",
            num_questions=data.num_questions,
        )

    # FULL TEST FLOW
    elif data.test_type == "full":
        if not data.branch_id:
            raise HTTPException(400, "branch_id required")

        branch = (
            db.query(models.Branch).filter(models.Branch.id == data.branch_id).first()
        )

        if not branch:
            raise HTTPException(404, "Branch not found")

        mcq_data = generate_mcqs(branch_name=branch.name, test_type="full")

    # INVALID TEST TYPE
    else:
        raise HTTPException(400, "Invalid test_type")

    # CREATE TEST ENTRY IN DATABASE
    test = models.Test(subject_id=data.subject_id)
    db.add(test)
    db.flush()  # Get test.id before committing

    # STORE QUESTIONS IN DATABASE
    for q in mcq_data["questions"]:
        question = models.Question(
            test_id=test.id,
            question_text=q["question"],
            question_type=q["question_type"],
            marks=q["marks"],
            numerical_answer=q["answer"] if q["question_type"] == "nat" else None,
        )
        db.add(question)
        db.flush()  # Get question.id before adding options

        if q["question_type"] in ["mcq", "msq"]:
            options = q["options"]
            correct_answers = q["answer"]

            if isinstance(correct_answers, str):
                correct_answers = [correct_answers]

            for key, value in options.items():
                option = models.Option(
                    question_id=question.id,
                    option_text=value,
                    is_correct=key in correct_answers,
                )
                db.add(option)

    # Commit all changes
    db.commit()
    db.refresh(test)

    # FORMAT RESPONSE — answers hidden, is_correct NOT exposed
    questions_out = [
        {
            "id": q.id,
            "question_text": q.question_text,
            "question_type": q.question_type,
            "marks": q.marks,
            "options": (
                [
                    {
                        "id": opt.id,
                        "option_text": opt.option_text,
                        # ✅ is_correct removed — answers not leaked
                    }
                    for opt in q.options
                ]
                if q.question_type in ["mcq", "msq"]
                else None
            ),
        }
        for q in test.questions
    ]

    return {"id": test.id, "questions": questions_out}


@router.post("/submit/{test_id}")
def submit_test(test_id: UUID, data: SubmitTest, db: Session = Depends(get_db)):
    test = db.query(models.Test).filter(models.Test.id == test_id).first()
    if not test:
        raise HTTPException(404, "Test not found")

    score = 0.0
    total = 0.0
    positive = 0.0
    negative = 0.0
    attempted = 0
    correct_count = 0

    # Per-question result map — sent back to frontend for highlighting
    question_results = {}

    for question in test.questions:
        total += question.marks

        user_answer = data.answers.get(str(question.id))

        # Collect correct option IDs for this question (for frontend highlighting)
        correct_ids = (
            [str(opt.id) for opt in question.options if opt.is_correct]
            if question.question_type in ["mcq", "msq"]
            else []
        )

        q_result = {
            "correct_option_ids": correct_ids,
            "is_correct": False,
            "was_attempted": False,
        }

        # -------------------
        # MCQ
        # -------------------
        if question.question_type == "mcq":
            correct_option = next(
                (opt for opt in question.options if opt.is_correct), None
            )

            if user_answer:
                attempted += 1
                q_result["was_attempted"] = True

                # Handle both string and list from frontend
                selected_id = (
                    user_answer[0] if isinstance(user_answer, list) else user_answer
                )

                if correct_option and selected_id == str(correct_option.id):
                    score += question.marks
                    positive += question.marks
                    correct_count += 1
                    q_result["is_correct"] = True
                else:
                    neg = round(question.marks / 3, 2)
                    score -= neg
                    negative += neg

        # -------------------
        # MSQ
        # -------------------
        elif question.question_type == "msq":
            correct_options = {
                str(opt.id) for opt in question.options if opt.is_correct
            }
            user_set = set(user_answer) if user_answer else set()

            if user_answer:
                attempted += 1
                q_result["was_attempted"] = True

                if user_set == correct_options:
                    score += question.marks
                    positive += question.marks
                    correct_count += 1
                    q_result["is_correct"] = True
                # No negative marking for MSQ — GATE standard

        # -------------------
        # NAT
        # -------------------
        elif question.question_type == "nat":
            if user_answer is not None:
                attempted += 1
                q_result["was_attempted"] = True

                tol = question.tolerance or 0

                try:
                    user_val = float(user_answer)
                except (ValueError, TypeError):
                    question_results[str(question.id)] = q_result
                    continue

                if abs(user_val - question.numerical_answer) <= tol:
                    score += question.marks
                    positive += question.marks
                    correct_count += 1
                    q_result["is_correct"] = True
                # No negative marking for NAT — GATE standard

        question_results[str(question.id)] = q_result

    # -------------------
    # FINAL METRICS
    # -------------------
    unattempted = len(test.questions) - attempted
    accuracy = (correct_count / attempted * 100) if attempted else 0

    return {
        "score": round(score, 2),
        "total": round(total, 2),
        "positive": round(positive, 2),
        "negative": round(negative, 2),
        "attempted": attempted,
        "unattempted": unattempted,
        "correct": correct_count,
        "incorrect": attempted - correct_count,
        "accuracy": round(accuracy, 2),
        # ✅ Per-question results for frontend highlighting
        "question_results": question_results,
    }
