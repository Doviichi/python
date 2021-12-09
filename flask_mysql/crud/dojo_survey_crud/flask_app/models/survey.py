from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask
class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO survey (name, location, language, comment) Values (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM survey ORDER BY survey.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return results[0]


    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid + False
            flash("Must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a launguage")
        if len(survey['comment']) < 5:
            is_valid = False
            flash("Must comment.")
        return is_valid



