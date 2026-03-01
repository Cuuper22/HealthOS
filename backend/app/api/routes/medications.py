from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.api.schemas import MedicationCreate, MedicationResponse
from app.database import SessionLocal
from app.models.medication import Medication
from app.services.timeline import create_timeline_event
from app.utils.auth import get_current_user_id

router = APIRouter(prefix="/api/medications", tags=["medications"])


@router.get("/", response_model=list[MedicationResponse])
def list_medications(
    current_user_id: str = Depends(get_current_user_id), skip: int = 0, limit: int = 100
) -> list[MedicationResponse]:
    """Get medications with pagination (skip, limit)."""
    limit = min(limit, 1000)
    with SessionLocal() as session:
        medications = (
            session.execute(
                select(Medication)
                .where(Medication.user_id == current_user_id)
                .offset(skip)
                .limit(limit)
            )
            .scalars()
            .all()
        )
        return [
            MedicationResponse(
                id=medication.id,
                user_id=medication.user_id,
                name=medication.name,
                dosage=medication.dosage,
                start_date=medication.start_date,
                end_date=medication.end_date,
                status=medication.status,
                notes=medication.notes,
            )
            for medication in medications
        ]


@router.post("/", response_model=MedicationResponse)
def create_medication(
    payload: MedicationCreate, current_user_id: str = Depends(get_current_user_id)
) -> MedicationResponse:
    # Override user_id from token
    payload.user_id = current_user_id
    with SessionLocal() as session:
        medication = Medication(**payload.model_dump())
        session.add(medication)
        session.flush()
        create_timeline_event(
            session,
            user_id=medication.user_id,
            event_type="medication",
            event_date=datetime.combine(
                medication.start_date or datetime.utcnow().date(), datetime.min.time()
            ),
            module_name="medications",
            title=medication.name,
            description=medication.dosage,
            source_record_id=medication.id,
        )
        session.commit()
        session.refresh(medication)

    return MedicationResponse(id=medication.id, **payload.model_dump())
