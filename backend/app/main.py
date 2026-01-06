from fastapi import FastAPI

from app.api.routes import auth, modules
from app.database import Base, engine
from app.modules.registry import ModuleRegistry
from app.modules.system import SystemModule

app = FastAPI(title="HealthOS")


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)
    registry = ModuleRegistry()
    registry.register(SystemModule())


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(modules.router)
