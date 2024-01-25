from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Book:
    db_name = "mvcusersbooks"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.nrOfPages = data['nrOfPages']
        self.price = data['price']
        self.author = data['author']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, description, nrOfPages, price, author, user_id) VALUES (%(title)s, %(description)s, %(nrOfPages)s, %(price)s, %(author)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
     

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db_name).query_db(query)
        books = []
        if results:
            for book in results:
                books.append(book)
        return books

    @classmethod
    def get_book_by_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN users on books.user_id = users.id WHERE books.id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM books where id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE books set description = %(description)s, price=%(price)s, nrOfPages = %(nrOfPages)s WHERE books.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['title'])< 2:
            flash('Title should be more  or equal to 2 characters', 'title')
            is_valid = False
        if len(book['description'])< 10:
            flash('Description should be more  or equal to 10 characters', 'description')
            is_valid = False
        if len(book['nrOfPages'])< 1:
            flash('Number of pages is required', 'nrOfPages')
            is_valid = False
        if len(book['price'])< 1:
            flash('Price is required', 'price')
            is_valid = False
        if len(book['author'])< 2:
            flash('Author name should be more  or equal to 2 characters', 'author')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_bookUpdate(book):
        is_valid = True
        if len(book['description'])< 10:
            flash('Description should be more  or equal to 10 characters', 'description')
            is_valid = False
        if len(book['nrOfPages'])< 1:
            flash('Number of pages is required', 'nrOfPages')
            is_valid = False
        if len(book['price'])< 1:
            flash('Price is required', 'price')
            is_valid = False
        return is_valid