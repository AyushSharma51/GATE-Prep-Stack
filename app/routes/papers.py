from fastapi import APIRouter, HTTPException, Path, status
from fastapi.responses import FileResponse
import os
from typing import Annotated

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@router.get("/{year}", tags=["CSE Previous Year Question Papers"])
def get_paper(year: Annotated[str, Path(description="Enter year like 2023 or 2025-1")]):
    file_path = os.path.join(BASE_DIR, "papers", "cse", f"{year}.pdf")
    print("Looking for:", file_path)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return FileResponse(file_path)
