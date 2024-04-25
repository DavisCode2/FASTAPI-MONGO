import urllib
# import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

username = urllib.parse.quote_plus("DavisCode")
password = urllib.parse.quote_plus("etc@atlaspymongo01")


# ca = certifi.where()
uri = "mongodb+srv://{}:{}@cluster0.qfkkeri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db

collection_name = db["todo_collection"]