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


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordReset(BaseModel):
    token: str
    new_password: str


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

    def model_post_init(self, __context):
        """Validate dosage field for realistic values."""
        if self.dosage:
            # Check for negative numbers in dosage
            import re

            numbers = re.findall(r"\d+\.?\d*", self.dosage)
            for num_str in numbers:
                num = float(num_str)
                if num < 0:
                    raise ValueError("Dosage cannot contain negative values")
                if num > 100000:  # Absurdly high dosage
                    raise ValueError("Dosage value is unrealistically high")

        # Validate date range
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValueError("End date cannot be before start date")


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
