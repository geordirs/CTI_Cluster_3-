"""merge multiple heads

Revision ID: merge_final
Revises: 89d5028d2dc8
Create Date: 2024-08-06 18:17:37.769859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'merge_final'
down_revision: Union[str, None] = '89d5028d2dc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
