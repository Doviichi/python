from flask import Flask 

from flask_app import app

from flask_app.controllers import login, recipe

if __name__ == "__main__":
    app.run(debug=True)