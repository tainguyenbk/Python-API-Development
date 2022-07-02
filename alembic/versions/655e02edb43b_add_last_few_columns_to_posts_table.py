"""add last few columns to posts table

Revision ID: 655e02edb43b
Revises: 86156649e83b
Create Date: 2022-07-02 10:29:07.277043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655e02edb43b'
down_revision = '86156649e83b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
