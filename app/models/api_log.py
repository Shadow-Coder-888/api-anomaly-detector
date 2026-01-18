from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class APILog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    response_time_ms = Column(Integer, nullable=False)
    payload_size = Column(Integer)
    is_anomalous = Column(Boolean, default=False)
    anomaly_reason = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

