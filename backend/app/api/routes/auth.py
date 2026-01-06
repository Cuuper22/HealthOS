from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.api.schemas import TokenResponse, UserCreate, UserLogin, UserResponse
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
def register(user: UserCreate) -> TokenResponse:
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
def login(credentials: UserLogin) -> TokenResponse:
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
