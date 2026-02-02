import streamlit as st
from datetime import datetime

#  Firebase Firestore Setup 
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_keys.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Transformer Model 
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

chatbot = load_model()

def generate_response(prompt):
    result = chatbot(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]

# Streamlit UI 
st.set_page_config(page_title="Chatbot with Firestore", layout="centered")

st.title(" AI Chatbot")
st.write("Chat with the bot. Conversations are saved in Firebase Firestore.")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate bot reply
    bot_reply = generate_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save to Firestore
    db.collection("chat_logs").add({
        "user_message": user_input,
        "bot_response": bot_reply,
        "timestamp": datetime.now()
    })
