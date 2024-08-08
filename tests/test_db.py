import logging
from app.database import engine, init_db, Base
from sqlalchemy import inspect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_database_tables():
    logger.info("Initializing database...")
    init_db()
    logger.info("Database initialized.")

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    logger.info(f"Tables found: {tables}")
    
    assert "users" in tables, "Users table not found in the database"
    assert "products" in tables, "Products table not found in the database"
    
    if "users" in tables:
        user_columns = [column['name'] for column in inspector.get_columns('users')]
        logger.info(f"User columns: {user_columns}")
        assert all(col in user_columns for col in ['id', 'username', 'email', 'password_hash', 'is_active']), "Missing columns in users table"
    
    if "products" in tables:
        product_columns = [column['name'] for column in inspector.get_columns('products')]
        logger.info(f"Product columns: {product_columns}")
        assert all(col in product_columns for col in ['id', 'name', 'description', 'price', 'stock_quantity']), "Missing columns in products table"