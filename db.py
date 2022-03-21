from pymongo import MongoClient
from os import getenv
from urllib.parse import quote

class Db:

    def __init__(self, USR="login", PWD=getenv("MONGODB_PASSWORD")):
        self.USR = USR
        self.PWD = PWD
        CONNECTION_STRING = f'mongodb+srv://{self.USR}:{quote(self.PWD)}@cluster0.uivfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        client = MongoClient(CONNECTION_STRING)
        self.client = client
    
    def test_connection(self):
        return self.client.test


if __name__ == '__main__':
    database = Db()
    print(database.test_connection())