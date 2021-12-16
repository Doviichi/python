from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash, session

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name  = data['first_name']
        self.last_name  = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # TRY TO MAKE LOGOUT CLASS!
    # def logout():
    #     id = session['user_id']
    # if 'user_id' not in session:


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_register(form_info):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query, form_info)
        if len(results) >= 1:
            flash("Email already taken","register")
            is_valid = False
        if not email_regex.match(form_info['email']):
            flash("Invalid Email","register")
            is_valid = False
        if len(form_info['first_name']) <3:
            flash("First Name must be longer.","register")
            is_valid = False
        if len(form_info['last_name']) <3:
            flash("Last Name must be longer.","register")
            is_valid = False
        if len(form_info['password']) < 8:
            flash("password must be 8 characters long!","register")
            is_valid = False
        if form_info['password'] != form_info['confirm']:
            flash("Passwords Dont Match!","register")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_id(cls, info):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, info)
        return cls(results[0])

    @classmethod
    def get_by_email(cls, form_info):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, form_info)
        return cls(results[0])

