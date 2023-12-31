"""empty message

Revision ID: ef5d6ce37cc0
Revises: 
Create Date: 2023-09-12 13:22:26.818980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5d6ce37cc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dilemma',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('choice_a', sa.String(length=25), nullable=False),
    sa.Column('choice_b', sa.String(length=25), nullable=False),
    sa.Column('c_score', sa.Float(), nullable=False),
    sa.Column('d_score', sa.Float(), nullable=False),
    sa.Column('v_score', sa.Float(), nullable=False),
    sa.Column('n_score', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=75), nullable=False),
    sa.Column('username', sa.String(length=75), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('c_score', sa.Float(), nullable=False),
    sa.Column('d_score', sa.Float(), nullable=False),
    sa.Column('v_score', sa.Float(), nullable=False),
    sa.Column('n_score', sa.Float(), nullable=False),
    sa.Column('last_dilemma', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['last_dilemma'], ['dilemma.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_token'), ['token'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_token'))

    op.drop_table('user')
    op.drop_table('dilemma')
    # ### end Alembic commands ###
