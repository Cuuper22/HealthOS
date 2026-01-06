from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings


def _ensure_database_dir() -> None:
    db_path = settings.database_url.replace("sqlite:///", "")
    Path(db_path).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


_ensure_database_dir()

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
