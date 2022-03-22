import pymongo
from os import getenv
from urllib.parse import quote

class Db:
    def __init__(self, USR=getenv("MONGODB_USER"), PWD=getenv("MONGODB_PASSWORD")):
        self.USR = USR
        self.PWD = PWD
        CONNECTION_STRING = f'mongodb+srv://{self.USR}:{quote(self.PWD)}@cluster0.uivfa.mongodb.net/blog?retryWrites=true&w=majority'
        client = pymongo.MongoClient(CONNECTION_STRING)
        self.client = client
    
    def test_connection(self):
        return self.client.test

    def find(self, collection, database='blog'):
        self.database = self.client[database]
        self.collection = self.database[collection]
        return self.collection.find()
    
    def find_one(self, collection, database='blog'):
        self.database = self.client[database]
        self.collection = self.database[collection]
        return self.collection.find_one()


if __name__ == '__main__':
    database = Db()
    print(database.test_connection())
    print([x for x in database.find('users')])