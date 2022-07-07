from store_app import db,app

class Book(db.Document):
    book_id = db.IntField(required=True,unique=True)  
    name = db.StringField(required=True)
    author = db.StringField()
    link = db.StringField(required=True)
