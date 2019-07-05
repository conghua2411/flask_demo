from pymongo import MongoClient

from flaskDemo import runServer

client = MongoClient("mongodb+srv://conghua:8V9A6JTzJEH29AJ@mongotest-h0ilz.mongodb.net/test?retryWrites=true&w=majority")


# db = client.test

# 8V9A6JTzJEH29AJ

if __name__ == '__main__':
    runServer()
