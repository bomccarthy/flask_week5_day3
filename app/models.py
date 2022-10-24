from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_dict = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, pokemon_dict, user_id, date_created):
        self.pokemon_dict = pokemon_dict
        self.user_id = user_id
        self.date_created = date_created

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()    

# class Pokemon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), nullable=False)
#     ability = db.Column(db.String)
#     base_experience = db.Column(db.String)
#     official_artwork = db.Column(db.String)
#     hp = db.Column(db.String)
#     attack = db.Column(db.String)
#     defense = db.Column(db.String)
#     special_attack = db.Column(db.String)
#     special_defense = db.Column(db.String)
#     speed = db.Column(db.String)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, name, ability, base_experience, official_artwork, hp, attack, defense, special_attack, special_defense, speed, date_created, user_id):
#         self.name = name
#         self.ability = ability
#         self.base_experience = base_experience
#         self.official_artwork = official_artwork
#         self.hp = hp
#         self.attack = attack
#         self.defense = defense
#         self.special_attack = special_attack
#         self.special_defense = special_defense
#         self.speed = speed
#         self.date_created = date_created
#         self.user_id = user_id

#     def saveToDB(self):
#         db.session.add(self)
#         db.session.commit()        