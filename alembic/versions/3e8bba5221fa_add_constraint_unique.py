"""add constraint unique

Revision ID: 3e8bba5221fa
Revises: 2a6271756df6
Create Date: 2024-07-09 13:45:26.913662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e8bba5221fa'
down_revision: Union[str, None] = '2a6271756df6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'sub_navbar', ['url'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sub_navbar', type_='unique')
    # ### end Alembic commands ###
