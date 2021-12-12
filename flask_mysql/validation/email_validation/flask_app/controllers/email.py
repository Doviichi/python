from flask_app import app
from flask import render_template, redirect, request, session,flash

from flask_app.models.emails import Email

@app.route('/')
def index():
    return redirect('/home')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/save', methods = ['post'])
def save():
    if not Email.is_valid(request.form):
        return redirect('/home')
    Email.save(request.form)
    return redirect('/all_emails')

@app.route('/all_emails')
def all_emails():
    return render_template('all_email.html', emails = Email.all_emails())
