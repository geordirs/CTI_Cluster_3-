import pytest

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import User, Product

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_user(db_session):
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword")
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_create_product(db_session):
    product = Product(
        name="Test Product",
        description="This is a test product",
        price=9.99,
        stock_quantity=10,
        low_stock_threshold=2,
        category="Test",
        image_url="http://example.com/image.jpg",
        is_active=True
    )
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)
    assert product.id is not None
    assert product.name == "Test Product"
    assert product.price == 9.99

def test_query_user(db_session):
    user = User(username="testuser", email="test@example.com", password_hash="hashedpassword")
    db_session.add(user)
    db_session.commit()

    queried_user = db.query(User).filter(User.username == "testuser").first()
    assert queried_user is not None
    assert queried_user.email == "test@example.com"

def test_query_product(db_session):
    product = Product(
        name="Test Product",
        description="This is a test product",
        price=9.99,
        stock_quantity=10,
        low_stock_threshold=2,
        category="Test",
        image_url="http://example.com/image.jpg",
        is_active=True
    )
    db_session.add(product)
    db_session.commit()

    queried_product = db.query(Product).filter(Product.name == "Test Product").first()
    assert queried_product is not None
    assert queried_product.price == 9.99