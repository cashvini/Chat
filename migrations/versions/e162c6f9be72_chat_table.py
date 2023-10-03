"""chat table

Revision ID: e162c6f9be72
Revises: 73d5161d57ce
Create Date: 2023-05-16 10:35:38.260273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e162c6f9be72'
down_revision = '73d5161d57ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
