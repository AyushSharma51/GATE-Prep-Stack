from fastapi import FastAPI
from .routes.papers import router as papers_router
from .routes.resources import router as resources_router
from .routes.test_generator import router as test_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="GATE Free Resources")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(papers_router)
app.include_router(resources_router)
app.include_router(test_router)

@app.get("/Health-Check", tags=["System"])
def heath_check():
    return {"message": "API is Working!"}

