"""unique constraint

Revision ID: 37f89a10f42c
Revises: c5ac56ca99a9
Create Date: 2023-04-19 16:31:33.814650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f89a10f42c'
down_revision = 'c5ac56ca99a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vocab_words', schema=None) as batch_op:
        batch_op.drop_constraint('fk_vocab_words_favorite_id_favorited_words', type_='foreignkey')
        batch_op.drop_column('favorite_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vocab_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_vocab_words_favorite_id_favorited_words', 'favorited_words', ['favorite_id'], ['id'])

    # ### end Alembic commands ###
