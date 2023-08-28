#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import User, Trait, TraitAssociation, Goblin, Date, Dialogue, Response, Outcome
# Local imports
from config import app, db, api
# Add your model imports
# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

class Users(Resource):
    
    def get(self):
        users = [user.to_dict(rules=('-traits',)) for user in User.query.all()]
        return make_response(jsonify(users), 200)
    
    def post(self):
        data = request.get_json(force=True)
        try:
            
            new_user = User(**data)
            db.session.add(new_user)
            db.session.commit()
            return make_response(jsonify(new_user.to_dict(rules=('-traits',))), 201)
        
        except ValueError as e:
            return make_response(jsonify({'error': str(e)}), 400)
    
api.add_resource(Users, '/users')        

class UsersById(Resource):
    
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response(jsonify({'error': 'User not found'}), 404)
        return make_response(jsonify(user.to_dict()), 200)
    
    def patch(self, id):
        data = request.get_json(force=True)
        try:
            user = User.query.filter_by(id=data['id']).first()
            for key, value in data.items():
                setattr(user, key, value)
            db.session.commit()
            return make_response(jsonify(user.to_dict(rules=('-traits',))), 200)
        
        except ValueError as e:
            return make_response(jsonify({'error': str(e)}), 400)
        
    def delete(self, id):
        data = request.get_json(force=True)
        try:
            user = User.query.filter_by(id=data['id']).first()
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify(user.to_dict(rules=('-traits',))), 200)
        
        except ValueError as e:
            return make_response(jsonify({'error': str(e)}), 400)
api.add_resource(UsersById, '/users/<int:id>')        

class Traits(Resource):
    
    def get(self):
        traits = [trait.to_dict(rules=('-users', '-dialogues', '-trait_associations')) for trait in Trait.query.all()]
        return make_response(jsonify(traits), 200)
api.add_resource(Traits, '/traits')    
    
class TraitAssociations(Resource):
    def get(self):
        trait_associations = [trait_association.to_dict(rules=('-users', '-traits')) for trait_association in TraitAssociation.query.all()]
        return make_response(jsonify(trait_associations), 200)
    def post(self):
        data = request.get_json(force=True)
        try:
            
            new_trait_association = TraitAssociation(**data)
            db.session.add(new_trait_association)
            db.session.commit()
            return make_response(jsonify(new_trait_association.to_dict(rules=('-users', '-traits'))), 201)
        
        except ValueError as e:
            return make_response(jsonify({'error': str(e)}), 400)
        

class Goblins(Resource):
    
    def get(self):
        goblins = [goblin.to_dict(rules=('-responses', '-outcomes')) for goblin in Goblin.query.all()]
        return make_response(jsonify(goblins), 200)
api.add_resource(Goblins, '/goblins')        

class Dates(Resource):
    
    def get(self):
        dates = [date.to_dict(rules=('-dialogues', '-outcomes')) for date in Date.query.all()]
        return make_response(jsonify(dates), 200) 
api.add_resource(Dates, '/dates')

class Dialogues(Resource):
    def get(self):
        dialogues = [dialogue.to_dict(rules=('-dates', '-traits', '-responses')) for dialogue in Dialogue.query.all()]
        return make_response(jsonify(dialogues), 200)
    
class Responses(Resource):
    def get(self):
        responses = [response.to_dict(rules=('-outcomes',)) for response in Response.query.all()]
        return make_response(jsonify(responses), 200)

class Outcome(Resource):
    def get(self):
        outcomes = [outcome.to_dict(rules=('-responses',)) for outcome in Outcome.query.all()]
        return make_response(jsonify(outcomes), 200)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)

