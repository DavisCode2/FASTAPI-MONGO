from fastapi import FastAPI
from routes.route import todo_router

app = FastAPI()


app.include_router(todo_router)


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import urllib.parse

# username = urllib.parse.quote_plus("DavisCode")
# password = urllib.parse.quote_plus("etc@atlaspymongo01")
# # password = etc@atlaspymongo01

# uri = "mongodb+srv://{}:{}@cluster0.qfkkeri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)