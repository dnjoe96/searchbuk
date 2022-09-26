import random
import time
from flask import render_template, redirect, request, flash, url_for, jsonify
from app import app, mongodb
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json
import uuid


class Pager:
    def __init__(self):
        self.has_prev = True

    def to_date(self, poxis_time):
        return datetime.utcfromtimestamp(poxis_time).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/quickcheck', methods=['GET', 'POST'])
def index_page():
    search_item = request.args.get('search_item')
    print(search_item)
    if search_item:
        print('in search item')
        posts = mongodb.db.newsbuk.find({'type': search_item})
        count = mongodb.db.newsbuk.count_documents({'type': search_item})
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
    pager.prev_num = page - 1
    pager.next_num = page + 1 if count > (page * 10) else page
    pager.page = page
    print(pager.page, pager.has_prev, pager.prev_num, pager.next_num)

    pages = posts.skip((page - 1) * 10).limit(10)
    return render_template('quickcheck/index.html', pages=pages, pager=pager, search_item=search_item)


@app.route('/api/post', methods=['GET'])
def get_post():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    type = request.args.get('type')
    id = request.args.get('id')

    if id and id != "":
        post = mongodb.db.newsbuk.find_one({'id': int(id)})
        list_cur = [dict(post)]
        return dumps(list_cur, indent=2)

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

    data['id'] = random.randint(1000, 10000)
    data['time'] = time.time()
    print(data)
    mongodb.db.newsbuk.insert_one(data)
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
