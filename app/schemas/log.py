from pydantic import BaseModel, Field

class APILogCreate(BaseModel):
    service_name: str
    endpoint: str
    method: str
    status_code: int = Field(ge=100, le=599)
    response_time_ms: int = Field(gt=0)
    payload_size: int | None = 0

class APILogResponse(APILogCreate):
    id: int
    is_anomalous: bool
    anomaly_reason: str | None

    class Config:
        from_attributes = True
