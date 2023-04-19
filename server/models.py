from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
# you might have to run "pip install Flask-Bcrypt"
from flask_bcrypt import Bcrypt

from config import db

class ModuleContent(db.Model, SerializerMixin):
    __tablename__ = 'module_contents'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String)
    content = db.Column(db.String)
    lesson_level = db.Column(db.Integer)

    users = db.relationship('User', backref='module_content')
    vocab_words = db.relationship('Vocab', backref='module_content')

    users = association_proxy('user_modules', 'user')

    def __repr__(self):
        return f"<ModuleContent(id={self.id}, video_url='{self.video_url}', content='{self.content}', lesson_level={self.lesson_level})>"

class Vocab(db.Model, SerializerMixin):
    __tablename__ = 'vocab_words'

    serialize_rules = ('-module_content_id',)

    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String)
    croatian_word = db.Column(db.String)

    favorite_id = db.Column(db.Integer, db.ForeignKey('favorited_words.id'))
    module_content_id = db.Column(db.Integer, db.ForeignKey('module_contents.id'))

    def __repr__(self):
        return f"<Vocab(id={self.id}, english_word='{self.english_word}', croatian_word='{self.croatian_word}')>"

class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorited_words'


    id = db.Column(db.Integer, primary_key=True)
    vocab_id = db.Column(db.Integer, db.ForeignKey('vocab_words.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @validates('vocab_id','user_id')
    def check_favorites(self, key, vocab_id):
        favorites = Favorite.query.filter_by(user_id=self.user_id).all()

        for favorite in favorites:
            if vocab_id == favorite.vocab_id:
                raise ValueError('Vocab word already favorited')
            
        return vocab_id

    def __repr__(self):
        return f"<Favorite(id={self.id}, vocab_id={self.vocab_id}, user_id={self.user_id})>"

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-favorites',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    progress_percentage = db.Column(db.Integer)

    current_module_id = db.Column(db.Integer, db.ForeignKey('module_contents.id'))

    favorites = db.relationship('Favorite', backref='user')
    modules = association_proxy('user_modules', 'module_content')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', password='{self._password_hash}', progress_percentage={self.progress_percentage})>"

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
