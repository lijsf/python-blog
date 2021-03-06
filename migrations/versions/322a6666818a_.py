"""empty message

Revision ID: 322a6666818a
Revises: None
Create Date: 2014-02-26 20:42:19.953336

"""

# revision identifiers, used by Alembic.
revision = '322a6666818a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=True),
    sa.Column('firstname', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('pwdhash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    ### end Alembic commands ###
