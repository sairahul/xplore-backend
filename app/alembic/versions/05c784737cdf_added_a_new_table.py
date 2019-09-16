"""Added a new table

Revision ID: 05c784737cdf
Revises: d4867f3a4c0a
Create Date: 2019-09-08 14:26:13.238332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c784737cdf'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('base_dir', sa.String(), nullable=True),
    sa.Column('thumbnail_dir', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dataset_id'), 'dataset', ['id'], unique=False)
    op.create_index(op.f('ix_dataset_name'), 'dataset', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dataset_name'), table_name='dataset')
    op.drop_index(op.f('ix_dataset_id'), table_name='dataset')
    op.drop_table('dataset')
    # ### end Alembic commands ###