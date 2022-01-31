"""update call sid to unique

Revision ID: ef2c9922878b
Revises: 411241d6277b
Create Date: 2022-01-31 19:57:58.951220

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "ef2c9922878b"
down_revision = "411241d6277b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "call", ["sid"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "call", type_="unique")
    # ### end Alembic commands ###
