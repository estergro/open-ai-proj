"""add file_key to invoices

Revision ID: c3ac971dba5e
Revises: 5964c6fda049
Create Date: 2025-07-15 08:52:32.485839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3ac971dba5e'
down_revision: Union[str, Sequence[str], None] = '5964c6fda049'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoices', sa.Column('file_key', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invoices', 'file_key')
    # ### end Alembic commands ###
