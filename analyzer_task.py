from crewai import Task
from agents.analyst import analyst

analysis_task = Task(
    description="""
    Analyze all collected information and extract insights.
    """,
    expected_output="Important insights and conclusions",
    agent=analyst
)