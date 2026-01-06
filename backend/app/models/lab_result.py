from datetime import date

from sqlalchemy import Date, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import TimestampedBase


class LabResult(TimestampedBase):
    __tablename__ = "lab_results"

    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    test_name: Mapped[str] = mapped_column(String, nullable=False)
    result_value: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str | None] = mapped_column(String, nullable=True)
    result_date: Mapped[date] = mapped_column(Date, nullable=False)
    reference_range: Mapped[str | None] = mapped_column(String, nullable=True)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)
