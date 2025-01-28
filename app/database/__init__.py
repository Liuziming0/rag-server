from pymongo import MongoClient
from config import Config

client = MongoClient(Config.BASE_URL, Config.DB_PORT)
db = client[Config.DB_NAME]