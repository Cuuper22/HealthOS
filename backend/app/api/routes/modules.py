from fastapi import APIRouter

from app.modules.registry import get_module_status

router = APIRouter(prefix="/api/modules", tags=["modules"])


@router.get("/")
def list_modules() -> list[dict[str, object]]:
    return get_module_status()
