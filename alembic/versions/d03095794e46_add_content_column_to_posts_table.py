"""add content column to posts table

Revision ID: d03095794e46
Revises: ff1a4a504c0c
Create Date: 2022-07-02 09:50:13.849704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd03095794e46'
down_revision = 'ff1a4a504c0c'
branch_labels = None
depends_on = None
 

def upgrade() -> None:
    op.create_table('users', 
                        sa.Column('id', sa.Integer(), nullable=False),
                        sa.Column('email', sa.String(), nullable=False),
                        sa.Column('password', sa.String(), nullable=False),
                        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text('now()'), nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                        sa.UniqueConstraint('email')
                        )
    pass


def downgrade() -> None:
    op.drop_column('users')
    pass
