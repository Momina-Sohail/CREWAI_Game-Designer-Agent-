from crewai import Agent,Task,Crew,LLM
from dotenv import load_dotenv
import os
load_dotenv()

import litellm
original_completion = litellm.completion

def patched_completion(*args, **kwargs):
   
    if 'messages' in kwargs:
        for msg in kwargs['messages']:
            if isinstance(msg, dict) and 'cache_breakpoint' in msg:
                del msg['cache_breakpoint']
    return original_completion(*args, **kwargs)

litellm.completion = patched_completion

llm = LLM(model="groq/llama-3.3-70b-versatile",
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
    description="Write complete, runnable Python code using pygame for a text-based "
        "educational game (history or math) for kids. Include a game loop, "
        "scoring, and clear instructions.",
    expected_output="Complete, runnable pygame code with no placeholders or partial snippets.",
    agent = game_designer_agent
)

crew = Crew(
    agents=[game_designer_agent],
    tasks=[game_designer_task]
)

result = crew.kickoff()
print(result)