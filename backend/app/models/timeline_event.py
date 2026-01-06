from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import TimestampedBase


class TimelineEvent(TimestampedBase):
    __tablename__ = "timeline_events"

    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    event_type: Mapped[str] = mapped_column(String, nullable=False)
    event_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    module_name: Mapped[str] = mapped_column(String, nullable=False)
    source_record_id: Mapped[str | None] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    severity: Mapped[str | None] = mapped_column(String, nullable=True)
    metadata: Mapped[dict] = mapped_column(JSON, default=dict)

    __table_args__ = (
        Index("idx_timeline_user_date", "user_id", "event_date"),
        Index("idx_timeline_module", "module_name"),
    )
