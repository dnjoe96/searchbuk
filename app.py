import os
import time
import urllib.parse
from threading import Thread

from app import app, MONGO_URI


def update_db():
    from pymongo import MongoClient
    import requests

    try:
        conn = MongoClient(MONGO_URI)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    db = conn.searchbuk.newsbuk
    base_url = 'https://hacker-news.firebaseio.com/v0'
    new_stories = base_url + '/newstories.json?print=pretty'

    r = requests.get(url=new_stories)

    curr_record = db.distinct('id')

    for one in r.json():
        if one in curr_record:
            # print('Record already found')
            continue

        story = base_url + f'/item/{one}.json?print=pretty'
        r = requests.get(url=story)

        print(r.json()['type'])
        db.insert_one(r.json())


def background_task():
    while True:
        time.sleep(5)
        update_db()


print('Starting background task...')
daemon = Thread(target=background_task, daemon=True, name='Monitor')
daemon.start()


if __name__ == '__main__':
    app.run(debug=True)
