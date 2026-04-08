from typing import List, Dict
from models import Email

class TriageTask:
    def __init__(self, name: str, difficulty: str, emails: List[Email], target_mapping: Dict[str, str]):
        self.name = name
        self.difficulty = difficulty
        self.emails = emails
        self.target_mapping = target_mapping  # {email_id: "correct_category"}

    def grade(self, agent_actions: Dict[str, str]) -> float:
        """Grading logic: Returns a score between 0.0 and 1.0."""
        if not agent_actions:
            return 0.0
        
        score = 0
        total = len(self.target_mapping)
        
        for email_id, correct_cat in self.target_mapping.items():
            if agent_actions.get(email_id) == correct_cat:
                score += 1
        
        return score / total

# Define the 3 required tasks
tasks = [
    # Task 1: Easy - Sorting obvious Spam vs Work
    TriageTask(
        name="Basic Sorting",
        difficulty="easy",
        emails=[
            Email(id="e1", sender="hr@company.com", subject="Payroll", body="Submit your timesheet."),
            Email(id="e2", sender="win@lottery.net", subject="Winner!", body="You won $1M!")
        ],
        target_mapping={"e1": "work", "e2": "spam"}
    ),
    
    # Task 2: Medium - Handling Billing and Priority
    TriageTask(
        name="Financial Triage",
        difficulty="medium",
        emails=[
            Email(id="e3", sender="aws@amazon.com", subject="Invoice", body="Your monthly bill is due."),
            Email(id="e4", sender="ceo@company.com", subject="Quick Question", body="Are you free for a call?")
        ],
        target_mapping={"e3": "billing", "e4": "work"}
    ),
    
    # Task 3: Hard - Complex Contextual Decision
    TriageTask(
        name="Contextual Priority",
        difficulty="hard",
        emails=[
            Email(id="e5", sender="security@bank.com", subject="Alert", body="Unusual activity detected."),
            Email(id="e6", sender="newsletter@tech.com", subject="Daily Digest", body="Here is your news.")
        ],
        target_mapping={"e5": "work", "e6": "ignore"}
    )
]