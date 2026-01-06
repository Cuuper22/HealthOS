from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
    sex: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class MedicalRecordCreate(BaseModel):
    user_id: str
    encounter_date: date
    provider: str | None = None
    diagnosis: str | None = None
    notes: str | None = None


class MedicalRecordResponse(MedicalRecordCreate):
    id: str


class LabResultCreate(BaseModel):
    user_id: str
    test_name: str
    result_value: float
    unit: str | None = None
    result_date: date
    reference_range: str | None = None
    notes: str | None = None


class LabResultResponse(LabResultCreate):
    id: str


class MedicationCreate(BaseModel):
    user_id: str
    name: str
    dosage: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: str = "active"
    notes: str | None = None


class MedicationResponse(MedicationCreate):
    id: str


class TimelineEventResponse(BaseModel):
    id: str
    user_id: str
    event_type: str
    event_date: datetime
    module_name: str
    title: str
    description: str | None = None
    severity: str | None = None
