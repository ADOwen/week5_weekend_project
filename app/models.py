from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
# create models based off of ERD (Database Tables)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    character = db.relationship('MarvelCharacter',backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    image = db.Column(db.String(300))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, image, content, user_id):
        self.title = title
        self.image = image
        self.content = content
        self.user_id = user_id        

class MarvelCharacter(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.String(300))
    comics_appeared_in = db.Column(db.Integer())
    super_power = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, description, comics_appeared_in, super_power,owner):
        self.name = name
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.super_power = super_power
        self.owner = owner

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'comics_appeared_in' : self.comics_appeared_in,
            'super_power' : self.super_power,
            'date_created' : self.date_created,
            'owner' : self.owner,

        }







