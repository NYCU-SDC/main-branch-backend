"""Add tags of post.

Revision ID: 09c62acff56f
Revises: 8195b87c1a79
Create Date: 2024-08-23 20:29:37.963215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09c62acff56f'
down_revision: Union[str, None] = '8195b87c1a79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('id', sa.BigInteger().with_variant(sa.INTEGER(), 'sqlite'), nullable=False),
    sa.Column('tag', sa.String(length=20), nullable=True),
    sa.Column('post_id', sa.BigInteger().with_variant(sa.INTEGER(), 'sqlite'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_tags_id'), 'post_tags', ['id'], unique=False)
    op.create_index(op.f('ix_post_tags_tag'), 'post_tags', ['tag'], unique=False)
    op.create_foreign_key(None, 'posts', 'users', ['poster'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_index(op.f('ix_post_tags_tag'), table_name='post_tags')
    op.drop_index(op.f('ix_post_tags_id'), table_name='post_tags')
    op.drop_table('post_tags')
    # ### end Alembic commands ###
