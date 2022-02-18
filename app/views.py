from flask import render_template, redirect, request, flash, url_for
from app import app, mongodb
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        city = request.form['city']

        # do the logic and save to database

        one = {
            'phone_number': phone_number.lower(),
            'first_name': first_name.lower(),
            'last_name': last_name.lower(),
            'address': address,
            'city': city.lower(),
            'date': datetime.utcnow().isoformat()
        }

        mongodb.db.addressbuk.insert_one(one)

        flash("Record saved successfully", "success")
        return redirect(url_for('index'))
    return render_template('index.html', name='Register', select="index")


@app.route('/edit/<string:id>/', methods=['GET', 'POST'])
def edit(id):
    # mongodb.db.addressbuk.find_one
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']

        # save to database
        flash("Record updated successfully", "success")
        return redirect(url_for('edit'))
    return render_template('edit.html', name='Register')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_by = request.form['search_by']
        search_item = request.form['search_item']

        # query database
        all = mongodb.db.addressbuk.find({'{}'.format(search_by): search_item})

        all_item = list(all)
        return redirect(url_for('search', list=all_item))
        # return render_template('results.html', list=all_item)
    return render_template('search.html', select="search")