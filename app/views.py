from flask import render_template, redirect, request, flash, url_for
from app import app, mongodb
from datetime import datetime
from bson.objectid import ObjectId


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        city = request.form['city']

        # if not first_name or not last_name or phone_number or\
        #     not address or not city:
        #     flash("Incomplete Data", "danger")
        #     return redirect(url_for('index'))

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


@app.route('/<string:id>/', methods=['GET', 'POST'])
def edit(id):
    contact = mongodb.db.addressbuk.find_one({'_id': ObjectId(id)})
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']
        city = request.form['city']

        # if not first_name or not last_name or phone_number or \
        #         not address or not city:
        #     flash("Incomplete Data", "danger")
        #     return redirect(url_for('index'))

        one = {
            'phone_number': phone_number.lower(),
            'first_name': first_name.lower(),
            'last_name': last_name.lower(),
            'address': address,
            'city': city.lower(),
            'date': datetime.utcnow().isoformat()
        }

        print(id)

        mongodb.db.addressbuk.update_one(
            {'_id': ObjectId(id)},
            {'$set': one}
        )

        flash("Record Updated successfully", "success")
        return redirect(url_for('index'))

    print(contact)

    return render_template('index.html', contact=contact)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_by = request.form['search_by']
        search_item = request.form['search_item']

        if not search_by or not search_item:
            flash("Incomplete Query Input", "danger")
            return render_template('search.html', search="active", home="")

        # query database
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
    one_contact = mongodb.db.addressbuk.find_one({'_id': ObjectId(id)})
    if not one_contact:
        flash("No Record found", "danger")
        return redirect(url_for('search'))
    mongodb.db.addressbuk.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('search'))