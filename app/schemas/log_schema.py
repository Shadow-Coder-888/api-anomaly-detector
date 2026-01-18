from pydantic import BaseModel
from typing import Optional


class LogCreate(BaseModel):
    service_name: str
    endpoint: str
    method: str
    status_code: int
    response_time_ms: int
    payload_size: Optional[int] = None
