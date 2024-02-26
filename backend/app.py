from flask import Flask
from flask_migrate import Migrate

from apps.model.db import db

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev", SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
)
migrate = Migrate(app, db)
db.init_app(app)
with app.app_context():
    from apps.model.DTO.match import MatchDTO

    db.create_all()
