"""add foreign key to post table

Revision ID: 218e294bac83
Revises: a7bc97adede6
Create Date: 2022-04-11 16:38:40.093497

"""
from alembic import op
import sqlalchemy as sa
from app.models import Votes


# revision identifiers, used by Alembic.
revision = '218e294bac83'
down_revision = 'a7bc97adede6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    
    
    pass


def downgrade():
    op.drop_column('posts','owner_id')
    
    pass
