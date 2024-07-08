"""Create main articles table

Revision ID: 3a1584a69baa
Revises: 1acda1789027
Create Date: 2024-06-26 10:17:50.478543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a1584a69baa'
down_revision: Union[str, None] = '1acda1789027'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("articles",
                    sa.Column('id', sa.String(length=36), primary_key=True),
                    sa.Column('url', sa.String(length=255), nullable=True),
                    sa.Column('title', sa.String(length=255), nullable=True),
                    sa.Column('published_date', sa.String(length=255), nullable=True),
                    sa.Column('author_id', sa.String(length=36), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
                    sa.PrimaryKeyConstraint('id'))


def downgrade() -> None:
    op.drop_table("articles")
