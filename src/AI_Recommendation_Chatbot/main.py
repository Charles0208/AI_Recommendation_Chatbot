#!/usr/bin/env python
import sys
import time
import json
from datetime import datetime
from AI_Recommendation_Chatbot.crew import AI_Recommendation_ChatbotCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# Memory/session store for preferences and recommendations
MAX_HISTORY = 20
session_memory = {
    "preferences": [],
    "recommendations": {},
    "conversation_history": []
}

def run():
    """
    Run the crew with the full conversation.
    """
    print("Welcome to the chatbot! Type 'exit' to stop.")
    crew_instance = AI_Recommendation_ChatbotCrew()
    crew = crew_instance.crew()
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        inputs = {
            "user_input": user_input, 
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "recommendations":session_memory.get("recommendations"), 
            "preferences":session_memory.get("preferences"),
            "conversation_history": session_memory["conversation_history"],
        }

        try:
            start = time.time()
            result = crew.kickoff(inputs=inputs)
            raw_output_str = dict(result)['raw']
            result = json.loads(raw_output_str)

            session_memory["preferences"] = result["preferences"]
            session_memory["conversation_history"].append({"role": "user", "message": user_input})
            session_memory["conversation_history"].append({"role": "bot", "message": result["output"]})
            session_memory["conversation_history"] = session_memory["conversation_history"][-MAX_HISTORY:]
            
            session_memory["recommendations"] = result["output"]
            
            end = time.time()
            print("Bot:\n", result['output'], "\n")
            print(f"\n===🔁 Total runtime: {end - start:.2f} seconds===\n")
        except Exception as e:
            print(f"Error: {e}")
    

def run_simple():
    """
    Run the crew.
    """
    inputs = {
        "user_input": "I'm looking for concerts or NBA games in NYC this weekend. Preferably something popular or headlined by a major artist."
    }
    AI_Recommendation_ChatbotCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        
    }
    try:
        AI_Recommendation_ChatbotCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AI_Recommendation_ChatbotCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
            "user_input": "I'm looking for concerts or NBA games in NYC this weekend. Preferably something popular or headlined by a major artist.", 
            "recommendations":session_memory.get("recommendations"), 
            "preferences":session_memory.get("preferences"),
            "conversation_history": session_memory["conversation_history"],
    }
    try:
        AI_Recommendation_ChatbotCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

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


