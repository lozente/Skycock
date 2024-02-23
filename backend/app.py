from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev", SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
)
migrate = Migrate(app, db)
db.init_app(app)
with app.app_context():
    from backend.app.model import *

    db.create_all()
