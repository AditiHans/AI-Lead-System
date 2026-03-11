from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_lead_system import run_pipeline

app = FastAPI(title="AI Lead Discovery API")

# Allow frontend requests
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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