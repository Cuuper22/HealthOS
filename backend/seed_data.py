"""
Seed data script for development/testing.
Run with: python seed_data.py
"""

from datetime import date, datetime, timedelta

from app.database import SessionLocal
from app.models.lab_result import LabResult
from app.models.medical_record import MedicalRecord
from app.models.medication import Medication
from app.models.timeline_event import TimelineEvent
from app.models.user import User
from app.utils.security import hash_password


def create_seed_data():
    """Create seed data for development."""
    with SessionLocal() as session:
        # Create test user
        test_user = User(
            email="test@healthos.dev",
            password_hash=hash_password("password123"),
            first_name="Test",
            last_name="User",
            date_of_birth=date(1990, 1, 15),
            sex="M",
        )
        session.add(test_user)
        session.flush()

        print(f"Created test user: {test_user.email}")
        print(f"User ID: {test_user.id}")
        print("Password: password123")

        # Create medical records
        records_data = [
            {
                "encounter_date": date.today() - timedelta(days=90),
                "provider": "Dr. Smith, General Practice",
                "diagnosis": "Annual physical - all normal",
                "notes": "Blood pressure: 120/80, Weight: 165 lbs",
            },
            {
                "encounter_date": date.today() - timedelta(days=30),
                "provider": "Dr. Johnson, Dermatology",
                "diagnosis": "Skin check - benign mole removed",
                "notes": "Routine screening",
            },
        ]

        for data in records_data:
            record = MedicalRecord(user_id=test_user.id, **data)
            session.add(record)
            session.flush()

            # Create timeline event
            event = TimelineEvent(
                user_id=test_user.id,
                event_type="medical_record",
                event_date=datetime.combine(record.encounter_date, datetime.min.time()),
                module_name="medical_records",
                source_record_id=record.id,
                title=record.diagnosis or "Medical appointment",
                description=record.provider,
            )
            session.add(event)

        print(f"Created {len(records_data)} medical records")

        # Create lab results
        labs_data = [
            {
                "test_name": "Hemoglobin A1C",
                "result_value": 5.4,
                "unit": "%",
                "result_date": date.today() - timedelta(days=60),
                "reference_range": "4.0-5.6",
                "notes": "Normal range",
            },
            {
                "test_name": "Total Cholesterol",
                "result_value": 185,
                "unit": "mg/dL",
                "result_date": date.today() - timedelta(days=60),
                "reference_range": "<200",
                "notes": "Desirable level",
            },
            {
                "test_name": "Vitamin D",
                "result_value": 32,
                "unit": "ng/mL",
                "result_date": date.today() - timedelta(days=45),
                "reference_range": "30-100",
                "notes": "Adequate",
            },
        ]

        for data in labs_data:
            lab = LabResult(user_id=test_user.id, **data)
            session.add(lab)
            session.flush()

            # Create timeline event
            event = TimelineEvent(
                user_id=test_user.id,
                event_type="lab_result",
                event_date=datetime.combine(lab.result_date, datetime.min.time()),
                module_name="labs",
                source_record_id=lab.id,
                title=lab.test_name,
                description=f"{lab.result_value} {lab.unit or ''}".strip(),
            )
            session.add(event)

        print(f"Created {len(labs_data)} lab results")

        # Create medications
        meds_data = [
            {
                "name": "Lisinopril",
                "dosage": "10mg once daily",
                "start_date": date.today() - timedelta(days=180),
                "status": "active",
                "notes": "For blood pressure management",
            },
            {
                "name": "Vitamin D3",
                "dosage": "2000 IU daily",
                "start_date": date.today() - timedelta(days=90),
                "status": "active",
                "notes": "Supplement",
            },
            {
                "name": "Amoxicillin",
                "dosage": "500mg three times daily",
                "start_date": date.today() - timedelta(days=120),
                "end_date": date.today() - timedelta(days=110),
                "status": "completed",
                "notes": "10-day course for infection",
            },
        ]

        for data in meds_data:
            med = Medication(user_id=test_user.id, **data)
            session.add(med)
            session.flush()

            # Create timeline event
            event = TimelineEvent(
                user_id=test_user.id,
                event_type="medication",
                event_date=datetime.combine(
                    med.start_date or datetime.utcnow().date(), datetime.min.time()
                ),
                module_name="medications",
                source_record_id=med.id,
                title=med.name,
                description=med.dosage,
            )
            session.add(event)

        print(f"Created {len(meds_data)} medications")

        session.commit()
        print("\nSeed data created successfully!")
        print(f"\nLogin credentials:")
        print(f"  Email: test@healthos.dev")
        print(f"  Password: password123")
        print(f"  User ID: {test_user.id}")


if __name__ == "__main__":
    create_seed_data()
