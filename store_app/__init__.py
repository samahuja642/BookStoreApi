from flask import Flask
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)

db_url =  f'mongodb+srv://samahuja642:{os.environ.get("mongo_pass")}@cluster0.8thvoo1.mongodb.net/?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = os.environ.get('sec_key')
# app.config['MONGODB_HOST'] = db_url
app.config['MONGODB_SETTINGS'] = {
    'db' : 'book_store',
    'host' : db_url
}

db = MongoEngine()
db.init_app(app)

from store_app import routes
