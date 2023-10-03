from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user


app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app import home,model,chat


with app.app_context():
    # Here you can access the Flask application and its components
    db.create_all()