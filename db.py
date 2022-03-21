from pymongo import MongoClient
from os import getenv
from urllib.parse import quote

class Db:

    def __init__(self, PWD=getenv("MONGODB_PASSWORD")):
        CONNECTION_STRING = f'mongodb+srv://login:{quote(PWD)}@cluster0.uivfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        self.PWD = PWD
        client = MongoClient(CONNECTION_STRING)
        self.client = client
    
    def test_connection(self):
        return self.client.test


if __name__ == '__main__':
    database = Db()
    print(database.test_connection())