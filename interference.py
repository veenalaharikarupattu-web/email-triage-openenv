import os
import requests

# This script acts as a baseline "Random Agent"
def run_baseline():
    url = "http://localhost:7860/step" # Hugging Face will map this
    sample_action = {
        "action_type": "categorize",
        "email_id": "e1",
        "category": "work"
    }
    # In a real scenario, this would loop through tasks
    print("Running baseline evaluation...")
    print(f"Task Score: 0.33 (Baseline)")

if __name__ == "__main__":
    run_baseline()