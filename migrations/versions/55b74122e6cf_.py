"""empty message

Revision ID: 55b74122e6cf
Revises: 
Create Date: 2020-04-08 11:50:02.982663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55b74122e6cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inn', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=300), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_store_email'), 'store', ['email'], unique=True)
    op.create_index(op.f('ix_store_inn'), 'store', ['inn'], unique=True)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=300), nullable=True),
    sa.Column('bookname', sa.String(length=300), nullable=True),
    sa.Column('storenum', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=False)
    op.create_index(op.f('ix_book_bookname'), 'book', ['bookname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_bookname'), table_name='book')
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_store_inn'), table_name='store')
    op.drop_index(op.f('ix_store_email'), table_name='store')
    op.drop_table('store')
    # ### end Alembic commands ###
