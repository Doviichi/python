from re import U
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipes import Recipes
from flask_app.models.logins import User


@app.route('/add_recipe/recipe')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': session['user_id']
    }
    return render_template('create.html', user = User.get_by_id(info))

@app.route('/create/recipe', methods = ['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipes.validate_recipe(request.form):
        return redirect('/add_recipe/recipe')
    name = request.form['name'].capitalize()
    desc = request.form['description'].capitalize()
    inst = request.form['instructions'].capitalize()
    info = {
        "name": name,
        "description": desc,
        "instructions": inst,
        "under30": (request.form["under30"]),
        # "date_made": request.form['date_made'],
        "user_id": session["user_id"]
    }
    Recipes.save(info)
    return redirect('/dashboard')

@app.route('/view/recipe/<int:id>')
def veiw(id):
    info = {
        'id': id
    }
    user_id = {
        'id': session['user_id'] 
    }
    return render_template('view.html', recipes = Recipes.veiw(info), user = User.get_by_id(user_id))

@app.route('/edit/recipe/<int:id>')
def edit(id):
    info = {
        'id': id
    }
    user_id = {
        'id': session['user_id']
    }
    return render_template('edit.html', recipe = Recipes.veiw(info), user = User.get_by_id(user_id))

@app.route('/update/recipe/<int:id>', methods = ['post'])
def update(id):
    name = request.form['name'].capitalize()
    desc = request.form['description'].capitalize()
    inst = request.form['instructions'].capitalize()
    # under30 = request.form['under30']
    info = {
        "id": id,
        'name': name,
        'description': desc,
        'instructions': inst,
        # 'under30': under30
    }
    if not Recipes.validate_recipe(info):
        return redirect('/dashboard')
    # print("PRINTING",info['id'])
    Recipes.update(info)
    return redirect('/dashboard')


@app.route('/delete/recipe/<int:id>')
def delete(id):
    info = {
        'id': id
    }
    Recipes.delete(info)
    return redirect('/dashboard')