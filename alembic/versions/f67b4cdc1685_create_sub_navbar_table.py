"""Create sub navbar table

Revision ID: f67b4cdc1685
Revises: bd0443b6e76c
Create Date: 2024-06-26 08:26:40.998256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f67b4cdc1685'
down_revision: Union[str, None] = 'bd0443b6e76c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("sub_navbar",
                    sa.Column('id', sa.String(length=36), primary_key=True),
                    sa.Column('url', sa.String(length=255), nullable=True),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'))

def downgrade() -> None:
    op.drop_table("sub_navbar")
