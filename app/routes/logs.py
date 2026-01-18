from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.log_schema import LogCreate
from app.services.log_service import create_log, get_logs
from app.db.deps import get_db

router = APIRouter()

@router.post("/logs")
def create_log_endpoint(
    log: LogCreate,
    db: Session = Depends(get_db)
):
    return create_log(db, log)


@router.get("/logs")
def get_logs_endpoint(
    service_name: str | None = None,
    db: Session = Depends(get_db)
):
    return get_logs(db, service_name)
