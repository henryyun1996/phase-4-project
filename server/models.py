from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class ModuleContent(db.Model, SerializerMixin):
    __tablename__ = 'module_contents'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String)
    content = db.Column(db.String)
    lesson_level = db.Column(db.Integer)

    users = db.relationship('User', backref='module_content')
    vocab_words = db.relationship('Vocab', backref='module_content')
    favorites = db.relationship('Favorite', backref='module_content')

    users = association_proxy('user_modules', 'user')

    def __repr__(self):
        return f"<ModuleContent(id={self.id}, video_url='{self.video_url}', content='{self.content}', lesson_level={self.lesson_level})>"

class Vocab(db.Model, SerializerMixin):
    __tablename__ = 'vocab_words'

    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String)
    croatian_word = db.Column(db.String)

    module_content_id = db.Column(db.Integer, db.ForeignKey('module_contents.id'))

    def __repr__(self):
        return f"<Vocab(id={self.id}, english_word='{self.english_word}', croatian_word='{self.croatian_word}')>"

class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorited_words'

    id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String)
    module_content_id = db.Column(db.Integer, db.ForeignKey('module_contents.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Favorite(id={self.id}, content={self.content} module_content_id={self.module_content_id}, user_id={self.user_id})>"

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    progress_percentage = db.Column(db.Integer)

    current_module_id = db.Column(db.Integer, db.ForeignKey('module_contents.id'))

    favorites = db.relationship('Favorite', backref='user')
    modules = association_proxy('user_modules', 'module_content')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', password='{self.password}', progress_percentage={self.progress_percentage})>"
