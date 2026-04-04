from uuid import UUID
from app import db_models as models
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.branches import BranchCreate, BranchUpdate

#--------------------------------LIST ALL BRANCHES--------------------------------------

def get_all_branches(db: Session):
    branches = db.query(models.Branch).filter(models.Branch.is_deleted.is_(False)).all()
    if not branches:
        raise HTTPException(status_code=404, detail="No branches found")
    return branches

#--------------------------------CREATE A NEW BRANCH-------------------------------------

def create_a_new_branch(data: BranchCreate, db: Session):

    existing = db.query(models.Branch).filter(models.Branch.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Branch already exists")

    branch = models.Branch(name=data.name)

    db.add(branch)
    db.commit()
    db.refresh(branch)

    return branch

#------------------------------------LIST SUBJECT BY BRANCH--------------------------------

def get_subject_by_branch(branch_id: UUID, db: Session):
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

#-----------------------------------UPDATE-----------------------------------------------

def update_a_branch(branch_id: UUID, data: BranchUpdate, db: Session):

    branch = db.query(models.Branch).filter(models.Branch.id == branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    if data.name is not None:
        branch.name = data.name

    db.commit()
    db.refresh(branch)

    return branch

#---------------------------------- DELETE ------------------------------------------------

def delete_a_branch(branch_id: UUID, db: Session):

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
