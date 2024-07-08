"""Create main navbar table

Revision ID: 74951996dae3
Revises: 
Create Date: 2024-06-24 13:44:06.687181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74951996dae3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("main_navbar",
                    sa.Column('id', sa.String(length=36), primary_key=True),
                    sa.Column('url', sa.String(length=255), nullable=True),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'))


def downgrade() -> None:
    op.drop_table("main_navbar")
