"""Initial migration

Revision ID: 4bb23277bc8f
Revises: 
Create Date: 2024-08-07 19:28:56.692722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bb23277bc8f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('posts', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'updated_at')
    op.drop_column('posts', 'created_at')
    # ### end Alembic commands ###
