from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.api.schemas import TimelineEventResponse
from app.database import SessionLocal
from app.models.timeline_event import TimelineEvent
from app.utils.auth import get_current_user_id

router = APIRouter(prefix="/api/timeline", tags=["timeline"])


@router.get("/", response_model=list[TimelineEventResponse])
def list_timeline(current_user_id: str = Depends(get_current_user_id)) -> list[TimelineEventResponse]:
    with SessionLocal() as session:
        events = (
            session.execute(
                select(TimelineEvent)
                .where(TimelineEvent.user_id == current_user_id)
                .order_by(TimelineEvent.event_date.desc())
            )
            .scalars()
            .all()
        )
        return [
            TimelineEventResponse(
                id=event.id,
                user_id=event.user_id,
                event_type=event.event_type,
                event_date=event.event_date,
                module_name=event.module_name,
                title=event.title,
                description=event.description,
                severity=event.severity,
            )
            for event in events
        ]
