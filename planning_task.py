from crewai import Task
from agents.planner import planner

planning_task = Task(
    description="""
    Create a detailed research plan for the given topic:
    {topic}
    """,
    expected_output="Research plan with key points",
    agent=planner
)