from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import os

load_dotenv()

llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")


class AgentState(TypedDict):
    topic: str
    raw_data: str
    summary: str
    recipient_email: str


def extract_data(state: AgentState) -> AgentState:
    print(f"\n[Step 1] Extracting data about: {state['topic']}")
    wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    raw_data = wiki.run(state['topic'])
    state['raw_data'] = raw_data
    print(f"Extracted {len(raw_data)} characters")
    return state


def summarize_data(state: AgentState) -> AgentState:
    print(f"\n[Step 2] Summarizing data...")
    prompt = f"Summarize this in 3-5 bullet points:\n\n{state['raw_data']}"
    response = llm.invoke(prompt)
    state['summary'] = response.content
    print(f"Summary generated")
    return state


def email_summary(state: AgentState) -> AgentState:
    print(f"\n[Step 3] Sending email...")
    sender_email = os.getenv("SENDER_EMAIL").strip()
    sender_password = os.getenv("EMAIL_PASSWORD").strip()
    
    try:
        message = MIMEText(state['summary'])
        message["From"] = sender_email
        message["To"] = state['recipient_email']
        message["Subject"] = f"Summary: {state['topic']}"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        print(f"Email sent to {state['recipient_email']}")
    except Exception as e:
        print(f"Error: {e}")
    
    return state


def create_agent():
    workflow = StateGraph(AgentState)
    workflow.add_node("extract", extract_data)
    workflow.add_node("summarize", summarize_data)
    workflow.add_node("email", email_summary)
    
    workflow.set_entry_point("extract")
    workflow.add_edge("extract", "summarize")
    workflow.add_edge("summarize", "email")
    workflow.add_edge("email", END)
    
    return workflow.compile()


if __name__ == "__main__":
    topic = "political history of usa"
    recipient_email = "recipient@example.com"
    
    agent = create_agent()
    result = agent.invoke({
        "topic": topic, 
        "raw_data": "", 
        "summary": "",
        "recipient_email": recipient_email
    })
    
    print(f"\n Complete!")
