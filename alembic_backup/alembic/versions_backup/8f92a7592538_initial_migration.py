"""Initial migration

Revision ID: 8f92a7592538
Revises: 
Create Date: 2023-08-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8f92a7592538'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Verifica si la columna ya existe antes de intentar añadirla
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('products')
    if 'low_stock_threshold' not in [col['name'] for col in columns]:
        op.add_column('products', sa.Column('low_stock_threshold', sa.Integer(), nullable=True))

def downgrade():
    # Elimina la columna solo si existe
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('products')
    if 'low_stock_threshold' in [col['name'] for col in columns]:
        op.drop_column('products', 'low_stock_threshold')
