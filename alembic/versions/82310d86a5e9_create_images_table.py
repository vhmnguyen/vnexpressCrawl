"""create images table

Revision ID: 82310d86a5e9
Revises: ecddeb5e339a
Create Date: 2024-07-11 09:01:46.455861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82310d86a5e9'
down_revision: Union[str, None] = 'ecddeb5e339a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('image_src', sa.String(length=255), nullable=True),
    sa.Column('alt', sa.String(length=255), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    # ### end Alembic commands ###
