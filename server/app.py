#!/usr/bin/env python3
import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Vocab

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Vocabs(Resource):
    def get(self):
        vocab_words = [vocab.to_dict() for vocab in Vocab.query.all()]
        return make_response(jsonify(vocab_words), 200)

api.add_resource(Vocabs, '/vocab')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
