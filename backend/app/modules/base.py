from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class BaseModule(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def display_name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        raise NotImplementedError

    @property
    def dependencies(self) -> list[str]:
        return []

    @property
    def enhances(self) -> list[str]:
        return []

    @abstractmethod
    def has_data(self, user_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_data_summary(self, user_id: str) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_last_update(self, user_id: str) -> datetime | None:
        raise NotImplementedError

    @abstractmethod
    def import_data(self, user_id: str, file_path: str, file_type: str) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def export_data(self, user_id: str, format: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def get_timeline_events(
        self, user_id: str, start_date: datetime, end_date: datetime
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    def query_related_module(self, module_name: str, query: dict[str, Any]) -> Any | None:
        from app.modules.registry import ModuleRegistry

        registry = ModuleRegistry()

        if not registry.is_module_available(module_name):
            return None

        module = registry.get_module(module_name)
        if not module.has_data(query.get("user_id")):
            return None

        return module.execute_query(query)

    def execute_query(self, query: dict[str, Any]) -> Any:
        raise NotImplementedError("Module does not support cross-queries")

    def get_insights(self, user_id: str) -> list[dict[str, Any]]:
        return []

    def get_correlations(self, user_id: str, other_module: str) -> dict[str, Any] | None:
        return None

    @abstractmethod
    def get_database_models(self) -> list[Any]:
        raise NotImplementedError
