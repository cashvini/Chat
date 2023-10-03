import os

from sqlalchemy import MetaData, create_engine
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "SECRET_KEY"
    #FLASK_APP = "FLASK_APP"
   #FLASK_ENV = ("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///chat.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # sql_engine = create_engine(SQLALCHEMY_DATABASE_URI)
    # sql_meta = MetaData(sql_engine)