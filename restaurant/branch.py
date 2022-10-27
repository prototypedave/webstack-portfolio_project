#!/usr/bin/python3
"""
handles all the branch related details
"""
from new import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, Email


class Branch(db.Model):
    """ creates branch table in db"""
    id = db.Column(db.Integer(), primary_key=True)
    restaurant_name = db.Column(db.String(length=30), nullable=False)
    contact1 = db.Column(db.String(length=12), nullable=False, unique=True)
    contact2 = db.Column(db.String(length=12), nullable=True)
    branch_email = db.Column(db.Integer(), nullable=False, unique=True)
    location = db.Column(db.String(length=3), nullable=False)

    def __init__(self, restaurant_name, contact1, contact2, branch_email, location) -> None:
        self.restaurant_name = restaurant_name
        self.mobile = contact1
        self.contact2 = contact2
        self.branch_email = branch_email
        self.location = location


    def __repr__(self) -> str:
        """ returns a string from db"""
        return f'Branch{self.restaurant_name}'


class BranchForm(FlaskForm):
    """ html inputs """
    restaurant_name = StringField(label='Restaurant:', validators=[Length(min=3), DataRequired()])
    contact1 = StringField(label='Mobile Number:', validators=[Length(min=8, max=12), DataRequired()])
    contact2 = StringField(label='Mobile Number2:', validators=[Length(min=8, max=12)])
    branch_email = StringField(label='Email:', validators=[DataRequired(), Email()])
    location = StringField(label='Location:', validators=[DataRequired()])
    submit = SubmitField()
