"""Create author table

Revision ID: 929216e85eed
Revises: 3a1584a69baa
Create Date: 2024-06-27 14:01:16.371243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '929216e85eed'
down_revision: Union[str, None] = '3a1584a69baa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("authors",
                    sa.Column('id', sa.String(length=36), primary_key=True),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'))


def downgrade() -> None:
    op.drop_table("authors")
