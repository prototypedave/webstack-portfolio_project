#!/usr/bin/python3
"""
routes for authentication
"""

from new import app, db
from flask import render_template, redirect, url_for, flash
from new.admin import RegisterForm, LoginForm, Admin
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/login', methods=["GET", "POST"])
def login_page():
    """ Handles admin login requests """
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            attempted_user = Admin.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(
                                attempted_password=form.password.data
                                ):
                login_user(attempted_user)
                flash(f'Welcome {attempted_user.username}, do some business!',
                                                    category="success"
                                                     )
                return redirect(url_for('home_page'))
        except:
            flash(f'Login Details dont match, Try again or create a new account',
                                                    category="danger"
                                                    )
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            new_admin = Admin(username=form.username.data,
                          email=form.email.data,
                          password=form.password1.data)
            db.session.add(new_admin)
            db.session.commit()
            flash(f"Admin updated", category="info")
            return redirect(url_for('home_page'))
        except:
            flash(f'username already exists')

    # checks if there is errors in the form data
    if form.errors != {}:
        """ if no errors from validations """
        for err in form.errors.values():
            flash(f"Error creating your account: {err}", category="danger")

    return render_template('register.html', form=form)
   
        
@app.route('/logout')
def logout_page():
    """ logs admin out of the website """
    logout_user()
    flash(f'You are logged out!', category="info")
    return redirect(url_for('login_page'))
    

@app.route('/home')
@login_required
def home_page():
    """ main page website """
    return render_template('home.html')
