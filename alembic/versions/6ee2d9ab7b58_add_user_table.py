"""add user table

Revision ID: 6ee2d9ab7b58
Revises: d03095794e46
Create Date: 2022-07-02 09:57:21.271656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ee2d9ab7b58'
down_revision = 'd03095794e46'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
