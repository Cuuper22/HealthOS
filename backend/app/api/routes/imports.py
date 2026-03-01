from fastapi import APIRouter, Depends, File, Form, UploadFile

from app.database import SessionLocal
from app.services.imports import create_import_record, save_upload
from app.utils.auth import get_current_user_id

router = APIRouter(prefix="/api/imports", tags=["imports"])


@router.post("/")
def import_data(
    module_name: str = Form(...),
    file_type: str | None = Form(None),
    file: UploadFile = File(...),
    current_user_id: str = Depends(get_current_user_id),
) -> dict[str, object]:
    with SessionLocal() as session:
        saved_path = save_upload(file.filename, file.file)
        record = create_import_record(
            session,
            user_id=current_user_id,
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
