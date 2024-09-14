from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task,writer_task

## Forming the tech focused crew with some enhanced cofiguration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,writer_task],
    process=Process.sequential
)


# starting the task execution process with enhanced feedback
# result = crew.kickoff(inputs = {'topic advancements formatted as markdown': "AI in healthcare"})
result = crew.kickoff(inputs={'topic': 'AI in healthcare','topic advancements formatted as markdown': "AI in healthcare"})

print(result) 