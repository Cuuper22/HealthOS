from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from sqlalchemy import select

from app.config import settings
from app.database import SessionLocal
from app.models.user import User

security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Dependency to extract and validate JWT token from Authorization header.
    Returns the authenticated user.
    """
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    with SessionLocal() as session:
        user = session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
        if user is None:
            raise credentials_exception

    return user


def get_current_user_id(user: User = Depends(get_current_user)) -> str:
    """
    Dependency to get just the user ID from the authenticated user.
    """
    return user.id
