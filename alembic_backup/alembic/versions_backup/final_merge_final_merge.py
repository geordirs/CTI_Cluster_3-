"""final merge

Revision ID: final_merge
Revises: merge_final
Create Date: 2024-08-06 18:19:19.245755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'final_merge'
down_revision: Union[str, None] = 'merge_final'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
