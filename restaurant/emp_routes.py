#!/usr/bin/python3
""" handles app routes """

from new import app, db
from flask import redirect, flash, url_for, request, render_template
from new.employee import Employee, EmployeeForm, EmployeeUpdateForm
from flask_login import login_required


@app.route('/employees', methods=['GET', 'POST'])
@login_required
def employees_page():
    """ renders web page for employees """
    employees = Employee.query.all()
    form1 = EmployeeForm(request.form)
    form2 = EmployeeUpdateForm()
    
    return render_template('employees.html', employees=employees, form1=form1, form2=form2)


@app.route('/newEmployee', methods=["POST"])
def new_employee():
    """ adds an employee to database """

    if request.method == 'POST':
        new_employee = Employee(name=request.form['name'],
                              mobile=request.form['mobile'],
                              age=request.form['age'],
                              gender=request.form['gender'],
                              salary=request.form['salary'],
                              role=request.form['role'])
        db.session.add(new_employee)
        db.session.commit()
        flash(f"New staff added", category="info")
        return redirect(url_for('employees_page'))
    

@app.route('/updateEmployee', methods=['GET', 'POST'])
def update_existing_employee():
    """ updates employee data """
    if request.method == 'POST':
        staff = Employee.query.get(request.form.get('id'))
        staff.name = request.form.get('name')
        staff.mobile = request.form.get('mobile')
        staff.age = request.form.get('age')
        staff.gender = request.form.get('gender')
        staff.salary = request.form.get('salary')
        staff.role = request.form.get('role')
        db.session.commit()
        flash(f'Employee updated Successfully', category="success")
        return redirect(url_for('employees_page'))

            
            


@app.route('/deleteEmployee', methods=['GET', 'POST'])
def delete_employee():
    """ removes an employees from db """
    if request.method == 'POST':
        if request.form.get('delete'):
            del_employee = Employee.query.filter_by(id=request.form['delete']).first()
            db.session.delete(del_employee)
            flash(f'Employee deleted', category="danger")
            db.session.commit()
            return redirect(url_for('employees_page'))





