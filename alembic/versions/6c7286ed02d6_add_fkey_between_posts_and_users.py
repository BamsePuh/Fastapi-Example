"""add fkey between posts and users

Revision ID: 6c7286ed02d6
Revises: 218e294bac83
Create Date: 2022-04-11 16:45:15.254572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c7286ed02d6'
down_revision = '218e294bac83'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fkey', table_name='posts')
    pass
