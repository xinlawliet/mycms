"""empty message

Revision ID: a1a17081190e
Revises: 2d52f845fa8f
Create Date: 2018-09-20 20:47:38.062494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1a17081190e'
down_revision = '2d52f845fa8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('message_ibfk_2', 'message', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('message_ibfk_2', 'message', 'front_user', ['reciver_id'], ['id'])
    # ### end Alembic commands ###
