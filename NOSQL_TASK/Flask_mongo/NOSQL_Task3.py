from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from transformers import pipeline
import os
from dotenv import load_dotenv

app=Flask(__name__)

load_dotenv()
uri=os.getenv("connection_string")

genrator=pipeline("text-generation",model="gpt2", temperature=0.7, top_k=50, top_p=0.95, num_return_sequences=1)
client=MongoClient(uri)
db=client["SourabhDB"]
collection=db["generated_results"]

@app.route("/generate",methods=["POST","GET"])
def user_data():
    data=request.json
    prompt=data.get("prompt")

    output=genrator(prompt,max_length=50)[0]["generated_text"]

    store_data={
        "Prompt":prompt,
        "output":output,
        "date_time":datetime.now()
    }
    collection.insert_one(store_data)
    if request.method=="GET":
        return "Work is done"

    return jsonify({
        "prompt":prompt,
        "output":output,
        "result":"data saved"
    })


if __name__=="__main__":
    app.run(debug=True)