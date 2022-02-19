from flask import render_template, redirect, request, flash, url_for
from app import app, mongodb
from datetime import datetime
from bson.objectid import ObjectId


@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Landing page of the applicaton that present a form to enter various
        information and save.
    :return: index page
    """
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        city = request.form['city']

        try:
            all = mongodb.db.addressbuk.find_one({'phone_number': phone_number})
        except ConnectionError as e:
            print("Connection Error - {}".format(e))
            flash("Something went wrong", "danger")
            return render_template('index.html', contact={}, search="", home="active")

        if all is not None:
            flash("Phone number already exists", "danger")
            return redirect(url_for('index'))

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
    return render_template('index.html', contact={}, search="", home="active")


@app.route('/edit/<string:id>/', methods=['GET', 'POST'])
def edit(id):
    """
        Edit the record saved in the database.
    :param id: id of the record to be edited
    :return: html template
    """
    contact = mongodb.db.addressbuk.find_one({'_id': ObjectId(id)})
    print(id)
    if request.method == "POST":
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        city = request.form['city']

        try:
            all = mongodb.db.addressbuk.find_one({'phone_number': phone_number})
        except ConnectionError as e:
            print("Connection Error - {}".format(e))
            flash("Something went wrong", "danger")
            return render_template('index.html', contact={}, search="", home="active")

        if all is not None:
            print(all['phone_number'], phone_number, all['_id'], id)
            if all['phone_number'] == phone_number and all['_id'] != id:
                flash("Phone number already exists", "danger")
                return redirect(url_for('edit', id=id))

        one = {
            'phone_number': phone_number.lower(),
            'first_name': first_name.lower(),
            'last_name': last_name.lower(),
            'address': address,
            'city': city.lower(),
            'date': datetime.utcnow().isoformat()
        }

        mongodb.db.addressbuk.update_one(
            {'_id': ObjectId(id)},
            {'$set': one}
        )

        flash("Record Updated successfully", "success")
        return redirect(url_for('search'))

    return render_template('edit.html', contact=contact)


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
        Searches the database for contact information
    :return: Html template
    """
    if request.method == "POST":
        search_by = request.form['search_by']
        search_item = request.form['search_item']

        if not search_by or not search_item:
            flash("Incomplete Query Input", "danger")
            return render_template('search.html', search="active", home="")

        try:
            all = mongodb.db.addressbuk.find({search_by.lower(): search_item.lower()})
        except ConnectionError as e:
            print("Connection Error - {}".format(e))
            flash("Something went wrong", "danger")
            return render_template('search.html', search="active", home="")

        all_item = list(all)
        return render_template('search.html', list=all_item, search="active", home="")
    return render_template('search.html', search="active", home="")


@app.route('/delete/<string:id>/', methods=['POST'])
def delete(id):
    """
        Deletes a record in the address book
    :param id: The id of the item to be deleted
    :return: Html template
    """
    one_contact = mongodb.db.addressbuk.find_one({'_id': ObjectId(id)})
    if not one_contact:
        flash("No Record found", "danger")
        return redirect(url_for('search'))
    mongodb.db.addressbuk.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('search'))
