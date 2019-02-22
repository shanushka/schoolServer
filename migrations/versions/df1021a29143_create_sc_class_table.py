"""create sc_class table

Revision ID: df1021a29143
Revises: a770c8c7f4b2
Create Date: 2019-02-13 14:39:38.513892

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'df1021a29143'
down_revision = 'a770c8c7f4b2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('sc_class',
                    sa.Column('class_id',sa.Integer, primary_key=True),
                    sa.Column('grade',sa.Integer, nullable=False),
                    sa.Column('section',sa.CHAR, nullable=False))


def downgrade():
    op.drop_table('sc_class')
