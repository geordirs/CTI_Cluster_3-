"""Merge heads

Revision ID: 64424cd67726
Revises: 8f92a7592538
Create Date: 2023-08-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '64424cd67726'
down_revision = '8f92a7592538'
branch_labels = None
depends_on = None

def upgrade():
    # En lugar de eliminar tablas, solo añadiremos columnas si no existen
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    
    # Verificar y añadir columna low_stock_threshold a products si no existe
    if 'low_stock_threshold' not in [col['name'] for col in inspector.get_columns('products')]:
        op.add_column('products', sa.Column('low_stock_threshold', sa.Integer(), nullable=True))

    # Aquí puedes añadir más columnas o tablas si es necesario

def downgrade():
    # Aquí puedes especificar cómo deshacer los cambios si es necesario
    pass
