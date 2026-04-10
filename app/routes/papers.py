from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..schemas.enums import GateBranch
import requests

router = APIRouter(tags=["Previous Year Question Papers"])

#  GitHub base URL
BASE_URL = "https://cdn.jsdelivr.net/gh/AyushSharma51/GATE-Papers@main"


@router.get("/papers/{branch}/{year}")
def get_subject_paper(branch: GateBranch, year: str):
    # Generate GitHub URL
    file_url = f"{BASE_URL}/papers/{branch.value}/{year}.pdf"

    try:
        response = requests.head(file_url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Paper not found")
    except:
        raise HTTPException(status_code=500, detail="Error connecting to storage")

    # Return URL instead of file
    return JSONResponse(content={
        "url": file_url,
        "branch": branch.value,
        "year": year
    })