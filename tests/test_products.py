import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Product

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

def test_create_product(client, db_session):
    # Primero, registramos un usuario y obtenemos un token
    client.post("/register", json={"username": "testuser", "email": "test@example.com", "password": "testpassword"})
    response = client.post("/token", data={"username": "testuser", "password": "testpassword"})
    token = response.json()["access_token"]
    
    # Ahora creamos un producto
    response = client.post(
        "/products/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 9.99,
            "stock_quantity": 10,
            "low_stock_threshold": 2,
            "category": "Test",
            "image_url": "http://example.com/image.jpg",
            "is_active": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert "id" in data

def test_get_products(client, db_session):
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_product(client, db_session):
    # Primero, creamos un producto
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword", is_active=True)
    db_session.add(user)
    db_session.commit()

    product = Product(name="Test Product", description="Test Description", price=9.99, stock_quantity=10, category="Test", is_active=True)
    db_session.add(product)
    db_session.commit()

    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product.id
    assert data["name"] == "Test Product"

def test_update_product(client, db_session):
    # Creamos un usuario y un producto
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword", is_active=True)
    db_session.add(user)
    db_session.commit()

    product = Product(name="Test Product", description="Test Description", price=9.99, stock_quantity=10, category="Test", is_active=True)
    db_session.add(product)
    db_session.commit()

    # Obtenemos un token
    response = client.post("/token", data={"username": "testuser", "password": "hashedpassword"})
    token = response.json()["access_token"]

    response = client.put(
        f"/products/{product.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Updated Product", "price": 19.99}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["price"] == 19.99

def test_delete_product(client, db_session):
    # Creamos un usuario y un producto
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword", is_active=True)
    db_session.add(user)
    db_session.commit()

    product = Product(name="Test Product", description="Test Description", price=9.99, stock_quantity=10, category="Test", is_active=True)
    db_session.add(product)
    db_session.commit()

    # Obtenemos un token
    response = client.post("/token", data={"username": "testuser", "password": "hashedpassword"})
    token = response.json()["access_token"]

    response = client.delete(
        f"/products/{product.id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted successfully"