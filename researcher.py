from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=300
)

researcher = Agent(
    role="AI Researcher",
    goal="Research topics and provide concise answers",
    backstory="Expert researcher who provides accurate information.",
    llm=llm,
    verbose=True
)