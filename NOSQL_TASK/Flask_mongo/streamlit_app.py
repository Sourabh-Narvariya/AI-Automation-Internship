import streamlit as st
from pymongo import MongoClient
from datetime import datetime
from transformers import pipeline
from dotenv import load_dotenv
import os

# ============================================
# LOAD ENVIRONMENT VARIABLES (CRITICAL!)
# ============================================
load_dotenv()

# PAGE CONFIG - Auto refresh every 3 seconds
st.set_page_config(page_title="MongoDB Live AI", layout="wide", initial_sidebar_state="expanded")
st.markdown('<meta http-equiv="refresh" content="3">', unsafe_allow_html=True)

# LOAD AI MODEL
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2", temperature=0.7)

generator = load_model()

# MONGODB CONNECTION WITH VALIDATION
MONGO_URI = os.getenv("connection_string")

if not MONGO_URI:
    st.error("ERROR: connection_string not found in .env file!")
    st.info("""
    **How to fix:**
    1. Create/edit `.env` file in your project directory
    2. Add: `connection_string=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority`
    3. Save and restart Streamlit
    """)
    st.stop()

try:
    # Connect with timeout
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
    # Test connection
    client.server_info()
    st.sidebar.success("MongoDB Atlas Connected!")
    
except Exception as e:
    st.error(f"MongoDB Connection Error:\n{str(e)}")
    st.info("""
    **Troubleshooting:**
    - Check your internet connection
    - Verify MongoDB URI is correct in .env
    - Check if IP is whitelisted in MongoDB Atlas
    - Try: `mongodb://localhost:27017` if using local MongoDB
    """)
    st.stop()

# Connect to database
db = client["SourabhDB"]
collection = db["generated_results"]

# SIDEBAR - CONNECTION INFO
with st.sidebar:
    st.markdown("### Database Status")
    st.write(f"**Database:** {db.name}")
    st.write(f"**Collection:** {collection.name}")
    try:
        doc_count = collection.count_documents({})
        st.metric("Total Documents", doc_count)
    except Exception as e:
        st.warning(f"Could not fetch count: {e}")

# MAIN APP - TITLE
st.title("GPT-2 Live AI Generator")
st.markdown("*Connected to MongoDB Atlas • Auto-refreshes every 3 seconds*")

# INPUT & GENERATION
col1, col2 = st.columns([4, 1])
with col1:
    prompt = st.text_input("Enter your prompt:", placeholder="Type something creative...")
with col2:
    generate_btn = st.button(" Generate", use_container_width=True)

if generate_btn:
    if prompt.strip():
        with st.spinner("Generating..."):
            try:
                output = generator(prompt, max_length=80, num_return_sequences=1)
                result = output[0]["generated_text"]
                
                # Prepare data
                data = {
                    "prompt": prompt,
                    "result": result,
                    "timestamp": datetime.now()
                }
                
                # Save to MongoDB
                insert_result = collection.insert_one(data)
                st.success(f"Saved to MongoDB! (ID: {str(insert_result.inserted_id)[:8]}...)")
                
                # Display result
                st.info(f"**Generated Output:**\n{result}")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt first!")

# MANUAL REFRESH BUTTON
st.divider()
if st.button("Refresh Results Now", use_container_width=True):
    st.rerun()

# LIVE RESULTS FROM MONGODB
st.subheader("Live Results (Auto-updates every 3 sec)")

try:
    # Fetch latest results
    results = list(collection.find().sort("timestamp", -1).limit(20))
    
    if not results:
        st.info(" No results yet. Generate some text above!")
    else:
        st.markdown(f"** Showing {len(results)} latest results** (Total in DB: {collection.count_documents({})})")
        
        for idx, doc in enumerate(results, 1):
            with st.container(border=True):
                col1, col2 = st.columns([0.3, 3])
                with col1:
                    st.markdown(f"**#{idx}**")
                with col2:
                    st.markdown(f"**Prompt:** `{doc['prompt']}`")
                    st.markdown(f"**Result:** {doc['result']}")
                    st.caption(f" {doc['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                    
except Exception as e:
    st.error(f" Error fetching results: {str(e)}")
