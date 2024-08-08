"""Final merge of all heads

Revision ID: final_merge
Revises: final_merge
Create Date: 2024-08-06 18:25:04.886200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'final_merge'
down_revision: Union[str, None] = 'final_merge'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
