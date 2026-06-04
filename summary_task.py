from crewai import Task
from agents.summarizer import summarizer

summary_task = Task(
    description="""
    Create a final professional summary report.
    """,
    expected_output="Final summarized report",
    agent=summarizer
)