#!/usr/bin/python3
"""
contains admin classes
"""

from new import db, bcrypt, login_manager
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError


class Admin(db.Model, UserMixin):
    """ details of the host user to be saved in db """
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=15), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


class RegisterForm(FlaskForm):
    """ handles registration of admin"""
    def validate_username(self, username_to_check):
        """ checks if admin exists in the db """
        admin = Admin.query.filter_by(username=username_to_check.data).first()
        if admin:
            raise ValidationError("Username Already Exists!, Try a New Username")

    def validate_email(self, email_to_check):
        """ checks if email already exists """
        email = Admin.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Email already exists, Have account? Try logging in instead")

    username = StringField(label='Username:', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired("password should match")])
    submit = SubmitField(label='Register')

    


class LoginForm(FlaskForm):
    """contains details for login"""
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")
