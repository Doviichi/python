
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash


email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "login_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)


    @staticmethod
    def validate_register(User):
        is_valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL('login_schema').query_db(query, User)
        if len(results) >= 1:
            flash("Email already taken","register")
            is_valid = False
        if not email_regex.match(User['email']):
            flash("Invalid Email","register")
            is_valid = False
        if len(User['first_name']) <3:
            flash("First Name must be longer.","register")
            is_valid = False
        if len(User['last_name']) <3:
            flash("Last Name must be longer.","register")
            is_valid = False

            # check how to require numbers and caps
        if len(User['password']) < 8:
            flash("password must be 8 characters long!","register")
            is_valid = False

            # what is User['confirm']?
        if User['password'] != User['confirm']:
            flash("Passwords Dont Match!","register")
            is_valid = False
        return is_valid


    @classmethod
    def get_by_email(cls,data):
        # WHERE IS %(email)s GETTING ITS DATA FROM?
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
            # dont understand return syntax (what is cls, and why is there a list of 0?), what is it returning?
        return cls(results[0])


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        # ERROR: indexError: tuple index out of range, but still gets added to db
        print ("PRINTING", results)
        return cls(results[0])
