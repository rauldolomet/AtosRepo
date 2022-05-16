from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
from .config import Config
from .home import home as home_blueprint

app=Flask(__name__)
app.secret_key = "aksnd1#kj$%"
app.config.from_object(Config)

def create_app():
    app.register_blueprint(home_blueprint)
    return app