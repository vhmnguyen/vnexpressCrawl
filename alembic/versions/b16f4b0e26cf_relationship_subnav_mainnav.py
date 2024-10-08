"""relationship subnav mainnav

Revision ID: b16f4b0e26cf
Revises: 9fec9bffd00b
Create Date: 2024-07-10 11:24:25.787683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b16f4b0e26cf'
down_revision: Union[str, None] = '9fec9bffd00b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sub_navbar', sa.Column('parent_category', sa.String(length=255), nullable=True))
    op.create_foreign_key(None, 'sub_navbar', 'main_navbar', ['parent_category'], ['url'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sub_navbar', type_='foreignkey')
    op.drop_column('sub_navbar', 'parent_category')
    # ### end Alembic commands ###
