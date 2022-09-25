from flask import render_template, redirect, request, flash, url_for, jsonify
from app import app, mongodb
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json


class Pager:
    def __init__(self):
        self.has_prev = True


@app.route('/quickcheck', methods=['GET', 'POST'])
def index_page():
    q = request.args.get('q')

    if q:
        posts = mongodb.db.newsbuk.find({'type': q})
        count = mongodb.db.newsbuk.count_documents({'type': q})
    else:
        posts = mongodb.db.newsbuk.find()
        count = mongodb.db.newsbuk.count_documents({})

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pager = Pager()
    pager.has_prev = True
    if page == 1:
        pager.has_prev = False
    pager.prev_num = page - 1 if page > 2 else 1
    pager.next_num = page + 1 if count > (page * 10) else page
    pager.page = page
    print(pager.page, pager.has_prev, pager.prev_num, pager.next_num)
    pages = posts.skip(page * 10).limit(10)

    return render_template('quickcheck/index.html', posts=posts, pages=pages, pager=pager, page=page)


@app.route('/api/post/<id>', methods=['GET'])
def get_post(id):
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    type = request.args.get('type')

    if type:
        posts = mongodb.db.newsbuk.find({'type': type})
    else:
        posts = mongodb.db.newsbuk.find()

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    per_page = int(per_page) if per_page else 10

    pages = posts.skip(page * per_page).limit(per_page)
    list_cur = list(pages)

    # Converting to the JSON
    return dumps(list_cur, indent=2)


@app.route('/api/post', methods=['POST'])
def add_post():
    data = request.json

    if data['id']:
        data.pop('id')

    mongodb.db.addressbuk.insert_one(data)
    return jsonify({'status': 'true', 'message': 'News Created'}), 200


@app.route('/api/post', methods=['DELETE'])
def delete_post():
    id = request.json.get('id')
    one = mongodb.db.newsbuk.find_one({'id': int(id)})
    if not one:
        return jsonify({'status': 'false', 'message': f'id {id} not found'}), 404
    if one['id'] > 10000:
        return jsonify({'status': 'false', 'message': 'this News cannot be deleted'}), 403

    mongodb.db.newsbuk.delete_one({'id': id})
    return jsonify({'status': 'true', 'message': 'News deleted'}), 200


@app.route('/api/post', methods=['PUT'])
def update_post():
    data = request.json
    print(data)
    one = mongodb.db.newsbuk.find_one({'id': int(data['id'])})
    if not one:
        return jsonify({'status': 'false', 'message': f'id {id} not found'}), 404
    if one['id'] > 10000:
        return jsonify({'status': 'false', 'message': 'this News cannot be updated'}), 403

    mongodb.db.newsbuk.update_one(
        {'id': int(data['id'])},
        {'$set': data}
    )
    return jsonify({'status': 'true', 'message': 'News Updated'}), 200
