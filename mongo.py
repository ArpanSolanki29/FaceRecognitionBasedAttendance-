import pymongo

#make connection
from pymongo import *
import datetime

class mongo:
    print("hello mongo")

def startConnection():
    client = MongoClient('mongodb://localhost:27017/')
    #Creating a database
    db = client.myfirstdb
    #Getting a collection
    collection = db.myfirstcollection
    return collection,db

def posting(name):
    collection,db = startConnection()
    post = {"author": name,
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    #inserting into databse
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print(post_id)