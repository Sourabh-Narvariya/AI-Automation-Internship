from pymongo import MongoClient

import os
from dotenv import load_dotenv

connection_string = os.getenv("connection_string")
client = MongoClient(connection_string)

#  Database name
db = client["User-Task1"]  
# collecction name
collection = db["users"]

data = {
    "name": "Sourabh Narvariya",
    "age": 22,
    "city": "Indore",
    "Skills": ["Python", "ML", "MongoDB"]

}
collection.insert_one(data)

print("Data inserted successfully")

for user in collection.find():
    print(user)

    

