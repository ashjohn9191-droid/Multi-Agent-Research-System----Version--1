from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)
planner = Agent(
    role="Research Planner",
    goal="Create a detailed research plan",
    backstory="Expert planner who breaks complex topics into tasks.",
    llm=llm,
    verbose=True
)
