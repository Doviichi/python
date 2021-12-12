from flask.app import Flask
from flask.globals import request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import email
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO email (email) VALUES (%(email)s)"
        data = {
            'email': request.form['email']
        }
        results = connectToMySQL('email_schema').query_db(query, data)


    @classmethod
    def all_emails(cls):
        query = "SELECT * FROM email"
        results = connectToMySQL('email_schema').query_db(query)
        return results


    @classmethod
    def last_email():
        query = "SELECT email FROM email where"

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM email WHERE id = %(email)s"
        results = connectToMySQL('email_schema').query_db(query, email)
        if len(results) >= 1:
            flash("Email Already taken.")
            is_valid = False
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            is_valid = False
        return is_valid