from fastapi import FastAPI
from app.database import create_tables
from app.routes.logs import router as logs_router

app = FastAPI(title="API Anomaly Detector")


@app.on_event("startup")
def startup_event():
    create_tables()


app.include_router(logs_router)
