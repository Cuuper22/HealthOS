from fastapi import APIRouter, File, Form, UploadFile

from app.database import SessionLocal
from app.services.imports import create_import_record, save_upload

router = APIRouter(prefix="/api/imports", tags=["imports"])


@router.post("/")
def import_data(
    user_id: str = Form(...),
    module_name: str = Form(...),
    file_type: str | None = Form(None),
    file: UploadFile = File(...),
) -> dict[str, object]:
    with SessionLocal() as session:
        saved_path = save_upload(file.filename, file.file)
        record = create_import_record(
            session,
            user_id=user_id,
            module_name=module_name,
            file_name=file.filename,
            file_type=file_type,
        )
        session.commit()
        session.refresh(record)

    return {
        "import_id": record.id,
        "status": record.status,
        "file_path": str(saved_path),
    }
