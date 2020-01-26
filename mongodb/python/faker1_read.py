#Read inserted values by faker1.py script.


import pymongo
import pprint

client = pymongo.MongoClient("mongodb://mongo:27017/")

db = client["faker1"]

for i in range(10):
    pprint.pprint(db.faker1.find_one())


