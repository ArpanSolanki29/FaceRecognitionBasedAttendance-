
#make connection
from pymongo import *
import datetime


class mongo:
    print("hello mongo")


def startConnection():
    client = MongoClient('mongodb://localhost:27017/')
#    #Creating a database
    db = client.myfirstdb
#    #Getting a collection
    collection = db.myfirstcollection

    return collection, db


def FindOne(value, database, input, output):
    collection, db = startConnection()
    result = db[database].find_one({input: value})
    print("result")
    print(result)
    return result.get(output)



def Insert(dict, Collection):
    collection, db = startConnection()
    print("Inserting")
    posts = db[Collection]
    post_id = posts.insert_one(dict).inserted_id
    print(post_id)


def Create():
    print("CREATING")


def posting(name):
    collection, db = startConnection()
    post = {"author": name,
            "subject": "My first blog post!",
            "Present": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

#    inserting into databse
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print(post_id)


def test():
    collection, db = startConnection()