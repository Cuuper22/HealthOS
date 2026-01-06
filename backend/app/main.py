from fastapi import FastAPI

from app.api.routes import auth, imports, labs, medical_records, medications, modules, timeline
from app.database import Base, engine
from app.modules.labs import LabsModule
from app.modules.medical_records import MedicalRecordsModule
from app.modules.medications import MedicationsModule
from app.modules.registry import ModuleRegistry
from app.modules.system import SystemModule
from app.utils.logging import configure_logging

app = FastAPI(title="HealthOS")


@app.on_event("startup")
def startup() -> None:
    configure_logging()
    Base.metadata.create_all(bind=engine)
    registry = ModuleRegistry()
    registry.register(SystemModule())
    registry.register(MedicalRecordsModule())
    registry.register(LabsModule())
    registry.register(MedicationsModule())


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(imports.router)
app.include_router(medical_records.router)
app.include_router(labs.router)
app.include_router(medications.router)
app.include_router(modules.router)
app.include_router(timeline.router)
