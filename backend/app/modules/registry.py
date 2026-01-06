from collections.abc import Iterable
from typing import Any

from sqlalchemy import select

from app.database import SessionLocal
from app.models.module_registry import ModuleRegistry as ModuleRegistryModel
from app.modules.base import BaseModule


class ModuleRegistry:
    _modules: dict[str, BaseModule] = {}

    def __init__(self) -> None:
        self._modules = ModuleRegistry._modules

    def register(self, module: BaseModule) -> None:
        self._modules[module.name] = module
        self._sync_to_database(module)

    def register_all(self, modules: Iterable[BaseModule]) -> None:
        for module in modules:
            self.register(module)

    def get_module(self, name: str) -> BaseModule:
        return self._modules[name]

    def list_modules(self) -> list[BaseModule]:
        return list(self._modules.values())

    def is_module_available(self, name: str) -> bool:
        return name in self._modules

    def _sync_to_database(self, module: BaseModule) -> None:
        with SessionLocal() as session:
            existing = session.execute(
                select(ModuleRegistryModel).where(ModuleRegistryModel.module_name == module.name)
            ).scalar_one_or_none()
            if existing:
                existing.display_name = module.display_name
                existing.description = module.description
                existing.version = module.version
                session.add(existing)
            else:
                session.add(
                    ModuleRegistryModel(
                        module_name=module.name,
                        display_name=module.display_name,
                        description=module.description,
                        version=module.version,
                    )
                )
            session.commit()


def get_module_status() -> list[dict[str, Any]]:
    with SessionLocal() as session:
        modules = session.execute(select(ModuleRegistryModel)).scalars().all()
        return [
            {
                "module_name": module.module_name,
                "display_name": module.display_name,
                "description": module.description,
                "version": module.version,
                "is_enabled": module.is_enabled,
                "has_data": module.has_data,
                "last_data_update": module.last_data_update,
            }
            for module in modules
        ]
