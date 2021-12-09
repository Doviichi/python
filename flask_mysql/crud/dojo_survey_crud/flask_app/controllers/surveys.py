from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/show')
    return redirect('/')
    # session['form'] = request.form
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['comments'] = request.form['comments']
    # print (session['form'])

@app.route('/show')
def show():
    return render_template('show.html', Survey = Survey.get_last_survey())