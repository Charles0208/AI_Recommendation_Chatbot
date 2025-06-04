import time
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool
from src.AI_Recommendation_Chatbot.tools.search_victorylive_events import VictoryLiveEventSearchTool

@CrewBase
class AI_Recommendation_ChatbotCrew():
    """AI_Recommendation_Chatbot crew"""

    @agent
    def conversation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['conversation_specialist'],
        )

    @agent
    def web_search_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['web_search_expert'],
            tools=[SerperDevTool(), ScrapeWebsiteTool(), VictoryLiveEventSearchTool()],
        )

    # @agent
    # def scraping_specialist(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['scraping_specialist'],
    #         tools=[SerperDevTool(), ScrapeWebsiteTool()],
    #     )

    @task
    def conversation_task(self) -> Task:
        return Task(
            config=self.tasks_config['conversation_task'],
        )

    @task
    def performer_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['performer_search_task'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
        )
        
    @task
    def search_providers_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_providers_task'],
            tools=[VictoryLiveEventSearchTool()],
        )

    # @task
    # def fetch_event_details_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['fetch_event_details_task'],
    #         tools=[ScrapeWebsiteTool(), SerperDevTool()],
    #         expected_output=self.tasks_config['fetch_event_details_task']['expected_output'],
    #         input_schema={
    #             "user_input": str,
    #             "recommendations": list,
    #             "preferences": dict
    #         }
    # )

    @crew
    def crew(self) -> Crew:
        """Creates the AI_Recommendation_Chatbot crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True, # Enables short-term, long-term, and entity memory
            verbose=True,
        )
