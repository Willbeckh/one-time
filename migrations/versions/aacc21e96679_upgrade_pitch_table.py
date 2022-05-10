"""Upgrade pitch table

Revision ID: aacc21e96679
Revises: 2988aea29e5e
Create Date: 2022-05-10 12:33:00.578882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aacc21e96679'
down_revision = '2988aea29e5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pitch_timestamp', table_name='pitch')
    op.drop_table('pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitch_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitch_pkey')
    )
    op.create_index('ix_pitch_timestamp', 'pitch', ['timestamp'], unique=False)
    # ### end Alembic commands ###