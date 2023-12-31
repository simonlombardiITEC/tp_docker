"""localidad fk in persona

Revision ID: 5b45e03072fb
Revises: 47cb5f331247
Create Date: 2023-06-13 20:16:15.743057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b45e03072fb'
down_revision = '47cb5f331247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persona', schema=None) as batch_op:
        batch_op.add_column(sa.Column('localidad', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'localidad', ['localidad'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persona', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('localidad')

    # ### end Alembic commands ###
