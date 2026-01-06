from datetime import datetime

from sqlalchemy import Boolean, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import TimestampedBase


class ModuleRegistry(TimestampedBase):
    __tablename__ = "module_registry"

    module_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    version: Mapped[str | None] = mapped_column(String, nullable=True)
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    has_data: Mapped[bool] = mapped_column(Boolean, default=False)
    last_data_update: Mapped[datetime | None] = mapped_column(nullable=True)
    settings: Mapped[dict] = mapped_column(JSON, default=dict)
