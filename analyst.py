from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)
analyst = Agent(
    role="Research Analyst",
    goal="Analyze collected information and extract insights",
    backstory="Expert analyst who identifies trends and patterns.",
    llm=llm,
    verbose=True
)
