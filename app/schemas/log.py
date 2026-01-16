from pydantic import BaseModel
from datetime import datetime

class APILogCreate(BaseModel):
    service_name: str
    endpoint: str
    method: str
    status_code: int
    response_time_ms: int
    payload_size: int | None = None

class APILogResponse(APILogCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
