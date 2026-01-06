import os
from pathlib import Path

os.environ.setdefault("HEALTHOS_DATABASE_URL", "sqlite:///./test.db")

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def setup_module() -> None:
    db_path = Path("./test.db")
    if db_path.exists():
        db_path.unlink()


def test_auth_and_core_modules_flow() -> None:
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
    user_id = register_response.json()["user"]["id"]

    modules_response = client.get("/api/modules/")
    assert modules_response.status_code == 200
    module_names = {module["module_name"] for module in modules_response.json()}
    assert {"system", "medical_records", "labs", "medications"}.issubset(module_names)

    med_response = client.post(
        "/api/medical-records/",
        json={
            "user_id": user_id,
            "encounter_date": "2024-01-01",
            "provider": "Primary Care",
            "diagnosis": "Annual checkup",
            "notes": "All good",
        },
    )
    assert med_response.status_code == 200

    lab_response = client.post(
        "/api/labs/",
        json={
            "user_id": user_id,
            "test_name": "Glucose",
            "result_value": 95.0,
            "unit": "mg/dL",
            "result_date": "2024-01-02",
            "reference_range": "70-99",
        },
    )
    assert lab_response.status_code == 200

    medication_response = client.post(
        "/api/medications/",
        json={
            "user_id": user_id,
            "name": "Atorvastatin",
            "dosage": "10mg",
            "start_date": "2024-01-03",
            "status": "active",
        },
    )
    assert medication_response.status_code == 200

    timeline_response = client.get(f"/api/timeline/?user_id={user_id}")
    assert timeline_response.status_code == 200
    assert len(timeline_response.json()) == 3
