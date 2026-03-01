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

    # Rate limiting
    rate_limit_auth: int = 5  # requests per minute for auth endpoints
    rate_limit_api: int = 60  # requests per minute for API endpoints

    # Email configuration (for password reset)
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    from_email: str = "noreply@healthos.example.com"
    frontend_url: str = "http://localhost:5173"

    class Config:
        env_prefix = "HEALTHOS_"


settings = Settings()
