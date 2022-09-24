import requests
import os
import urllib.parse

username = urllib.parse.quote_plus(str(os.environ.get('MONGO_USER')))
password = urllib.parse.quote_plus(str(os.environ.get('MONGO_PASS')))
MONGO_URI = 'mongodb+srv://{}:{}@cluster0.of0j7.azure.mongodb.net/searchbuk?retryWrites=true&w=majority'.format(username, password)


from pymongo import MongoClient

try:
    conn = MongoClient(MONGO_URI)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.searchbuk.newsbuk

base_url = 'https://hacker-news.firebaseio.com/v0'

topstories = base_url + '/newstories.json?print=pretty'

r = requests.get(url=topstories)

curr_record = db.distinct('id')


count = 0
for one in r.json():
    if one in curr_record:
        print('Record already found')
        continue

    story = base_url + f'/item/{one}.json?print=pretty'
    r = requests.get(url=story)
    if count == 100:
        break
    print(r.json()['type'])
    db.insert_one(r.json())
    count += 1
