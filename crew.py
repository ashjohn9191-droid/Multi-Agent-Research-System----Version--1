from crewai import Task, Crew
from agents.researcher import researcher

research_task = Task(
    description="""
    Research {topic}

    Requirements:
    - Give important information only
    - Use bullet points
    - Maximum 150 words
    """,
    agent=researcher,
    expected_output="Short research report"
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)