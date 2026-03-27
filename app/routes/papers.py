from fastapi import APIRouter, HTTPException, Path, status
from fastapi.responses import FileResponse
import os
from typing import Annotated


router = APIRouter()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Common function (reusable)
def get_question_paper(branch: str, year: str):
    file_path = os.path.join(BASE_DIR, "papers", branch, f"{year}.pdf")
    print("Looking for:", file_path)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{branch.upper()} paper for {year} not found"
        )

    return FileResponse(file_path)


#  CSE Route
@router.get("/cse/{year}", tags=["Previous Year Question Papers"])
def get_cse_papers(
    year: Annotated[str, Path(description="Enter year like 2023 or 2025-1")]
):
    return get_question_paper("cse", year)


#  DA Route (Data Science & AI)
@router.get("/da/{year}", tags=["Previous Year Question Papers"])
def get_da_papers(
    year: Annotated[str, Path(description="Enter year like 2023 or 2025-1")]
):
    return get_question_paper("da", year)


#  ME Route (Mechanical Engineering)
@router.get("/me/{year}", tags=["Previous Year Question Papers"])
def get_me_papers(
    year: Annotated[str, Path(description="Enter year like 2023 or 2025-1")]
):
    return get_question_paper("me", year)
