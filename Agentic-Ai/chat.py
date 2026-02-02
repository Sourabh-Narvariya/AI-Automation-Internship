from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()



llm = ChatGroq(model="llama-3.1-8b-instant")

# ---------------- STATE ----------------
class ChatState(TypedDict):
    user_input: str
    agent_response: str
    final_response: str

# ---------------- AGENTS ----------------

def router_agent(state: ChatState):
    prompt = f"""
Decide which agent should answer:
User: {state['user_input']}

Agents:
- knowledge
- code
Return only agent name.
"""
    decision = llm.invoke(prompt).content.strip().lower()
    return {"agent_response": decision}

def knowledge_agent(state):
    res = llm.invoke(state["user_input"]).content
    return {"agent_response": res}

def code_agent(state):
    res = llm.invoke(f"Write code for: {state['user_input']}").content
    return {"agent_response": res}

def summary_agent(state):
    res = llm.invoke(f"Summarize: {state['agent_response']}").content
    return {"agent_response": res}

def critic_agent(state):
    res = llm.invoke(f"Improve and correct this:\n{state['agent_response']}").content
    return {"final_response": res}

# ---------------- GRAPH ----------------

graph = StateGraph(ChatState)

graph.add_node("router", router_agent)
graph.add_node("knowledge", knowledge_agent)
graph.add_node("code", code_agent)
graph.add_node("summary", summary_agent)
graph.add_node("critic", critic_agent)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda s: s["agent_response"],
    {
        "knowledge": "knowledge",
        "code": "code",
    },
)

graph.add_edge("knowledge", "summary")
graph.add_edge("code", "summary")
graph.add_edge("summary", "critic")
graph.add_edge("critic", END)

app = graph.compile()

# ---------------- CHAT LOOP ----------------

while True:
    user = input("You: ")
    result = app.invoke({"user_input": user})
    print("\nAI:", result["final_response"])



