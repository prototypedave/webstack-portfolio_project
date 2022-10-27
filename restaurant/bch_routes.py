#!/usr/bin/python3
""" handles app routes """

from new import app, db
from flask import redirect, flash, url_for, request, render_template
from new.branch import Branch, BranchForm
from flask_login import login_required


@app.route('/branch', methods=['GET', 'POST'])
@login_required
def branch_page():
    """ loads branch """
    branch = Branch.query.all()
    form = BranchForm()
    return render_template('branch.html', branch=branch, form=form)

@app.route("/branch/add", methods=['POST', 'GET'])
def add_branch():
    """ register a branch """
    form = BranchForm()
    if form.validate_on_submit:
        try:
            branch = Branch(
                restaurant_name=form.restaurant_name.data,
                contact1=form.contact1.data,
                contact2=form.contact2.data,
                branch_email=form.branch_email.data,
                location=form.location.data
            )
            db.session.add(branch)
            db.session.commit()
            flash(f"Branch added", category="info")
            return redirect(url_for('branch_page'))
        except:
            flash(f'branch already exists')
    #checks if there is errors in the form data
    if form.errors != {}:
        """ if no errors from validations """
        for err in form.errors.values():
            flash(f"Error creating your account: {err}", category="danger")
    return render_template('branch.html', form=form)


@app.route('/branch/update', methods=['GET', 'POST'])
def update_branch():
    """updates branch table """
    if request.method == 'POST':
        branch = Branch.query.get(request.form.get('id'))
        branch.restaurant_name = request.form.get('restaurant')
        branch.contact1 = request.form.get('contact1')
        branch.contact2 = request.form.get('contact2')
        branch.branch_email = request.form.get('bch-email')
        branch.location = request.form.get('location')
        db.session.commit()
        flash(f'Employee updated Successfully', category="success")
        return redirect(url_for('branch_page'))