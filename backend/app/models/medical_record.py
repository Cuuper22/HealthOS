from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import TimestampedBase


class MedicalRecord(TimestampedBase):
    __tablename__ = "medical_records"

    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    encounter_date: Mapped[date] = mapped_column(Date, nullable=False)
    provider: Mapped[str | None] = mapped_column(String, nullable=True)
    diagnosis: Mapped[str | None] = mapped_column(String, nullable=True)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)
