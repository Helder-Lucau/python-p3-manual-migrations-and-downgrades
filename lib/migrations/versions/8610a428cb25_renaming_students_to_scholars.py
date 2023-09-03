"""Renaming students to scholars

Revision ID: 8610a428cb25
Revises: 791279dd0760
Create Date: 2023-09-03 18:34:34.933865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8610a428cb25'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
