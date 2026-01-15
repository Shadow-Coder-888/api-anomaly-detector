from fastapi import FastAPI
from app.database import create_tables

app = FastAPI(title="API Anomaly Detector")

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/")
def health_check():
    return {"status": "running"}
