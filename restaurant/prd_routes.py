#!/usr/bin/python3
""" handles app routes """

from fileinput import filename
import os
from new import app, db
from flask import redirect, flash, url_for, request, render_template, Response
from new.product import Menu, MenuForm
from flask_login import login_required



@app.route('/menu', methods=['GET', 'POST'])
@login_required
def product_page():
    """ loads menu """
    menu = Menu.query.all()
    form = MenuForm()
    return render_template('product.html', menu=menu, form=form)


def save_image(photo):
    image = photo.filename
    img_path = os.path.join(app.root_path,'static/menu_pics', image)
    photo.save(img_path)
    return image


@app.route('/menu/add_menu', methods=['POST', 'GET'])
def add_menu():
    """ adds a new item """
    form = MenuForm()
    if form.validate_on_submit():
        item = Menu(food=form.food.data,
                    ingredients = form.ingredients.data,
                    category = form.category.data,
                    price = form.price.data,
                    image = save_image(form.image.data)   
                )
        db.session.add(item)
        db.session.commit()
        flash(f'{item.food} added succefully')
        return redirect(url_for('product_page'))


@app.route('/menu/update', methods=['POST', 'GET'])
def menu_update():
    """updates branch table """
    if request.method == 'POST':
        menu = Menu.query.get(request.form.get('id'))
        menu.food = request.form.get('efood')
        menu.ingredients = request.form.get('ingredients')
        menu.category = request.form.get('ecategory')
        menu.price = request.form.get('price')
        image = request.form.get('pic')
        image_url = url_for('static', filename='menu_pics/{menu.image}')
        if image != image_url:
            menu.image = save_image(image)
        else:
            menu.image = image
        db.session.commit()
        flash(f'Food updated Successfully', category="success")
        return redirect(url_for('product_page'))


@app.route('/menu/delete', methods=['GET', 'POST'])
def remove_food():
    """ deletes a record from db """
    if request.method == 'POST':
        if request.form.get('delete'):
            del_food = Menu.query.filter_by(id=request.form['delete']).first()
            db.session.delete(del_food)
            flash(f'Food removed', category="danger")
            db.session.commit()
            return redirect(url_for('product_page'))