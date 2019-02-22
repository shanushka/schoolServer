"""create student table

Revision ID: ee41c8033131
Revises: df1021a29143
Create Date: 2019-02-13 14:40:24.494391

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ee41c8033131'
down_revision = 'df1021a29143'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('student',
                    sa.Column('student_id',sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('name',sa.String(100), nullable=False),
                    sa.Column('roll_number',sa.Integer),
                    sa.Column('contact_number',sa.Integer, nullable=False),
                    sa.Column('father_name',sa.String(100)),
                    sa.Column('mother_name',sa.String(100)),
                    sa.Column('class_id',sa.Integer, sa.ForeignKey("sc_class.class_id")),)


def downgrade():
    op.drop_table('student')
