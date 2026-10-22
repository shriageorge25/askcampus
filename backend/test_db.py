import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
db = MongoClient(os.getenv("MONGODB_URI"))["askcampus"]
db.ping.insert_one({"ok": True})
print(db.ping.find_one())