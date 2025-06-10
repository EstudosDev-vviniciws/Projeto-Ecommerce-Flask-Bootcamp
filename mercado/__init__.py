from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '14e213928bbca654b936b462'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)

from mercado import routes