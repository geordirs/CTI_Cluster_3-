from app.database import engine, init_db
from sqlalchemy import inspect

init_db()
inspector = inspect(engine)

print("Tablas en la base de datos:")
for table_name in inspector.get_table_names():
    print(table_name)
    for column in inspector.get_columns(table_name):
        print(f"  {column['name']}: {column['type']}")