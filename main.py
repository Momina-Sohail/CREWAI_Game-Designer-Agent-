# variable

# name = "John"
# num1 = 5
# bool = True/False
# floating number = 3.14


from crewai import Agent,Task,Crew,LLM
from dotenv import load_dotenv
import os
load_dotenv()

# Monkey patch to remove cache_breakpoint from Groq calls
import litellm
original_completion = litellm.completion

def patched_completion(*args, **kwargs):
    # Remove cache_breakpoint from messages if present
    if 'messages' in kwargs:
        for msg in kwargs['messages']:
            if isinstance(msg, dict) and 'cache_breakpoint' in msg:
                del msg['cache_breakpoint']
    return original_completion(*args, **kwargs)

litellm.completion = patched_completion

llm = LLM(model="groq/llama-3.1-8b-instant",
          api_key = os.getenv("GROQ_API_KEY"),
          max_tokens=4096
)

game_designer_agent=Agent(
    role="Game Designer Developer",
    goal="Design a text based game for the user to play using python that will use the pygame library to create the game",
    backstory="you are game designer developer that will built a text base game for kids and teens to play and learn about history and math or any other subject",
    llm=llm
)

game_designer_task = Task(
    description="you are a game designer developer which have 15 years of experience in gaming industry and love to build text based game for kids",
    expected_output="you are a game designer developer",
    agent = game_designer_agent
)

crew = Crew(
    agents=[game_designer_agent],
    tasks=[game_designer_task],
    llm=llm
)

result = crew.kickoff()
print(result)