import pymongo
from os import getenv
from urllib.parse import quote

class Db:
    def __init__(self, USR=getenv("MONGODB_USER"), PWD=getenv("MONGODB_PASSWORD")):
        self.USR = USR
        self.PWD = PWD
        CONNECTION_STRING = f'mongodb+srv://{quote(str(self.USR))}:{quote(str(self.PWD))}@cluster0.uivfa.mongodb.net/blog?retryWrites=true&w=majority'
        client = pymongo.MongoClient(CONNECTION_STRING)
        self.client = client
    
    def test_connection(self):
        return self.client.test

    def find(self, collection, query=None, database='blog'):
        self.database = self.client[database]
        self.collection = self.database[collection]
        self.query = query
        return self.collection.find(self.query)
    
    def find_one(self, collection, query=None, database='blog'):
        self.database = self.client[database]
        self.collection = self.database[collection]
        self.query = query
        return self.collection.find_one(self.query)


if __name__ == '__main__':
    database = Db()
    print(database.test_connection())