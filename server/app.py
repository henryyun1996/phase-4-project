#!/usr/bin/env python3
from flask import Flask, jsonify, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Resource, Api

from config import *
from models import Vocab, ModuleContent, User, Favorite

# welcome page to our API!
class Home(Resource):
    def get(self):
        welcome_message = '<h1>Welcome to our little API!</h1>'
        return make_response(welcome_message, 200)

# GET request for all Vocab words
class Vocabs(Resource):
    def get(self):
        vocab_words = [vocab.to_dict() for vocab in Vocab.query.all()]
        return make_response(jsonify(vocab_words), 200)

# GET request for individual Vocab word based off ID
class VocabByID(Resource):
    def get(self, id):
        vocab_word = Vocab.query.filter_by(id=id).first()
        if vocab_word:
            return make_response(vocab_word.to_dict())
        else:
            return make_response({"error": "Vocab word not found"}, 404)

# GET request for all Module Contents
class ModuleContents(Resource):
    def get(self):
        module_contents = [mc.to_dict() for mc in ModuleContent.query.all()]
        return make_response(jsonify(module_contents), 200)

# GET request so User can log in using login credentials
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
    
# PATCH request so User can change login credentials if they want
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        new_username = request.json.get('username')
        new_password = request.json.get('_password_hash')
        current_module_id = request.json.get('current_module_id')
        progress_percentage = request.json.get('progress_percentage')

        if progress_percentage:
            user.progress_percentage = progress_percentage

        if current_module_id:
            user.current_module_id = current_module_id

        if new_username:
            user.username = new_username

        if new_password:
            user.password_hash = new_password

        db.session.commit()
        return make_response(user.to_dict(), 200)
    
# DELETE request so User can delete their profile if they want
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": "User not found"}, 404)
        Favorite.query.filter_by(user_id=user.id).delete()
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 200)

# POST request so logged in User can add Vocab words into their Favorites list
class Favorites(Resource):
    def post(self, user_id):
        data = request.get_json()

        user = User.query.get(user_id)
        vocab = Vocab.query.get(data['vocab_id'])
        if not user or not vocab:
            return make_response({"error": "User or Vocab not found"}, 404)
       
        new_favorite = Favorite(vocab_id=data['vocab_id'], user_id=user_id)
        user.favorites.append(new_favorite)


        db.session.commit()
        return make_response(new_favorite.to_dict(), 200)
    


class FavoriteById(Resource):

    # DELETE request so logged in User can delete Vocab word/ words once they're done reviewing
    def delete(self, id):

        favorite = Favorite.query.filter_by(id=id).first()

        if not favorite:
            return make_response({"error": "Favorite not found"}, 404)
        
        db.session.delete(favorite)
        db.session.commit()

        return make_response({"message": "Favorite removed successfully"}, 200)


class Signup(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        new_user = User(
            username=username
        )

        new_user.password_hash = password

        try:
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return make_response(new_user.to_dict(), 201)

        except Exception as e:
            print(e)
            return make_response({'error': 'Unprocessable Entity'}, 417)

class CheckSession(Resource):

    def get(self):
        user_id = session.get('user_id')
        
        if not user_id:
            return {'error': 'Unauthorized'}, 401
        
        current_user = User.query.filter(User.id == user_id).first()
        return current_user.to_dict(), 200

class Login(Resource):
    
    def post(self):
        data = request.get_json()

        check_user = User.query.filter(User.username == data['username']).first()
        
        if check_user and check_user.authenticate(data['password']):
            session['user_id'] = check_user.id
            return make_response(check_user.to_dict(), 200)
        return {'error': 'Unauthorized'}, 401


class Logout(Resource):

    def delete(self):
        
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204
        return {'error': '401 Unauthorized'}, 401


api.add_resource(Home, '/')
api.add_resource(Vocabs, '/vocab')
api.add_resource(VocabByID, '/vocab/<int:id>')
api.add_resource(ModuleContents, '/module')
api.add_resource(UserByID, '/user/<int:id>')
api.add_resource(Favorites, '/user/<int:user_id>/favorites')
api.add_resource(FavoriteById, '/favorites/<int:id>')
api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
