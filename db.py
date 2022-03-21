from pymongo import MongoClient
from os import getenv
from urllib.parse import quote

def get_database():
    CONNECTION_STRING = f'mongodb+srv://login:{quote(getenv("MONGODB_PASSWORD"))}@cluster0.uivfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(CONNECTION_STRING)

    return client

if __name__ == '__main__':
    print(get_database().test)