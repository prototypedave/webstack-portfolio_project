#!/usr/bin/python3
""" handles app routes """

from datetime import datetime, timedelta, date
from new import app, db
from flask import redirect, flash, url_for, request, render_template
from new.reports import Report, ReportForm
from flask_login import login_required
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import io
import base64


@app.route('/report', methods=['GET', 'POST'])
@login_required
def report_page():
    """ renders web page for employees """
    report = Report.query.all()
    form = ReportForm()
    det = date.today()
    id = Report.query.filter_by(reportDate = det).first()
    return render_template('reports.html', report=report, id=id, form=form)


@app.route('/report/add', methods=["POST", "GET"])
def add_report():
    """ generates report of a given day """
    form = ReportForm()
    if form.validate_on_submit():
        report = Report(
            sales=form.sales.data,
            expenses=form.expenses.data,
            startCash=form.startCash.data,
            closeCash=form.sales.data + form.startCash.data - form.expenses.data,
            profit=form.sales.data + form.startCash.data - form.expenses.data,
            reportDate=form.reportDate.data
        )
        db.session.add(report)
        db.session.commit()
        flash(f'report saved' , category="success")
        return redirect(url_for('report_page'))
        
        
@app.route('/report/today', methods=['GET', 'POST'])
def daily():
    """ gets report for the day """
    if request.method == 'POST':
        try:
            daily = Report.query.filter_by(reportDate = datetime.today()).first()
            labels = ['sales', 'expenses']
            sales = daily.sales
            expenses = daily.expenses
            plt.pie([sales, expenses], labels = labels, )
            canvas = FigureCanvas(fig)
            img=io.BytesIO()
            fig.savefig(img)
            img.seek(0)
            return send_file(img,mimetype='img/png')

        except:
            flash(f'You need to input todays data first')
            return redirect(url_for('add_report'))
    if request.method == 'GET':
        return render_template('report.html', daily=daily)


@app.route('/report/anyday', methods=['GET', 'POST'])
def given_day():
    """ gets report for the day """
    if request.method == 'POST':
        d = request.form('date')
        try:
            daily = Report.query.filter_by(reportDate = d).first()
            return daily
        except:
            flash(f'No data found, try another date')
            return redirect(url_for('add_report'))
    if request.method == 'GET':
        return render_template('report.html', daily=daily)


@app.route('/report/weekly', methods=['GET', 'POST'])
def weekly():
    """ gets report for the day """
    if request.method == 'POST':
        d = datetime.today() - timedelta(days=7)


    if request.method == 'GET':
        return render_template('report.html', daily=daily)


@app.route('/report/monthly', methods=['GET', 'POST'])
def monthly():
    """ gets report for the day """
    if request.method == 'POST':
        try:
            daily = Report.query.filter_by(reportDate = datetime.today()).first()
            return daily
        except:
            flash(f'You need to input todays data first')
            return redirect(url_for('add_report'))
    if request.method == 'GET':
        return render_template('report.html', daily=daily)            


@app.route('/report/anually', methods=['GET', 'POST'])
def anually():
    """ gets report for the day """
    if request.method == 'POST':
        try:
            daily = Report.query.filter_by(reportDate = datetime.today()).first()
            return daily
        except:
            flash(f'You need to input todays data first')
            return redirect(url_for('add_report'))
    if request.method == 'GET':
        return render_template('report.html', daily=daily)




