from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from ..schemas import GateBranch

router = APIRouter(tags=["Previous Year Question Papers"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@router.get("/papers/{branch}/{year}")
def get_subject_paper(branch: GateBranch, year: str):
    file_path = os.path.join(BASE_DIR, "papers", branch.value, f"{year}.pdf")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Paper not found")

    return FileResponse(file_path)
