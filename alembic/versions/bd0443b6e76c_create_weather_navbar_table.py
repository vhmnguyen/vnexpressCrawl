"""Create weather navbar table

Revision ID: bd0443b6e76c
Revises: 74951996dae3
Create Date: 2024-06-24 13:47:16.865565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd0443b6e76c'
down_revision: Union[str, None] = '74951996dae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("weather_navbar",
                    sa.Column('id', sa.String(length=36), primary_key=True),
                    sa.Column('url', sa.String(length=255), nullable=True),
                    sa.Column('location', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'))

def downgrade() -> None:
    op.drop_table("weather_navbar")
