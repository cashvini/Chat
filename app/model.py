

from app import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin,db.Model):
    
    """Data model for user accounts."""
    
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

   # __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.Text, nullable=True)
    password= db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    def __init__(self, id=None,username=None,email=None,created_date=None,name=None,password=None):
        self.id = id
        self.username = username
        self.email = email
        self.created_date = created_date
        self.name = name
        self.password = password


    
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(140))
    answer = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Chat {}>'.format(self.body)
    
