"""empty message

Revision ID: 290eeb9858c1
Revises: 7e934008d2e5
Create Date: 2020-02-16 21:29:07.149501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290eeb9858c1'
down_revision = '7e934008d2e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('uid', sa.Integer(), nullable=False))
    op.drop_column('User', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('User', 'uid')
    # ### end Alembic commands ###