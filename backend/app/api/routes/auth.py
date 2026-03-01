from fastapi import APIRouter, HTTPException, Request, status
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy import select

from app.api.schemas import PasswordReset, PasswordResetRequest, TokenResponse, UserCreate, UserLogin, UserResponse
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/api/auth", tags=["auth"])
limiter = Limiter(key_func=get_remote_address)


@router.post("/register", response_model=TokenResponse)
@limiter.limit("5/minute")
def register(request: Request, user: UserCreate) -> TokenResponse:
    with SessionLocal() as session:
        existing = session.execute(select(User).where(User.email == user.email)).scalar_one_or_none()
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

        new_user = User(
            email=user.email,
            password_hash=hash_password(user.password),
            first_name=user.first_name,
            last_name=user.last_name,
            date_of_birth=user.date_of_birth,
            sex=user.sex,
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    token = create_access_token(new_user.id)
    return TokenResponse(
        access_token=token,
        user=UserResponse(
            id=new_user.id,
            email=new_user.email,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
        ),
    )


@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
def login(request: Request, credentials: UserLogin) -> TokenResponse:
    with SessionLocal() as session:
        user = session.execute(select(User).where(User.email == credentials.email)).scalar_one_or_none()
        if not user or not verify_password(credentials.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(user.id)
    return TokenResponse(
        access_token=token,
        user=UserResponse(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        ),
    )


@router.post("/password-reset-request")
@limiter.limit("3/hour")
def request_password_reset(request: Request, payload: PasswordResetRequest) -> dict[str, str]:
    """Request a password reset token. Email is sent (or logged in dev mode)."""
    with SessionLocal() as session:
        user = session.execute(select(User).where(User.email == payload.email)).scalar_one_or_none()
        # Always return success to prevent email enumeration
        if not user:
            return {"message": "If the email exists, a password reset link has been sent"}

    # Create a password reset token (valid for 1 hour)
    from datetime import timedelta

    reset_token = create_access_token(user.id, expires_delta=timedelta(hours=1))

    # In development, log the reset token instead of sending email
    from app.config import settings
    import logging

    logger = logging.getLogger(__name__)

    if settings.environment == "development":
        logger.info(f"Password reset token for {user.email}: {reset_token}")
        logger.info(f"Reset URL: {settings.frontend_url}/reset-password?token={reset_token}")
    else:
        # In production, send email with reset link
        # TODO: Implement email sending
        logger.warning("Email sending not implemented - password reset token logged instead")
        logger.info(f"Password reset token for {user.email}: {reset_token}")

    return {"message": "If the email exists, a password reset link has been sent"}


@router.post("/password-reset")
@limiter.limit("5/minute")
def reset_password(request: Request, payload: PasswordReset) -> dict[str, str]:
    """Reset password using a valid reset token."""
    from jose import JWTError

    from app.config import settings

    try:
        from jose import jwt

        decoded = jwt.decode(payload.token, settings.secret_key, algorithms=[settings.algorithm])
        user_id = decoded.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid reset token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired reset token")

    with SessionLocal() as session:
        user = session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid reset token")

        user.password_hash = hash_password(payload.new_password)
        session.commit()

    return {"message": "Password has been reset successfully"}
