import os
from flask import Flask
from flask_pymongo import PyMongo
import urllib.parse

app = Flask(__name__)

username = urllib.parse.quote_plus(str(os.environ.get('MONGO_USER')))
password = urllib.parse.quote_plus(str(os.environ.get('MONGO_PASS')))
MONGO_URI = 'mongodb+srv://{}:{}@cluster0.of0j7.azure.mongodb.net/searchbuk?retryWrites=true&w=majority'.format(username, password)
mongodb = PyMongo(app, MONGO_URI)

app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['DEBUG'] = False

from app import views