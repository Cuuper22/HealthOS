from fastapi.testclient import TestClient
from jose import jwt

from app.config import settings
from app.database import Base, engine
from app.main import app
from app.utils.security import create_access_token, hash_password, verify_password

client = TestClient(app)


def setup_module() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_password_hashing() -> None:
    password = "supersecret"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrongpassword", hashed)


def test_create_access_token() -> None:
    user_id = "test-user-123"
    token = create_access_token(user_id)
    
    # Verify token can be decoded
    payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    assert payload["sub"] == user_id
    assert "exp" in payload


def test_register_success() -> None:
    response = client.post(
        "/api/auth/register",
        json={
            "email": "newuser@example.com",
            "password": "testpass123",
            "first_name": "New",
            "last_name": "User",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "newuser@example.com"
    assert data["user"]["first_name"] == "New"


def test_register_duplicate_email() -> None:
    # First registration
    client.post(
        "/api/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "testpass123",
        },
    )
    
    # Attempt duplicate registration
    response = client.post(
        "/api/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "testpass123",
        },
    )
    assert response.status_code == 409


def test_login_success() -> None:
    # Register user
    client.post(
        "/api/auth/register",
        json={
            "email": "login@example.com",
            "password": "testpass123",
        },
    )
    
    # Login
    response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "testpass123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "login@example.com"


def test_login_invalid_credentials() -> None:
    # Register user
    client.post(
        "/api/auth/register",
        json={
            "email": "badlogin@example.com",
            "password": "testpass123",
        },
    )
    
    # Try wrong password
    response = client.post(
        "/api/auth/login",
        json={
            "email": "badlogin@example.com",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == 401


def test_login_nonexistent_user() -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "email": "doesnotexist@example.com",
            "password": "testpass123",
        },
    )
    assert response.status_code == 401


def test_protected_endpoint_with_valid_token() -> None:
    # Register and get token
    reg_response = client.post(
        "/api/auth/register",
        json={
            "email": "protected@example.com",
            "password": "testpass123",
        },
    )
    token = reg_response.json()["access_token"]
    
    # Access protected endpoint
    response = client.get(
        "/api/timeline/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_protected_endpoint_without_token() -> None:
    response = client.get("/api/timeline/")
    assert response.status_code == 403


def test_protected_endpoint_with_invalid_token() -> None:
    response = client.get(
        "/api/timeline/",
        headers={"Authorization": "Bearer invalid-token-here"},
    )
    assert response.status_code == 401
