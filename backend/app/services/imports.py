from pathlib import Path
from typing import BinaryIO

from sqlalchemy.orm import Session

from app.models.data_import import DataImport


BASE_DIR = Path(__file__).resolve().parents[3]
UPLOAD_DIR = BASE_DIR / "data" / "uploads"


def save_upload(file_name: str, file_stream: BinaryIO) -> Path:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    destination = UPLOAD_DIR / file_name
    with destination.open("wb") as output:
        output.write(file_stream.read())
    return destination


def create_import_record(
    session: Session,
    *,
    user_id: str,
    module_name: str,
    file_name: str | None,
    file_type: str | None,
) -> DataImport:
    record = DataImport(
        user_id=user_id,
        module_name=module_name,
        file_name=file_name,
        file_type=file_type,
        status="completed",
        records_imported=0,
    )
    session.add(record)
    return record
