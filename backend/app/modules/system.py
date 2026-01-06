from datetime import datetime
from typing import Any

from app.modules.base import BaseModule


class SystemModule(BaseModule):
    @property
    def name(self) -> str:
        return "system"

    @property
    def display_name(self) -> str:
        return "System"

    @property
    def description(self) -> str:
        return "Core system module for HealthOS."

    @property
    def version(self) -> str:
        return "0.1.0"

    def has_data(self, user_id: str) -> bool:
        return False

    def get_data_summary(self, user_id: str) -> dict[str, Any]:
        return {"status": "no data"}

    def get_last_update(self, user_id: str) -> datetime | None:
        return None

    def import_data(self, user_id: str, file_path: str, file_type: str) -> dict[str, Any]:
        return {"imported": 0}

    def export_data(self, user_id: str, format: str) -> bytes:
        return b""

    def get_timeline_events(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> list[dict[str, Any]]:
        return []

    def get_database_models(self) -> list[Any]:
        return []
