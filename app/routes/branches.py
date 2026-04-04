from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import db_models as models
from ..database import get_db
from ..schemas.branches import BranchCreate, BranchResponse, BranchUpdate
from ..schemas.subjects import SubjectResponse


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
# GET SUBJECTS BY BRANCH
# -------------------------------
@router.get(
    "/subjects/{branch_id}",
    response_model=list[SubjectResponse],
    tags=["User-Resources"],
)
def get_subjects(branch_id: UUID, db: Session = Depends(get_db)):
    subjects = (
        db.query(models.Subject)
        .filter(
            models.Subject.branch_id == branch_id, models.Subject.is_deleted.is_(False)
        )
        .all()
    )

    if not subjects:
        raise HTTPException(status_code=404, detail="No subjects found for this branch")

    return subjects


# -------------------------------
# UPDATE BRANCH
# -------------------------------
@router.patch(
    "/branches/{branch_id}", response_model=BranchResponse, tags=["Admin-Resources"]
)
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
# DELETE BRANCH
# -------------------------------
@router.delete("/branches/{branch_id}", tags=["Admin-Resources"])
def delete_branch(branch_id: UUID, db: Session = Depends(get_db)):

    branch = (
        db.query(models.Branch)
        .filter(models.Branch.id == branch_id, models.Branch.is_deleted.is_(False))
        .first()
    )

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    # check active subjects
    active_subjects = [s for s in branch.subjects if not s.is_deleted]

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
