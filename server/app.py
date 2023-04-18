#!/usr/bin/env python3
import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Resource, Api

from config import app, api, db
from models import db, Vocab, ModuleContent, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        welcome_message = '<h1>Welcome to our little API!</h1>'
        return make_response(welcome_message, 200)

class Vocabs(Resource):
    def get(self):
        vocab_words = [vocab.to_dict() for vocab in Vocab.query.all()]
        return make_response(jsonify(vocab_words), 200)

class VocabByID(Resource):
    def get(self, id):
        vocab_word = Vocab.query.filter_by(id=id).first()
        if vocab_word:
            return make_response(vocab_word.to_dict())
        else:
            return make_response({"error": "Vocab word not found"}, 404)

class ModuleContents(Resource):
    def get(self):
        module_contents = [mc.to_dict() for mc in ModuleContent.query.all()]
        return make_response(jsonify(module_contents), 200)

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(user.to_dict())
        elif User.query.count() == 0:
            message = '<h1>Sorry, there are no registered users yet.</h1>'
            return make_response(message, 404)
        else:
            return make_response({"error": "No User found"}, 404)
    
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        new_username = request.json.get()['username']
        new_password = request.json.get()['password']

        if new_username:
            user.username = new_username
        if new_password:
            user.password = new_password

        db.session.commit()
        return make_response(user.to_dict(), 200)
    
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 200)

class Favorite(Resource):
    def post(self, user_id, vocab_id):
        user = User.query.get(user_id)
        vocab = Vocab.query.get(vocab_id)
        if not user or not vocab:
            return make_response({"error": "User or Vocab not found"}, 404)
        user.favorites.append(vocab)
        db.session.commit()
        return make_response({"message": "Vocab added to favorites successfully"}, 200)
    
    def delete(self, user_id, vocab_id):
        user = User.query.get(user_id)
        vocab = Vocab.query.get(vocab_id)
        if not user or not vocab:
            return make_response({"error": "User or Vocab not found"}, 404)
        if vocab in user.favorites:
            user.favorites.remove(vocab)
            db.session.commit()
            return make_response({"message": "Vocab removed from favorites successfully"}, 200)
        else:
            return make_response({"error": "Vocab not in favorites"}, 404)


api.add_resource(Home, '/')
api.add_resource(Vocabs, '/vocab')
api.add_resource(VocabByID, '/vocab/<int:id>')
api.add_resource(ModuleContents, '/module')
api.add_resource(UserByID, '/user/<int:id>')
api.add_resource(Favorite, '/user/<int:user_id>/vocab/<int:vocab_id>/favorite')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
