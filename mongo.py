import pymongo
import os
if os.path.exists("env.py"):
  import env 
# from os import path
# if path.exists("env.py"):
#     import env
# Import mongo url from env file, set database and collection
MONGODB_URI = os.environ.get('MONGO_URI')
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({'nationality': 'english'}, {'$set': {'hair_colour': 'gold'}})

documents = coll.find({'nationality': 'english'})

for doc in documents:
    print(doc)

