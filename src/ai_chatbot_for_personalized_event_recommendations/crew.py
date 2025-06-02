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
            tools=[SerperDevTool()],
        )

    @agent
    def scraping_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['scraping_specialist'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def reasonability_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['reasonability_checker'],
        )

    @agent
    def ranking_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['ranking_specialist'],
        )


    @task
    def initiate_conversation_task(self) -> Task:
        return Task(
            config=self.tasks_config['initiate_conversation_task'],
            tools=[],
        )

    @task
    def perform_web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['perform_web_search_task'],
            tools=[SerperDevTool()],
        )

    @task
    def scrape_ticket_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_ticket_information_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def validate_results_task(self) -> Task:
        return Task(
            config=self.tasks_config['validate_results_task'],
            tools=[],
        )

    @task
    def rank_results_task(self) -> Task:
        return Task(
            config=self.tasks_config['rank_results_task'],
            tools=[],
        )

    @task
    def present_results_task(self) -> Task:
        return Task(
            config=self.tasks_config['present_results_task'],
            tools=[],
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
            verbose=True,
        )
