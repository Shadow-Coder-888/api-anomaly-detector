from sqlalchemy.orm import Session
from app.models.api_log import APILog
from app.schemas.log import APILogCreate

LATENCY_THRESHOLD_MS = 1000
PAYLOAD_THRESHOLD = 500000  # 500 KB


def detect_anomaly(log: APILogCreate) -> tuple[bool, str | None]:
    if log.response_time_ms > LATENCY_THRESHOLD_MS:
        return True, "High latency"

    if log.status_code >= 500:
        return True, "Server error"

    if log.payload_size and log.payload_size > PAYLOAD_THRESHOLD:
        return True, "Payload size anomaly"

    return False, None


def create_log(db: Session, log: APILogCreate) -> APILog:
    is_anomalous, reason = detect_anomaly(log)

    db_log = APILog(
        service_name=log.service_name,
        endpoint=log.endpoint,
        method=log.method.upper(),
        status_code=log.status_code,
        response_time_ms=log.response_time_ms,
        payload_size=log.payload_size or 0,
        is_anomalous=is_anomalous,
        anomaly_reason=reason,
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
