from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from users import Users

@app.route('/')
def index():
    users = Users.read_all()
    print(users)
    return render_template('/index.html', users = users)

@app.route('/create')
def show():
    return render_template('create.html')

@app.route('/add_user', methods=['post'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.add_user(data)
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)