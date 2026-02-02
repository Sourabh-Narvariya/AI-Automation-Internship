from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

app = Flask(__name__)

# MongoDB Connection
load_dotenv()
MONGO_URI = os.getenv("connection_string")
client = MongoClient(MONGO_URI)

db = client["SourabhDB"]
collection = db["generated_results"]

# Helper: Today's Date Range

def get_today_range():
    start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    return start, end


# API Route: Get Today's Entries

@app.route("/today", methods=["GET"])
def get_today_entries():
    start, end = get_today_range()

    results = list(collection.find({
        "date_time": {
            "$gte": start,
            "$lt": end
        }
    }, {"_id": 0}))  

    return jsonify({
        "count": len(results),
        "entries": results
    })


# Run Flask App

if __name__ == "__main__":
    app.run(debug=True)
