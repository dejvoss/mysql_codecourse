import pymongo
import os

# from os import path
# if path.exists("env.py"):
#     import env
# Import mongo url from env file, set database and collection
MONGO_URI = 'mongodb+srv://root:r00tUser@myfirstcluster-yipty.mongodb.net/myTestDB?retryWrites=true&w=majority'
MONGODB_URI = MONGO_URI
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

documents = coll.find()

for doc in documents:
    print(doc)

