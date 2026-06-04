from crewai import Task
from agents.researcher import researcher

research_task = Task(
    description="""
    Research the topic thoroughly:
    {topic}
    """,
    expected_output="Detailed research findings",
    agent=researcher
)