import os
from pathlib import Path

os.environ.setdefault("HEALTHOS_DATABASE_URL", "sqlite:///./test.db")

from fastapi.testclient import TestClient

from app.database import Base, engine

def setup_module() -> None:
    db_path = Path("./test.db")
    if db_path.exists():
        db_path.unlink()
    # Create tables before app starts
    Base.metadata.create_all(bind=engine)


# Import app after database setup
from app.main import app

client = TestClient(app)


def test_auth_and_core_modules_flow() -> None:
    # Register a new user
    register_response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "password",
            "first_name": "Test",
            "last_name": "User",
        },
    )
    assert register_response.status_code == 200
    data = register_response.json()
    user_id = data["user"]["id"]
    token = data["access_token"]
    
    # Setup auth header for subsequent requests
    headers = {"Authorization": f"Bearer {token}"}

    # Test modules endpoint (no auth required)
    modules_response = client.get("/api/modules/")
    assert modules_response.status_code == 200
    module_names = {module["module_name"] for module in modules_response.json()}
    assert {"system", "medical_records", "labs", "medications"}.issubset(module_names)

    # Create medical record (requires auth)
    med_response = client.post(
        "/api/medical-records/",
        json={
            "user_id": user_id,  # This will be overridden by token
            "encounter_date": "2024-01-01",
            "provider": "Primary Care",
            "diagnosis": "Annual checkup",
            "notes": "All good",
        },
        headers=headers,
    )
    assert med_response.status_code == 200

    # Create lab result (requires auth)
    lab_response = client.post(
        "/api/labs/",
        json={
            "user_id": user_id,  # This will be overridden by token
            "test_name": "Glucose",
            "result_value": 95.0,
            "unit": "mg/dL",
            "result_date": "2024-01-02",
            "reference_range": "70-99",
        },
        headers=headers,
    )
    assert lab_response.status_code == 200

    # Create medication (requires auth)
    medication_response = client.post(
        "/api/medications/",
        json={
            "user_id": user_id,  # This will be overridden by token
            "name": "Atorvastatin",
            "dosage": "10mg",
            "start_date": "2024-01-03",
            "status": "active",
        },
        headers=headers,
    )
    assert medication_response.status_code == 200

    # Get timeline (requires auth)
    timeline_response = client.get("/api/timeline/", headers=headers)
    assert timeline_response.status_code == 200
    assert len(timeline_response.json()) == 3

    # Test that endpoints are protected (no auth = 403)
    unauth_response = client.get("/api/timeline/")
    assert unauth_response.status_code == 403
