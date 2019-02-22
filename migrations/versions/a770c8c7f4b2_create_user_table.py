"""create user table

Revision ID: a770c8c7f4b2
Revises: d1494702ca5b
Create Date: 2019-02-13 14:38:51.827255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'a770c8c7f4b2'
down_revision = 'd1494702ca5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('user_id',UUID(as_uuid=True), primary_key=True),
                    sa.Column('name',sa.String(100), nullable=False),
                    sa.Column('password',sa.String),
                    sa.Column('email',sa.String),
                    sa.Column('contact_number',sa.BigInteger),
                    sa.Column('role_id',sa.Integer, sa.ForeignKey("role.role_id"))
                    )


def downgrade():
    op.drop_table('users')
