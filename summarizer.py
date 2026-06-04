from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)
summarizer = Agent(
    role="Summary Writer",
    goal="Create concise and readable reports",
    backstory="Professional report writer.",
    llm=llm,
    verbose=True
)
