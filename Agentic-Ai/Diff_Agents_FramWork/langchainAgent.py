from langchain_community.tools import WikipediaQueryRun  # pip install wikipedia
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(temperature=0, model_name = "llama-3.1-8b-instant")

wiki = WikipediaQueryRun(api_wrapper = WikipediaAPIWrapper())

agent = create_agent(llm, [wiki] )

response = agent.invoke({
    "messages":[("user" "Use Wikipedia to explain who is P.V.Sindhu ")]
})

print(response['messages'][-1].content)
