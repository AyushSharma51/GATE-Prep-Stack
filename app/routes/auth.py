from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.db_models import User
from app.schemas.auth import SignupRequest
from app.security import hash_password, get_current_user, require_admin
from app.schemas.auth import SignupRequest, LoginRequest
from app.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    data: SignupRequest,
    db: Session = Depends(get_db)
):
    # 1. Check whether email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # 2. Hash the password
    hashed_password = hash_password(data.password)

    # 3. Create the user
    user = User(
        name=data.name,
        email=data.email,
        password_hash=hashed_password,
        role="user"
    )

    # 4. Save user to database
    db.add(user)
    db.commit()
    db.refresh(user)

    # 5. Return response
    return {
        "message": "Account created successfully",
        "user_id": str(user.id),
        "name": user.name,
        "email": user.email
    }

@router.post("/login")
def login(
    data: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    # 1. Find user
    user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # 2. Verify password
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # 3. Create JWT
    token = create_access_token(
        str(user.id),
        user.role
    )

    # 4. Put JWT in HttpOnly cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60
    )

    return {
        "message": "Login successful"
    }

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    }

@router.get("/admin-test")
def admin_test(current_user: User = Depends(require_admin)):
    return {
        "message": "You are an admin!",
        "user": current_user.name
    }