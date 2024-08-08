"""merge heads

Revision ID: 7319021cb98c
Revises: cf18fbfd8c6a
Create Date: 2024-08-06 13:32:36.179898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7319021cb98c'
down_revision: Union[str, None] = 'cf18fbfd8c6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
