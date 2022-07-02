"""add foreign-key to posts table

Revision ID: 86156649e83b
Revises: 6ee2d9ab7b58
Create Date: 2022-07-02 10:20:58.040752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86156649e83b'
down_revision = '6ee2d9ab7b58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:  
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
