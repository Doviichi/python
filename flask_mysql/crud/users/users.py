from mysqlconnection import MySQLConnection, connectToMySQL
from datetime import datetime

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('new_users_schema').query_db(query)
        users = []
        
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        results = connectToMySQL('new_users_schema').query_db(query, data)
        return results


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('new_users_schema').query_db(query, data)
        return (cls(results[0]))

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at =NOW() WHERE id = %(id)s"
        results = connectToMySQL('new_users_schema').query_db(query, data)
        
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        results = connectToMySQL('new_users_schema').query_db(query, data)
        return results

