from sqlalchemy.orm import Session
from app.db.models import ApiLog

def create_log(db: Session, log):
    db_log = ApiLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_logs(db: Session, service_name: str | None = None):
    query = db.query(ApiLog)
    if service_name:
        query = query.filter(ApiLog.service_name == service_name)
    return query.all()

