#!/usr/bin/env python3
import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Resource, Api

from config import app, api, db
from models import db, Vocab

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        html = '<h1>Welcome to our little API!</h1>'
        return make_response(html, 200)

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

api.add_resource(Home, '/')
api.add_resource(Vocabs, '/vocab')
api.add_resource(VocabByID, '/vocab/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
