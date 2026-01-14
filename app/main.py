from fastapi import FastAPI

app = FastAPI(title="API Anomaly Detector")

@app.get("/")
def health_check():
    return {"status": "running"}
