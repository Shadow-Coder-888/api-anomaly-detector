from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/api_anomaly_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
