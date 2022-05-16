from tokenize import String
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .home import home as home_blueprint
from .login import login as login_blueprint 

#app config

app=Flask(__name__)
app.secret_key = "aksnd1#kj$%"
app.config.from_object(Config)

#database config

db= SQLAlchemy(app)
migrate=Migrate(app, db)

#database models

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64))
    email=db.Column(db.String(120))
    pass_hash=db.Column(db.String(128))

class Assets(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    asset_name=db.Column(db.String(64))
    location=db.Column(db.String(120))
    updated=db.Column(db.String(128))

def create_app():
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    return app