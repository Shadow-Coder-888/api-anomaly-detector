from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.log import APILogCreate, APILogResponse
from app.services.log_service import create_log

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.post("/", response_model=APILogResponse)
def create_api_log(log: APILogCreate, db: Session = Depends(get_db)):
    return create_log(db, log)
