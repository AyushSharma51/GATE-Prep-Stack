from fastapi import FastAPI
from .routes.papers import router as papers_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(papers_router)

@app.get("/Health-Check", tags=["API Working"])
def heath_check():
    return {"message":"API is Working!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)