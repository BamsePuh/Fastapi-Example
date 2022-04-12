"""add content column to post table

Revision ID: 846f044b587a
Revises: 678616bfff9f
Create Date: 2022-04-10 18:50:58.877802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846f044b587a'
down_revision = '678616bfff9f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
