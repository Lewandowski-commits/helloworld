from pymongo import MongoClient
from os import getenv

def get_database():
    CONNECTION_STRING = f'mongodb+srv://login:{getenv("MONGODB_PASSWORD")}@cluster0.uivfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(CONNECTION_STRING)

    return client

if __name__ == '__main__':
    get_database().test