"""merge heads2

Revision ID: 89d5028d2dc8
Revises: 7319021cb98c
Create Date: 2024-08-06 13:34:22.923554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89d5028d2dc8'
down_revision: Union[str, None] = '7319021cb98c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
