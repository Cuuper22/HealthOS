from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import select

from app.api.schemas import MedicalRecordCreate, MedicalRecordResponse
from app.database import SessionLocal
from app.models.medical_record import MedicalRecord
from app.services.timeline import create_timeline_event

router = APIRouter(prefix="/api/medical-records", tags=["medical-records"])


@router.get("/", response_model=list[MedicalRecordResponse])
def list_records(user_id: str) -> list[MedicalRecordResponse]:
    with SessionLocal() as session:
        records = (
            session.execute(select(MedicalRecord).where(MedicalRecord.user_id == user_id))
            .scalars()
            .all()
        )
        return [
            MedicalRecordResponse(
                id=record.id,
                user_id=record.user_id,
                encounter_date=record.encounter_date,
                provider=record.provider,
                diagnosis=record.diagnosis,
                notes=record.notes,
            )
            for record in records
        ]


@router.post("/", response_model=MedicalRecordResponse)
def create_record(payload: MedicalRecordCreate) -> MedicalRecordResponse:
    with SessionLocal() as session:
        record = MedicalRecord(**payload.model_dump())
        session.add(record)
        session.flush()
        create_timeline_event(
            session,
            user_id=record.user_id,
            event_type="medical_record",
            event_date=datetime.combine(record.encounter_date, datetime.min.time()),
            module_name="medical_records",
            title=record.diagnosis or "Medical record",
            description=record.provider,
            source_record_id=record.id,
        )
        session.commit()
        session.refresh(record)

    return MedicalRecordResponse(id=record.id, **payload.model_dump())
