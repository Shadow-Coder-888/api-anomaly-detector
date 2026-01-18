from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.api_log import APILog

def get_logs(
    db: Session,
    service_name: str | None,
    status_code: int | None,
    skip: int,
    limit: int,
):
    query = db.query(APILog)

    if service_name:
        query = query.filter(APILog.service_name == service_name)

    if status_code:
        query = query.filter(APILog.status_code == status_code)

    return query.order_by(APILog.created_at.desc()).offset(skip).limit(limit).all()


def get_log_stats(db: Session):
    total = db.query(func.count(APILog.id)).scalar()

    avg_response = db.query(func.avg(APILog.response_time_ms)).scalar()

    error_count = (
        db.query(APILog)
        .filter(APILog.status_code >= 400)
        .count()
    )

    error_rate = (error_count / total) if total else 0

    return {
        "total_requests": total,
        "avg_response_time_ms": float(avg_response or 0),
        "error_rate": error_rate,
    }
