"""add column

Revision ID: fbb5a05639c0
Revises: 6791977c0a3c
Create Date: 2023-03-09 09:54:47.372548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb5a05639c0'
down_revision = '6791977c0a3c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'content' )
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
