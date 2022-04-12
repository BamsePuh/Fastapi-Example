"""create post table

Revision ID: 678616bfff9f
Revises: 
Create Date: 2022-04-10 18:40:10.324357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '678616bfff9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(),nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
