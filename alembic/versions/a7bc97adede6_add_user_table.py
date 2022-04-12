"""add user table

Revision ID: a7bc97adede6
Revises: 846f044b587a
Create Date: 2022-04-11 05:35:31.776883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7bc97adede6'
down_revision = '846f044b587a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(),nullable=False),
                    sa.Column('email', sa.String(),nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=False), 
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')  
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
