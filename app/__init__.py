from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = "dracubeo123"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://toan1:Dr@cubeo123@localhost/Library_db?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)

admin = Admin(app=app, name="", template_mode="bootstrap4")

login = LoginManager(app=app)

