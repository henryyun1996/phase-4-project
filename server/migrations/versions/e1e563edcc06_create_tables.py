"""Create Tables

Revision ID: e1e563edcc06
Revises: 
Create Date: 2023-04-17 15:17:49.859271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1e563edcc06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('module_contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_url', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('lesson_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('progress_percentage', sa.Integer(), nullable=True),
    sa.Column('current_module_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['current_module_id'], ['module_contents.id'], name=op.f('fk_users_current_module_id_module_contents')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vocab_words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('english_word', sa.String(), nullable=True),
    sa.Column('croatian_word', sa.String(), nullable=True),
    sa.Column('module_content_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['module_content_id'], ['module_contents.id'], name=op.f('fk_vocab_words_module_content_id_module_contents')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorited_words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module_content_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['module_content_id'], ['module_contents.id'], name=op.f('fk_favorited_words_module_content_id_module_contents')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_favorited_words_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorited_words')
    op.drop_table('vocab_words')
    op.drop_table('users')
    op.drop_table('module_contents')
    # ### end Alembic commands ###
