import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv('MONGODB_URL')
class Mongodb:
    def __init__(self, collection_name,database_name):
        self.client = pymongo.MongoClient(mongo_url)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

