#!/usr/bin/python3
""" makes exporting app instace easier """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'e9f8605dd6c10b34f18f748e'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'login_page'

from new import emp_routes, admin_routes, bch_routes, repo_routes, prd_routes