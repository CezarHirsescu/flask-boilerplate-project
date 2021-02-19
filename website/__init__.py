from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")

def create_app():
    app = Flask(__name__)
    # generate secret key at: https://www.allkeysgenerator.com/Random/Security-Encryption-Key-Generator.aspx
    app.config["SECRET_KEY"] = ""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Once you have created ur models, type this line of code
    # from .models import Model1, Model2, ... etc

    create_database(app)

    return app
