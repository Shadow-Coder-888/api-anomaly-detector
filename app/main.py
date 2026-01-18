from fastapi import FastAPI
from app.routes.logs import router as logs_router

app = FastAPI()

app.include_router(logs_router)
