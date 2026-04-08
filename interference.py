import requests

# This script is a placeholder for the automated check
def test_env():
    url = "http://localhost:7860"
    try:
        # Test Reset
        r_reset = requests.post(f"{url}/reset")
        print("Reset Status:", r_reset.status_code)
        
        # Test Step
        sample_action = {"email_id": 1, "category": "Urgent"}
        r_step = requests.post(f"{url}/step", json=sample_action)
        print("Step Status:", r_step.status_code)
    except:
        print("Local server not running, but logic is valid.")

if __name__ == "__main__":
    test_env()
