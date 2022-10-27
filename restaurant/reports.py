#!/usr/bin/python3
"""
handles restaurant reports
"""

from new import db, app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import Length, DataRequired


class Report(db.Model):
    """ CREATES A REPORTS DB TABLE """
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    sales = db.Column(db.Integer(), nullable=False)
    expenses = db.Column(db.Integer(), nullable=False)
    startCash = db.Column(db.Integer(), nullable=False)
    closeCash = db.Column(db.Integer(), nullable=False)
    profit = db.Column(db.Integer(), nullable=False)
    reportDate = db.Column(db.DateTime(), nullable=False)


class ReportForm(FlaskForm):
    """gets reports data """
    sales = IntegerField(label='Enter Todays Sales:', validators=[DataRequired()])
    expenses = IntegerField(label='Enter Todays Expenses:', validators=[DataRequired()])
    startCash = IntegerField(label='Cash in Drawer Before opening:', validators=[DataRequired()])
    reportDate = DateField(label='Report Date:', validators=[DataRequired()])
    closeCash = IntegerField(label='Cash in Drawer after closing:', validators=[DataRequired()])
    submit = SubmitField()


