#!/usr/bin/python3
"""
handles the menu items
"""

from new import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import Length, DataRequired

class Menu(db.Model):
    """ creates menu table """
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    food = db.Column(db.Text(), nullable=False)
    ingredients = db.Column(db.Text(), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    


class MenuForm(FlaskForm):
    """form to get menu data"""
    food = StringField(label='Food Name:', validators=[Length(min=3), DataRequired()])
    ingredients = StringField(label='Ingredients:', validators=[Length(min=3), DataRequired()])
    category = StringField(label='Category:', validators=[DataRequired()])
    price = IntegerField(label='Item Price:', validators=[DataRequired()])
    image = FileField(label='Upload photo:', validators=[DataRequired()])
    submit = SubmitField(label='upload')
