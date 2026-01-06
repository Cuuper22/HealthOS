from datetime import datetime

from sqlalchemy.orm import Session

from app.models.timeline_event import TimelineEvent


def create_timeline_event(
    session: Session,
    *,
    user_id: str,
    event_type: str,
    event_date: datetime,
    module_name: str,
    title: str,
    description: str | None = None,
    severity: str | None = None,
    source_record_id: str | None = None,
) -> TimelineEvent:
    event = TimelineEvent(
        user_id=user_id,
        event_type=event_type,
        event_date=event_date,
        module_name=module_name,
        source_record_id=source_record_id,
        title=title,
        description=description,
        severity=severity,
    )
    session.add(event)
    return event
