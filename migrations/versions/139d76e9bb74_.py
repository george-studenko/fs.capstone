"""empty message

Revision ID: 139d76e9bb74
Revises: 4f2cc7cbf3b7
Create Date: 2020-02-22 12:05:15.141491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '139d76e9bb74'
down_revision = '4f2cc7cbf3b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('category_id', sa.Integer(), nullable=False))
    op.add_column('Recipe', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Recipe', 'User', ['user_id'], ['id'])
    op.create_foreign_key(None, 'Recipe', 'Category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Recipe', type_='foreignkey')
    op.drop_constraint(None, 'Recipe', type_='foreignkey')
    op.drop_column('Recipe', 'user_id')
    op.drop_column('Recipe', 'category_id')
    # ### end Alembic commands ###