from pymongo import mongo_client
import pymongo
from .config import settings

client = mongo_client.MongoClient(
    "mongodb://newuser:password123@mongopes:27017/", serverSelectionTimeoutMS=5000)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
#User.create_index([("email", pymongo.ASCENDING)], unique=True)


MissingPerson = db.missingperson
#MissingPerson.create_index([("contact_number", pymongo.ASCENDING)], unique=True)

realtimeFaceVectors = db.realFacesV
foundPerson = db.foundPersons
streamLinks = db.streamlinks
FoundList = db.foundPersons