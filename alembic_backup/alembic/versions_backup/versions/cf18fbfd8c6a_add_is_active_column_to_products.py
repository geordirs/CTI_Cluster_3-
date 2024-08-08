"""Add is_active column to products

Revision ID: cf18fbfd8c6a
Revises: <id_de_la_revision_anterior>
Create Date: 2023-08-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cf18fbfd8c6a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('products', sa.Column('is_active', sa.Boolean(), nullable=True, server_default=sa.text('true')))

def downgrade():
    op.drop_column('products', 'is_active')
