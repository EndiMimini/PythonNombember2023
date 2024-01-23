from flask_app.config.mysqlconnection import connectToMySQL

class Post:
    db_name = "usersdatabasepython"
    def __init__(self, data):
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, content) VALUES (%(title)s, %(content)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.db_name).query_db(query)
        posts = []
        if results:
            for post in results:
                posts.append(post)
        return posts

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)