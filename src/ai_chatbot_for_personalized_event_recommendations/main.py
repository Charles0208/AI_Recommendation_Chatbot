#!/usr/bin/env python
import sys
import time
from ai_chatbot_for_personalized_event_recommendations.crew import AiChatbotForPersonalizedEventRecommendationsCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with the full conversation.
    """
    print("Welcome to the chatbot! Type 'exit' to stop.")
    crew_instance = AiChatbotForPersonalizedEventRecommendationsCrew()
    crew = crew_instance.crew()

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        inputs = {"user_input": user_input}

        try:
            start = time.time()
            result = crew.kickoff(inputs=inputs)
            end = time.time()
            print(f"\n===🔁 Total runtime: {end - start:.2f} seconds===\n")
            print("Bot:", result, "\n")
        except Exception as e:
            print(f"Error: {e}")
    

def run_simple():
    """
    Run the crew.
    """
    inputs = {
        "user_input": "I'm looking for concerts or NBA games in NYC this weekend. Preferably something popular or headlined by a major artist."
    }
    AiChatbotForPersonalizedEventRecommendationsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        
    }
    try:
        AiChatbotForPersonalizedEventRecommendationsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiChatbotForPersonalizedEventRecommendationsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        
    }
    try:
        AiChatbotForPersonalizedEventRecommendationsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "run-simple":
        run_simple()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
