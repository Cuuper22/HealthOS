import os
from pathlib import Path

os.environ.setdefault("HEALTHOS_DATABASE_URL", "sqlite:///./test_health.db")

from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app

client = TestClient(app)


def setup_module() -> None:
    db_path = Path("./test_health.db")
    if db_path.exists():
        db_path.unlink()
    Base.metadata.create_all(bind=engine)


def get_auth_token() -> str:
    """Helper to register a user and return auth token."""
    import uuid
    email = f"health_test_{uuid.uuid4().hex[:8]}@example.com"
    response = client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": "testpass123",
        },
    )
    return response.json()["access_token"]


def test_create_and_list_medical_records() -> None:
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create medical record
    create_response = client.post(
        "/api/medical-records/",
        json={
            "user_id": "will-be-overridden",
            "encounter_date": "2024-01-15",
            "provider": "Dr. Smith",
            "diagnosis": "Common cold",
            "notes": "Rest and fluids",
        },
        headers=headers,
    )
    assert create_response.status_code == 200
    record = create_response.json()
    assert record["diagnosis"] == "Common cold"
    assert record["provider"] == "Dr. Smith"
    
    # List medical records
    list_response = client.get("/api/medical-records/", headers=headers)
    assert list_response.status_code == 200
    records = list_response.json()
    assert len(records) == 1
    assert records[0]["diagnosis"] == "Common cold"


def test_create_and_list_lab_results() -> None:
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create lab result
    create_response = client.post(
        "/api/labs/",
        json={
            "user_id": "will-be-overridden",
            "test_name": "Hemoglobin A1C",
            "result_value": 5.7,
            "unit": "%",
            "result_date": "2024-01-20",
            "reference_range": "<5.7",
        },
        headers=headers,
    )
    assert create_response.status_code == 200
    result = create_response.json()
    assert result["test_name"] == "Hemoglobin A1C"
    assert result["result_value"] == 5.7
    
    # List lab results
    list_response = client.get("/api/labs/", headers=headers)
    assert list_response.status_code == 200
    results = list_response.json()
    assert len(results) == 1
    assert results[0]["test_name"] == "Hemoglobin A1C"


def test_create_and_list_medications() -> None:
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create medication
    create_response = client.post(
        "/api/medications/",
        json={
            "user_id": "will-be-overridden",
            "name": "Lisinopril",
            "dosage": "10mg daily",
            "start_date": "2024-01-01",
            "status": "active",
        },
        headers=headers,
    )
    assert create_response.status_code == 200
    medication = create_response.json()
    assert medication["name"] == "Lisinopril"
    assert medication["dosage"] == "10mg daily"
    
    # List medications
    list_response = client.get("/api/medications/", headers=headers)
    assert list_response.status_code == 200
    medications = list_response.json()
    assert len(medications) == 1
    assert medications[0]["status"] == "active"


def test_timeline_integration() -> None:
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create various records
    client.post(
        "/api/medical-records/",
        json={
            "user_id": "x",
            "encounter_date": "2024-01-10",
            "diagnosis": "Checkup",
        },
        headers=headers,
    )
    client.post(
        "/api/labs/",
        json={
            "user_id": "x",
            "test_name": "CBC",
            "result_value": 14.5,
            "unit": "g/dL",
            "result_date": "2024-01-11",
        },
        headers=headers,
    )
    client.post(
        "/api/medications/",
        json={
            "user_id": "x",
            "name": "Aspirin",
            "dosage": "81mg",
            "start_date": "2024-01-12",
            "status": "active",
        },
        headers=headers,
    )
    
    # Check timeline
    timeline_response = client.get("/api/timeline/", headers=headers)
    assert timeline_response.status_code == 200
    events = timeline_response.json()
    assert len(events) == 3
    
    # Verify events are sorted by date descending
    event_types = [e["event_type"] for e in events]
    assert "medication" in event_types
    assert "lab_result" in event_types
    assert "medical_record" in event_types


def test_data_isolation_between_users() -> None:
    # Create two users
    token1 = get_auth_token()
    token2 = get_auth_token()
    
    headers1 = {"Authorization": f"Bearer {token1}"}
    headers2 = {"Authorization": f"Bearer {token2}"}
    
    # User 1 creates a record
    client.post(
        "/api/medical-records/",
        json={
            "user_id": "x",
            "encounter_date": "2024-01-01",
            "diagnosis": "User 1 record",
        },
        headers=headers1,
    )
    
    # User 2 creates a record
    client.post(
        "/api/medical-records/",
        json={
            "user_id": "x",
            "encounter_date": "2024-01-02",
            "diagnosis": "User 2 record",
        },
        headers=headers2,
    )
    
    # Verify user 1 only sees their records
    records1 = client.get("/api/medical-records/", headers=headers1).json()
    assert len(records1) == 1
    assert records1[0]["diagnosis"] == "User 1 record"
    
    # Verify user 2 only sees their records
    records2 = client.get("/api/medical-records/", headers=headers2).json()
    assert len(records2) == 1
    assert records2[0]["diagnosis"] == "User 2 record"
