from bson import json_util
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://default:verygoodpassword@discotech.b8mzxei.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.DISCoTech
collection = db.resources

class controller:

  @staticmethod
  def find_all():
    return json_util.dumps(collection.find())
