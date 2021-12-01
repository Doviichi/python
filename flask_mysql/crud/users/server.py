from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from users import Users


# home page
@app.route('/')
def index():
    users = Users.read_all()
    print(users)
    return render_template('/index.html', users = users)

# create new user
@app.route('/user/create')
def show():
    return render_template('create.html')
# create and procces the new user, redirect to home
@app.route('/add_user', methods=['post'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.add_user(data)
    return redirect('/')

# edit user
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', user=Users.get_one(data))
# process and update user, redirect home
@app.route('/user/update/<int:id>', methods=['post'])
def update(id):
    data = {
        'id':id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.update(data)
    return redirect('/')

# shows individual user
@app.route('/user/show/<int:id>')
def show_user(id):
    data = {
        'id':id
    }
    return render_template('show.html', user=Users.get_one(data))

# delete user *with out warning!* and redirects home
@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Users.delete(data)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)