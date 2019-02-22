"""create subject table

Revision ID: 83fe326b0a4f
Revises: ee41c8033131
Create Date: 2019-02-13 14:40:34.778636

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '83fe326b0a4f'
down_revision = 'ee41c8033131'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subject', sa.Column('subject_id',sa.Integer, primary_key=True),
        sa.Column('name',sa.String(100), nullable=False),
        sa.Column('class_id',sa.Integer, sa.ForeignKey('sc_class.class_id')))


def downgrade():
    op.drop_table('subject')
