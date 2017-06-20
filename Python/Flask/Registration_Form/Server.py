from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime, date, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
def validate():
    errors = 0
    #Check first name
    if len(request.form['FirstName']) < 1:
        flash('Name cannot be blank', 'FirstNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['FirstName']) == True:
        flash('Name cannot have numbers', 'FirstNameError')
        errors += 1
        pass
    else:
        session['FirstName'] = request.form['FirstName']
    #Check last name
    if len(request.form['LastName']) < 1:
        flash('Name cannot be blank', 'LastNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['LastName']) == True:
        flash('Name cannot have numbers', 'LastNameError')
        errors += 1
        pass
    else:
        session['LastName'] = request.form['LastName']
    #Check birthdate
    if request.form['Birthdate'] == '':
        flash('Please pick a birthday', 'DateError')
        errors += 1
        pass

    else:
        session['Birthdate'] = request.form['Birthdate']
        now = datetime.now()
        birthDate = datetime.strptime(session['Birthdate'], "%Y-%m-%d")

        if now > birthDate:
            pass
        else:
            errors += 1
            flash('Birthdate must be in the past', 'dateError')
    #Check email
    if len(request.form['Email']) < 1:
        flash('Email cannot be blank', 'EmailError')
        errors += 1
        pass
    elif not EMAIL_REGEX.match(request.form['Email']):
        flash('Invalid Email address', 'EmailError')
        errors += 1
        pass
    else:
        session['Email'] = request.form['Email']
    #Check password
    if len(request.form['Password']) < 1:
        flash('Password cannot be blank', 'PasswordError')
        errors += 1
        pass
    elif len(request.form['Password']) < 8:
        flash('Password must be greater than 8 characters', 'PasswordError')
        errors += 1
        pass
    elif not PASSWORD_REGEX.match(request.form['Password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'PasswordError')
    else:
        session['Password'] = request.form['Password']
    #Check confirmation password
    if len(request.form['ConfirmPassword']) < 1:
        flash('Please confirm password', 'ConfirmPasswordError')
        errors += 1
        pass
    elif request.form['ConfirmPassword'] != request.form['Password']:
        flash('Passwords do not match', 'ConfirmPasswordError')
        errors += 1
    else:
        session['ConfirmPassword'] = request.form['ConfirmPassword']
    #See if there are any errors
    if errors > 0:
        session['Password'] = ''
        session['ConfirmPassword'] = ''
        return False
    else:
        return True
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    if session['FirstName'] == None:
        session['FirstName'] = ''
    if session['LastName'] == None:
        session['LastName'] = ''
    if session['Birthdate'] == None:
        session['Birthdate'] = ''
    if session['Email'] == None:
        session['Email'] = ''
    if session['Password'] == None:
        session['Password'] = ''
    if session['ConfirmPassword'] == None:
        session['ConfirmPassword'] = ''
    if validate() == False:
        return redirect('/')
    return redirect('/show')
@app.route('/show')
def show_user():
    
    return render_template('results.html')
@app.route('/clear', methods=['POST'])
def clear():
    session['FirstName'] = ''
    session['LastName'] = ''
    session['Birthdate'] = ''
    session['Email'] = ''
    session['Password'] = ''
    session['ConfirmPassword'] = ''
    return redirect('/')
app.run(debug=True)
