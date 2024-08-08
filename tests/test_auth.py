import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user(client, db_session):
    response = client.post(
        "/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_existing_user(client, db_session):
    # Primero, creamos un usuario
    client.post(
        "/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    
    # Intentamos crear el mismo usuario de nuevo
    response = client.post(
        "/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

def test_login(client, db_session):
    # Primero, creamos un usuario
    client.post(
        "/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    
    response = client.post(
        "/token",
        data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client, db_session):
    # Primero, creamos un usuario
    client.post(
        "/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    
    response = client.post(
        "/token",
        data={"username": "testuser", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

