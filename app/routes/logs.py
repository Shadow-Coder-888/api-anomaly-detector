from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.api_log import APILog
from app.schemas.log import APILogCreate, APILogResponse

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.post("/", response_model=APILogResponse)
def create_log(log: APILogCreate, db: Session = Depends(get_db)):
    db_log = APILog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
