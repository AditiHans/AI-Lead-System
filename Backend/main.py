import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_lead_system import run_pipeline

load_dotenv()

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL", "*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Lead system running"}

@app.get("/discover/{segment}")
def discover(segment: str):

    leads = run_pipeline(segment)

    return {
        "segment": segment,
        "lead_count": len(leads),
        "leads": leads
    }
