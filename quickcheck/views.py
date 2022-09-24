from flask import render_template, redirect, request, flash, url_for
from app import app, mongodb
from datetime import datetime
from bson.objectid import ObjectId


@app.route('/quickcheck', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html')
