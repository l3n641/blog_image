"""image table

Revision ID: cada4a188012
Revises: 
Create Date: 2019-04-11 16:41:12.420444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cada4a188012'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('delete_time', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('img_id', sa.Integer(), nullable=True),
    sa.Column('bookmarked', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###
