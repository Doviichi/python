from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.logins import User
from flask_app.models.recipes import Recipes
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    fname = request.form['first_name'].capitalize()
    lname = request.form['last_name'].capitalize()
    data = {
        'fname': fname,
        'lname': lname,
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login', methods = ['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email Not Recognized", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user = User.get_by_id(info), recipes = Recipes.get_all(info))


@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')