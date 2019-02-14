"""create role table

Revision ID: d1494702ca5b
Revises: 
Create Date: 2019-02-13 14:38:32.796655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1494702ca5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
                    sa.Column('role_id', sa.Integer, primary_key=True),
                    sa.Column('type',sa.String))


def downgrade():
    op.drop_table('role')
