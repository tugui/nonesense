from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask import Blueprint

db_bp = Blueprint('db_bp', __name__)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)


# Initialize app with extension
db.init_app(db_bp)
# Create database within app context

with db_bp.app_context():
    db.create_all()