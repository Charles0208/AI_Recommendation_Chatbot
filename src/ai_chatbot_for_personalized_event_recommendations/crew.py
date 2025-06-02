import time
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class AiChatbotForPersonalizedEventRecommendationsCrew():
    """AiChatbotForPersonalizedEventRecommendations crew"""

    @agent
    def conversation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['conversation_specialist'],
        )

    @agent
    def web_search_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['web_search_expert'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
        )
        
    @agent
    def filtering_and_ranking_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['filtering_and_ranking_specialist'],
        )

    @agent
    def scraping_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['scraping_specialist'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )


    @task
    def conversation_task(self) -> Task:
        return Task(
            config=self.tasks_config['conversation_task'],
        )

    @task
    def fetch_events_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_events_data_task'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
        )

    @task
    def filter_and_rank_task(self) -> Task:
        return Task(
            config=self.tasks_config['filter_and_rank_task'],
        )

    @task
    def present_results_task(self) -> Task:
        return Task(
            config=self.tasks_config['present_results_task'],
        )

    @task
    def fetch_event_details_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_event_details_task'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiChatbotForPersonalizedEventRecommendations crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True, # Enables short-term, long-term, and entity memory
            verbose=False,
        )
