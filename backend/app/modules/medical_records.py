from datetime import datetime
from typing import Any

from sqlalchemy import func, select

from app.database import SessionLocal
from app.models.medical_record import MedicalRecord
from app.modules.base import BaseModule


class MedicalRecordsModule(BaseModule):
    @property
    def name(self) -> str:
        return "medical_records"

    @property
    def display_name(self) -> str:
        return "Medical Records"

    @property
    def description(self) -> str:
        return "Clinical encounters, diagnoses, and provider notes."

    @property
    def version(self) -> str:
        return "0.1.0"

    def has_data(self, user_id: str) -> bool:
        with SessionLocal() as session:
            count = session.execute(
                select(func.count()).select_from(MedicalRecord).where(MedicalRecord.user_id == user_id)
            ).scalar_one()
            return count > 0

    def get_data_summary(self, user_id: str) -> dict[str, Any]:
        with SessionLocal() as session:
            count = session.execute(
                select(func.count()).select_from(MedicalRecord).where(MedicalRecord.user_id == user_id)
            ).scalar_one()
            return {"records": count}

    def get_last_update(self, user_id: str) -> datetime | None:
        with SessionLocal() as session:
            record = session.execute(
                select(MedicalRecord).where(MedicalRecord.user_id == user_id).order_by(MedicalRecord.updated_at.desc())
            ).scalars().first()
            return record.updated_at if record else None

    def import_data(self, user_id: str, file_path: str, file_type: str) -> dict[str, Any]:
        return {"imported": 0, "message": "Import not implemented"}

    def export_data(self, user_id: str, format: str) -> bytes:
        return b""

    def get_timeline_events(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> list[dict[str, Any]]:
        return []

    def get_database_models(self) -> list[Any]:
        return [MedicalRecord]
