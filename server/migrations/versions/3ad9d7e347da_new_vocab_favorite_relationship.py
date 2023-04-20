"""new vocab favorite relationship

Revision ID: 3ad9d7e347da
Revises: bd382f44ab69
Create Date: 2023-04-19 10:12:10.007818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ad9d7e347da'
down_revision = 'bd382f44ab69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorited_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vocab_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_favorited_words_module_content_id_module_contents', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_favorited_words_vocab_id_vocab_words'), 'vocab_words', ['vocab_id'], ['id'])
        batch_op.drop_column('module_content_id')

    with op.batch_alter_table('vocab_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_vocab_words_module_content_id_module_contents', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_vocab_words_favorite_id_favorited_words'), 'favorited_words', ['favorite_id'], ['id'])
        batch_op.drop_column('module_content_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vocab_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('module_content_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_vocab_words_favorite_id_favorited_words'), type_='foreignkey')
        batch_op.create_foreign_key('fk_vocab_words_module_content_id_module_contents', 'module_contents', ['module_content_id'], ['id'])
        batch_op.drop_column('favorite_id')

    with op.batch_alter_table('favorited_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('module_content_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_favorited_words_vocab_id_vocab_words'), type_='foreignkey')
        batch_op.create_foreign_key('fk_favorited_words_module_content_id_module_contents', 'module_contents', ['module_content_id'], ['id'])
        batch_op.drop_column('vocab_id')

    # ### end Alembic commands ###