Game Designer Agent

## What Does This Do?

This project is an AI agent that acts like a game designer. You give it a simple instruction, and it writes complete, ready-to-run Python code for a simple educational game — designed to help kids and teens learn subjects like history and math while playing, instead of just reading.

Instead of just explaining what a game could look like, it actually writes the full code for the game: the game screen, the questions, clicking to answer, and keeping score.

## How It Works

1. An **AI agent** is set up and told to act like an experienced game designer.
2. It's given clear instructions on what to create: a complete, working game — not just an idea or description.
3. The agent uses **Groq**, a fast AI model, to actually write the code.
4. A small fix is included in the code to make sure the AI model and the tool talking to it work together properly.
5. When you run the script, the agent writes out the full game code, which you can then save and run yourself.

## Example Output

When you run it, the agent writes a simple quiz game — it shows a question with multiple answers, lets you click one, and keeps track of your score as you go.