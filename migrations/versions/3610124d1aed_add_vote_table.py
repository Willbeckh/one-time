"""Add vote table

Revision ID: 3610124d1aed
Revises: ad5e33c7d5dd
Create Date: 2022-05-12 12:46:42.231004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3610124d1aed'
down_revision = 'ad5e33c7d5dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('votes_user_id_fkey', 'votes', type_='foreignkey')
    op.drop_column('votes', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('votes_user_id_fkey', 'votes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###