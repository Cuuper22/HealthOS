from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "HealthOS"
    environment: str = "development"
    database_url: str = "sqlite:///../data/database/healthos.db"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    log_level: str = "INFO"
    encryption_key: str = "change-me"

    class Config:
        env_prefix = "HEALTHOS_"


settings = Settings()
