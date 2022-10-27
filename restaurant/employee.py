#!/usr/bin/python3
"""
Employee class & form
"""

from new import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired


class EmployeeForm(FlaskForm):
    """ handles registration of new employee """
    name = StringField(label='Name:', validators=[Length(min=3), DataRequired()])
    mobile = StringField(label='Mobile Number:', validators=[Length(min=3), DataRequired()])
    age = StringField(label='Age:', validators=[DataRequired()])
    gender = StringField(label='Gender:', validators=[DataRequired()])
    salary = IntegerField(label='Monthly Salary:', validators=[DataRequired()])
    role = StringField(label='Employee Job Role:', validators=[Length(min=3, max=12), DataRequired()])
    submit = SubmitField(label='Add Employee')


class EmployeeUpdateForm(FlaskForm):
    """ takes in only a selected record items from the employee to update"""
    name = StringField(label='Name:', validators=[Length(min=3), DataRequired()])
    mobile = StringField(label='Mobile Number:', validators=[Length(min=3), DataRequired()])
    age = StringField(label='Age:', validators=[DataRequired()])
    salary = IntegerField(label='Monthly Salary:', validators=[DataRequired()])
    role = StringField(label='Employee Job Role:', validators=[Length(min=3, max=12), DataRequired()])
    submit = SubmitField(label='update')
    

class Employee(db.Model):
    """ handles db storage of employee table"""
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    mobile = db.Column(db.String(length=12), nullable=False, unique=True)
    salary = db.Column(db.Integer(), nullable=False)
    age = db.Column(db.String(length=3), nullable=False)
    gender= db.Column(db.String(length=1), nullable=False)
    role = db.Column(db.String(length=15), nullable=False)

    def __init__(self, name, mobile, salary, age, gender, role) -> None:
        self.name = name
        self.mobile = mobile
        self.salary = salary
        self.age = age
        self.gender = gender
        self.role = role


    def __repr__(self) -> str:
        """ returns a string from db"""
        return f'Employee{self.name}'
