from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipes:
    db = "recipes_schema"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.under30 = db_data['under30']
        self.date_made = db_data['date_made']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']



    @classmethod
    def save(cls, info):
        query = "INSERT INTO recipes (name, description, instructions, under30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under30)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, info)

    @staticmethod
    def validate_recipe(form_info):
        is_valid = True
        if len(form_info['name']) <3:
            flash("Name Too Short")
            is_valid = False
        if len(form_info['description']) <5:
            flash("Description Too Short, Describe a bit more.")
            is_valid =False
        if len(form_info['instructions']) <5:
            flash("Instruction is Too Short, Explain Better!")
            is_valid = False
        # if len(form_info['under30']) == 0:
        #     flash("chose option")
        #     is_valid = False
        return is_valid

    @classmethod
    def get_all(cls, info):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE user_id = %(id)s;"
        results =  connectToMySQL(cls.db).query_db(query, info)
        return results

    @classmethod
    def veiw(cls, info):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, info)

    @classmethod
    def update(cls, info):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under30 = %(under30)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, info)


    @classmethod
    def delete(cls, info):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, info)
