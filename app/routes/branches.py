from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.branches import BranchCreate, BranchResponse, BranchUpdate
from ..schemas.subjects import SubjectResponse
from ..services.branch_services import (
    create_a_new_branch,
    delete_a_branch,
    get_all_branches,
    get_subject_by_branch,
    update_a_branch,
)


router = APIRouter(prefix="/resources")


# -------------------------------
# GET ALL BRANCHES
# -------------------------------
@router.get("/branches", response_model=list[BranchResponse], tags=["User-Resources"])
def get_branches(db: Session = Depends(get_db)):

    return get_all_branches(db)


# -------------------------------
# CREATE BRANCH
# -------------------------------
@router.post("/branches", response_model=BranchResponse, tags=["Admin-Resources"])
def create_branch(data: BranchCreate, db: Session = Depends(get_db)):

    return create_a_new_branch(data, db)


# -------------------------------
# GET SUBJECTS BY BRANCH
# -------------------------------
@router.get(
    "/subjects/{branch_id}",
    response_model=list[SubjectResponse],
    tags=["User-Resources"],
)
def get_subjects(branch_id: UUID, db: Session = Depends(get_db)):

    return get_subject_by_branch(branch_id, db)


# -------------------------------
# UPDATE BRANCH
# -------------------------------
@router.patch(
    "/branches/{branch_id}", response_model=BranchResponse, tags=["Admin-Resources"]
)
def update_branch(branch_id: UUID, data: BranchUpdate, db: Session = Depends(get_db)):

    return update_a_branch(branch_id, data, db)


# -------------------------------
# DELETE BRANCH
# -------------------------------
@router.delete("/branches/{branch_id}", tags=["Admin-Resources"])
def delete_branch(branch_id: UUID, db: Session = Depends(get_db)):

    return delete_a_branch(branch_id, db)
