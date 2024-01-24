from flask_app.config.mysqlconnection import connectToMySQL

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

    

        
