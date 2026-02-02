from agno.agent import Agent 
from agno.models.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
agent = Agent(
    model = Groq(id = "llama-3.1-8b-instant"),
    description=" You are a helpful and very good AI assistant",
    tools = [],
    markdown= True
    )
agent.print_response("Who is Salman khan?", stream= True)