from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.api.schemas import LabResultCreate, LabResultResponse
from app.database import SessionLocal
from app.models.lab_result import LabResult
from app.services.timeline import create_timeline_event
from app.utils.auth import get_current_user_id

router = APIRouter(prefix="/api/labs", tags=["labs"])


@router.get("/", response_model=list[LabResultResponse])
def list_results(current_user_id: str = Depends(get_current_user_id)) -> list[LabResultResponse]:
    with SessionLocal() as session:
        results = (
            session.execute(select(LabResult).where(LabResult.user_id == current_user_id))
            .scalars()
            .all()
        )
        return [
            LabResultResponse(
                id=result.id,
                user_id=result.user_id,
                test_name=result.test_name,
                result_value=result.result_value,
                unit=result.unit,
                result_date=result.result_date,
                reference_range=result.reference_range,
                notes=result.notes,
            )
            for result in results
        ]


@router.post("/", response_model=LabResultResponse)
def create_result(
    payload: LabResultCreate, current_user_id: str = Depends(get_current_user_id)
) -> LabResultResponse:
    # Override user_id from token
    payload.user_id = current_user_id
    with SessionLocal() as session:
        result = LabResult(**payload.model_dump())
        session.add(result)
        session.flush()
        create_timeline_event(
            session,
            user_id=result.user_id,
            event_type="lab_result",
            event_date=datetime.combine(result.result_date, datetime.min.time()),
            module_name="labs",
            title=result.test_name,
            description=f"{result.result_value} {result.unit or ''}".strip(),
            source_record_id=result.id,
        )
        session.commit()
        session.refresh(result)

    return LabResultResponse(id=result.id, **payload.model_dump())
