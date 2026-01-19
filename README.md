
---

# API Anomaly Detector

## Problem Statement

Modern systems expose APIs that handle critical operations such as authentication, payments, and data access. These APIs are frequently targeted by:

* Abuse (excessive requests, scraping)
* Misuse (unexpected payloads, abnormal status codes)
* Attacks (brute force, enumeration, automated probing)

Traditional logging systems **store data but do not analyze behavior**. As a result, anomalies are detected late or not at all.

This project addresses that gap.

---

## What Problem This Solves

* Identifies **abnormal API usage patterns**
* Detects **suspicious request behavior** early
* Provides a foundation for **security monitoring and alerting**
* Converts raw API logs into **actionable insights**

This is not a generic logger. It is a **behavior-aware API telemetry system**.

---

## How the System Solves It

1. **API logs are captured** in structured form (endpoint, method, status, latency, timestamp).
2. Logs are stored in a **relational database** for consistency and querying.
3. Historical data is analyzed to establish **normal behavior baselines**.
4. Incoming logs are compared against these baselines to detect:

   * Unusual request frequency
   * Abnormal response codes
   * Latency spikes
   * Endpoint misuse patterns
5. Detected anomalies can later be used for:

   * Alerts
   * Dashboards
   * Automated blocking (future scope)

---

## Core Features

* Centralized API log ingestion
* Persistent storage using PostgreSQL
* REST endpoints for log ingestion and retrieval
* Extensible design for ML-based anomaly detection
* Clean separation of routes, services, and database logic

---

## Tech Stack

**Backend**

* Python 3.11+
* FastAPI
* SQLAlchemy
* Pydantic

**Database**

* PostgreSQL

**Tooling**

* Uvicorn
* Virtualenv
* Git / GitHub

**Planned**

* Scikit-learn / PyOD for anomaly detection
* Background workers for analysis
* Metrics & alerting

---

## Project Structure

```
api-anomaly-detector/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── logs.py
│   ├── services/
│   │   └── log_service.py
│   ├── models/
│   │   └── log.py
│   ├── schemas/
│   │   └── log.py
│   └── db/
│       ├── base.py
│       └── session.py
│
├── alembic/
├── README.md
├── requirements.txt
└── .env
```

---

## How to Run the Project (Local)

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/api-anomaly-detector.git
cd api-anomaly-detector
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/api_logs
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start the Server

```bash
python -m uvicorn app.main:app --reload
```

### 7. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Create Log

```
POST /logs
```

Stores a single API log entry.

### Read Logs

```
GET /logs
```

Supports pagination and filtering.

---

## Design Decisions

### Why FastAPI

* High performance
* Automatic OpenAPI documentation
* Strong typing with Pydantic
* Production-ready async support

### Why PostgreSQL

* Reliable transactional storage
* Strong indexing for analytics
* Suitable for time-series queries

### Why Service Layer

* Keeps routes thin
* Business logic remains testable
* Easier future ML integration

---

## Scalability Considerations

* Database indexing on timestamp and endpoint
* Batch processing for anomaly detection
* Background workers for analysis
* Can be deployed behind API Gateway

---

## Future Enhancements

* ML-based anomaly detection
* Real-time alerting (email / Slack / webhook)
* Dashboard for visualization
* Rate-limit enforcement integration
* Authentication and RBAC

---

## Status

**Active Development**

This project is being built incrementally with production-grade practices.

---

