from pymongo import MongoClient

client = \
    MongoClient("mongodb+srv://conghua:8V9A6JTzJEH29AJ@mongotest-h0ilz.mongodb.net/test?retryWrites=true&w=majority")


def getData(_id):
    cursor = client['sample_airbnb']['listingsAndReviews'].find({"_id": {"$gt": _id}})
    print(cursor.count())
    return cursor


def getDataPosts():
    return client['sample_training']['posts'].find()
