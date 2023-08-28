#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Trait, TraitAssociation, Goblin, Date, Dialogue, Response, Outcome

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        User.query.delete()
        Trait.query.delete()
        TraitAssociation.query.delete()
        Goblin.query.delete()
        Date.query.delete()
        Dialogue.query.delete()
        Response.query.delete()
        Outcome.query.delete()
        db.session.commit()
        print("deleted all data")
        
        print("Creating users...")
        user1 = User(username="user1", password="Password#1", email="grantbruemmer@gmail.com")
        user2 = User(username="user2", password="Password#2", email="fakeuser@gmail.com")
        user3 = User(username="user3", password="Password#3", email="fakeuser2@gmail.com")
        users = [user1, user2, user3]
        db.session.add_all(users)
        db.session.commit()
        
        print("Creating traits...")
        trait1 = Trait(name="trait1")
        trait2 = Trait(name="trait2")
        trait3 = Trait(name="trait3")
        
        traits = [trait1, trait2, trait3]
        db.session.add_all(traits)
        db.session.commit()
        
        print("Creating trait associations...")
        trait_association1 = TraitAssociation(trait_id=trait1.id, user_id=user1.id)
        trait_association2 = TraitAssociation(trait_id=trait2.id, user_id=user2.id)
        trait_association3 = TraitAssociation(trait_id=trait3.id, user_id=user3.id)
        trait_associations = [trait_association1, trait_association2, trait_association3]
        db.session.add_all(trait_associations)
        db.session.commit()
        
        print("Creating goblins...")
        
        grubnub = Goblin(name="Grubnub", description="Grubnub is a goblin that is very powerful and powerful and power")
        sneezle = Goblin(name="Sneezle", description="Sneezle is a goblin that can't stop snow.")
        blort = Goblin(name="Blort", description="Blort is a goblin that wants to blort out the sun.")
        grimble = Goblin(name="Grimble", description="Grimble is a goblin that is very powerful and powerful and powerful and powerful and powerful and powerful and.")
        zongos = Goblin(name="Zongos", description="Zongos is a goblin that is very powerful and powerful and powerful and powerful and powerful and powerful and.")
        
        goblins = [grubnub, sneezle, blort, grimble, zongos]
        db.session.add_all(goblins)
        db.session.commit()
        
        print("Creating dates...")
        
        date1 = Date(name="date1", description="date1")
        date2 = Date(name="date2", description="date2")
        date3 = Date(name="date3", description="date3")
        
        dates = [date1, date2, date3]
        db.session.add_all(dates)
        db.session.commit()
        
        print("Creating dialogues...")
        dialogue1 = Dialogue(date_part= 1, date_id=date1.id, trait_id=trait1.id, description="Test1")
        dialogue2 =Dialogue(date_part= 2, date_id=date2.id, trait_id=trait2.id, description="Test2")
        dialogue3 =Dialogue(date_part= 3, date_id=date3.id, trait_id=trait3.id, description="Test3")
        
        dialogues = [dialogue1, dialogue2, dialogue3]
        db.session.add_all(dialogues)
        db.session.commit()
        
        print("Creating responses...")
        response1 = Response(dialogue_id=dialogue1.id, goblin_id=grubnub.id, response="Test_Response_1", outcome=True)
        response2 = Response(dialogue_id=dialogue2.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response3 = Response(dialogue_id=dialogue3.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        
        responses = [response1, response2, response3]
        db.session.add_all(responses)
        db.session.commit()
        
        print("Creating outcomes...")
        outcome1 = Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_1")
        outcome2 = Outcome(date_id = date2.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_2")
        outcome3 = Outcome(date_id = date3.id, goblin_id=blort.id, outcome_description="Test_Outcome_3")
        
        outcomes = [outcome1, outcome2, outcome3]
        db.session.add_all(outcomes)
        db.session.commit()
        
        
        
        
        
        
        