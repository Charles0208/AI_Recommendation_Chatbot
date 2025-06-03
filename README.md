# AI_Recommendation_Chatbot Crew

Welcome to the AI_Recommendation_Chatbot Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, install crewai:

```bash
uv tool install crewai
```

If this is your first time running this command, there will be a message to set the path to the package you just install. Follow the message.

Now, clone the repo and navigate to the project directory AI_Recommendation_Chatbot

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

Create a .env file in the base of the project directory. Add your api keys. An example .env file is shown below:

```bash
MODEL=gpt-4.1-mini # Found this was best openai model
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serer-api-key
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the AI_Recommendation_Chatbot Crew, assembling the agents and assigning them tasks as defined in your configuration.

If you would like the terminal to output a detailed log of the tasks and the agents' reasoning, set verbose=True in crew.py:crew

## Understanding the Crew

The AI_Recommendation_Chatbot Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Modifying the chatbot

- Modify `src/AI_Recommendation_Chatbot/config/agents.yaml` to modify agents
- Modify `src/AI_Recommendation_Chatbot/config/tasks.yaml` to modify tasks
- Modify `src/AI_Recommendation_Chatbot/crew.py` to add logic, tools and specific args
- Modify `src/AI_Recommendation_Chatbot/main.py` to add custom inputs for agents and tasks

## Online resource

For a video tutorial of the above steps, use this playlist: https://youtube.com/playlist?list=PLpkzjZ2JCjKJYqKavdl87BWotEaqbzjRt&si=dGBPnn2CBr94ll4p

## Support

For support, questions, or feedback regarding the AI_Recommendation_Chatbot Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
