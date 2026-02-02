from crewai import Agent, Task, Crew
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()
# print(os.getenv("GROQ_API_KEY"))

llm = LLM(model="groq/llama-3.1-8b-instant", temperature=0)

# dev_agent = Agent(
#     role="Senior Python Developer",
#     goal="Write and debug Python code",
#     backstory="Expert Python developer with 10 years of experience",
#     llm=llm,
#     verbose = True  
# )


research_agent = Agent(
    role="Research Analyst",
    goal="Research and gather information from the web",
    backstory="Expert researcher with strong analytical skills",
    llm=llm,
    verbose=True
)

task1 = Task(
    description="Research and provide information about P.V. Sindhu, the Indian badminton player",
    expected_output="A comprehensive summary about P.V. Sindhu including her achievements and career highlights",
    agent=research_agent
)

crew = Crew(
    agents=[research_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print(result)


