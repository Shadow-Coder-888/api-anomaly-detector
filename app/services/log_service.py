from sqlalchemy.orm import Session
from app.models.api_log import APILog
from app.schemas.log import APILogCreate

def create_log(db: Session, log: APILogCreate):
    db_log = APILog(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
