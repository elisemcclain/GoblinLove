from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from validate_email import validate_email  
import re
from datetime import datetime
from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    grubnub_win = db.Column(db.Integer, nullable=False, default=0)
    sneezle_win = db.Column(db.Integer, nullable=False, default=0)
    blort_win = db.Column(db.Integer, nullable=False, default=0)
    grimble_win = db.Column(db.Integer, nullable=False, default=0)
    zongos_win = db.Column(db.Integer, nullable=False, default=0)
    
    personality_traits = db.relationship('TraitAssociation', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    serialize_rules = ('-personality_traits.user', '-traits.user')
    
    @validates('username')
    def validate_username(self, key, username):
        if User.query.filter_by(username=username).first():
            raise ValueError('That username is taken.')
        return username
    
    @validates('password')
    def validate_password(self, key, password):
        length_test = len(password) >= 8
        uppercase_test = re.search(r'[A-Z]', password) is not None
        lowercase_test = re.search(r'[a-z]', password) is not None
        digit_test = re.search(r'[0-9]', password) is not None
        special_test = re.search(r'[!@#$%^&*()\-_=+{}[\]|\\:;"\'<>,.?/~]', password) is not None
        if length_test and uppercase_test and lowercase_test and digit_test and special_test:
            return password
        else:
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.')
        
    # @validates('email')
    # def validate_email(self, key, email):
    #     if User.query.filter_by(email=email).first():
    #         raise ValueError('That email is taken.')
    #     if validate_email(email):
    #         return email
    #     else:
    #         raise ValueError('Please enter a valid email address.')
        
        
class Trait(db.Model, SerializerMixin):

    __tablename__ = 'traits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    users = db.relationship('TraitAssociation', backref='trait', lazy='dynamic', cascade='all, delete-orphan')
    dialogues = db.relationship('Dialogue', backref='trait', lazy='dynamic', cascade='all, delete-orphan')


    serialize_rules = ('-users', '-dialogues',)

class TraitAssociation(db.Model, SerializerMixin):
    
    __tablename__ = 'trait_associations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    trait_id = db.Column(db.Integer, db.ForeignKey('traits.id'), nullable=False)
    
    serialize_rules = ('-trait.trait_associations', '-user.trait_associations',)
    
class Goblin(db.Model, SerializerMixin):
    
    __tablename__ = 'goblins'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    responses = db.relationship('Response', backref='goblin', lazy='dynamic', cascade='all, delete-orphan')
    outcomes = db.relationship('Outcome', backref='goblin', lazy='dynamic', cascade='all, delete-orphan')
    
    serialize_rules = ('-responses', '-outcomes.goblins',)
    
class Date(db.Model, SerializerMixin):
    
    __tablename__ = 'dates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    dialogues = db.relationship('Dialogue', backref='date', lazy='dynamic', cascade='all, delete-orphan')
    outcomes = db.relationship('Outcome', backref='date', lazy='dynamic', cascade='all, delete-orphan')
    
    serialize_rules = ('-dialogue.dates',)
    
class Dialogue(db.Model, SerializerMixin):
    
    __tablename__ = 'dialogues'
    
    id = db.Column(db.Integer, primary_key=True)
    date_part = db.Column(db.Integer, nullable=False, default=1)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'), nullable=False)
    trait_id = db.Column(db.Integer, db.ForeignKey('traits.id'), nullable=False)
    description = db.Column(db.String, nullable=False)
    
    responses = db.relationship('Response', backref='dialogue', lazy='dynamic', cascade='all, delete-orphan')
    
    serialize_rules = ('description',)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date_part': self.date_part,
            'date_id': self.date_id,
            'trait_id': self.trait_id,
            'description': self.description,
        }
    
class Response(db.Model, SerializerMixin):
    
    __tablename__ = 'responses'
    
    id = db.Column(db.Integer, primary_key=True)
    dialogue_id = db.Column(db.Integer, db.ForeignKey('dialogues.id'), nullable=False)
    goblin_id = db.Column(db.Integer, db.ForeignKey('goblins.id'), nullable=False)
    response = db.Column(db.String, nullable=False)
    outcome = db.Column(db.Boolean, nullable=False, default=False)
    
    serialize_rules = ('-goblin', '-dialogue',)
    
class Outcome(db.Model, SerializerMixin):
    
    __tablename__ = 'outcomes'
    
    id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'), nullable=False)
    goblin_id = db.Column(db.Integer, db.ForeignKey('goblins.id'), nullable=False)
    outcome_description = db.Column(db.String, nullable=False)
    
    # serialize_rules = ('-goblin.outcomes', '-date.outcomes',)
    
    
    