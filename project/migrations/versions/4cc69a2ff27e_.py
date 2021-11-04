"""empty message

Revision ID: 4cc69a2ff27e
Revises: 800339cb98ab
Create Date: 2021-11-04 15:48:50.881344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc69a2ff27e'
down_revision = '800339cb98ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('image', sa.String(length=150), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'image')
    # ### end Alembic commands ###