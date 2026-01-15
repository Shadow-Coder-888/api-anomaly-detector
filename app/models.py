from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ApiLog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(String(100), nullable=False)
    endpoint = Column(Text, nullable=False)
    method = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

