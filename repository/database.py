import sys

from .mongo.MongoDB import *

USERNAME = sys.argv[1]
PASS = sys.argv[2]
DB_NAME = "MongoCollege"
COLLECTIONS = {"student": AUTO_INCREMENT, "teacher": DEFAULT}

# first.last@mongocollege.edu -> teacher id
URL = f"mongodb+srv://{USERNAME}:{PASS}@cluster0.u6lhh.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

CONNECTION = MongoDB(database=DB_NAME, docs=COLLECTIONS, url=URL)
