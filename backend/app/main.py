from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from app.api.routes import auth, imports, labs, medical_records, medications, modules, timeline
from app.database import Base, engine
from app.modules.labs import LabsModule
from app.modules.medical_records import MedicalRecordsModule
from app.modules.medications import MedicationsModule
from app.modules.registry import ModuleRegistry
from app.modules.system import SystemModule
from app.utils.exceptions import (
    APIException,
    api_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.utils.logging import configure_logging

app = FastAPI(title="HealthOS")

# Exception handlers for consistent error responses
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# CORS middleware - allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default + common React port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
