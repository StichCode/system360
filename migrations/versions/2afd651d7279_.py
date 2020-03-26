"""empty message

Revision ID: 2afd651d7279
Revises: 
Create Date: 2020-03-26 11:14:50.889982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2afd651d7279'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('franchises',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=12), server_default='', nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=100), server_default='', nullable=True),
    sa.Column('last_name', sa.String(length=100), server_default='', nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('franchise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['franchise_id'], ['franchises.id'], ),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('shops',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=12), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_table('checkouts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False, comment='время начала задачи'),
    sa.Column('end', sa.DateTime(), nullable=False, comment='время конца задачи'),
    sa.Column('worker', sa.Integer(), nullable=False, comment='пользователь с ролью работник'),
    sa.Column('type', sa.Enum('regular', 'extraordinary', name='typecheckout'), nullable=False, comment='Тип проверки'),
    sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
    sa.ForeignKeyConstraint(['worker'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('objects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('type', sa.String(length=64), nullable=False),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('checkout', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False, comment='статус задачи'),
    sa.Column('title', sa.String(length=100), nullable=False, comment='название задачи'),
    sa.ForeignKeyConstraint(['checkout'], ['checkouts.id'], ),
    sa.ForeignKeyConstraint(['object_id'], ['objects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False, comment='название подзадачи'),
    sa.ForeignKeyConstraint(['task'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_tasks')
    op.drop_table('tasks')
    op.drop_table('objects')
    op.drop_table('checkouts')
    op.drop_table('shops')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('franchises')
    # ### end Alembic commands ###