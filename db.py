from pymongo import MongoClient
from os import getenv
from urllib.parse import quote

class Db:
    PWD = getenv("MONGODB_PASSWORD")
    CONNECTION_STRING = f'mongodb+srv://login:{quote(PWD)}@cluster0.uivfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    def __init__(self, pwd=PWD, cnx=CONNECTION_STRING):
        self.PWD = pwd
        self.CONNECTION_STRING = cnx
        client = MongoClient(self.CONNECTION_STRING)
        self.client = client
    
    def test_connection(self):
        return self.client.test


if __name__ == '__main__':
    database = Db()
    print(database.test_connection())