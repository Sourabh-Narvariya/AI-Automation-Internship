import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timedelta
from transformers import pipeline
from dotenv import load_dotenv
import os
load_dotenv()

# Load GPT-2 Model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2", temperature=0.7)

generator = load_model()

# MongoDB Connection
MONGO_URI = os.getenv("connection_string")
client = MongoClient(MONGO_URI)

db = client["SourabhDB"]
collection = db["generated_results"]


# Helper: Today's Date Range
def get_today_range():
    start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    return start, end

# Streamlit UI
st.title("GPT-2 Text Generator (Live MongoDB)")

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if prompt:
        output = generator(prompt, max_length=80, num_return_sequences=1)
        result = output[0]["generated_text"]

        data = {
            "prompt": prompt,
            "result": result,
            "date_time": datetime.now()
        }

        collection.insert_one(data)
        st.success("Generated & saved to MongoDB")

        st.subheader("Generated Result")
        st.write(result)

# Today's Entries
st.subheader("Today's Entries")
start, end = get_today_range()

query = {
    "$or": [
        {"date_time": {"$gte": start, "$lt": end}},
        {"timestamp": {"$gte": start, "$lt": end}},
    ]
}

today_docs = list(collection.find(query, {"_id": 0}).sort("date_time", -1))
st.caption(f"Count: {len(today_docs)}")

if not today_docs:
    st.info("No entries found for today.")
else:
    for doc in today_docs:
        prompt_text = doc.get("prompt", "-unknown-")
        result_text = doc.get("result") or doc.get("output") or ""
        ts = doc.get("date_time") or doc.get("timestamp")
        st.markdown(f"**Prompt:** {prompt_text}")
        st.markdown(f"**Result:** {result_text}")
        st.caption(f"🕒 {ts}")
        st.divider()
