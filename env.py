import openenv
from models import Action
from tasks import tasks

# We are creating a clean class without problematic inheritance
class EmailTriageEnv:
    def __init__(self):
        self.current_task_index = 0
        self.actions_taken = {}

    def reset(self):
        task = tasks[self.current_task_index]
        self.actions_taken = {}
        return {
            "unread_count": len(task.emails),
            "emails": [e.dict() for e in task.emails],
            "current_status": f"Starting Task: {task.name}"
        }

    def step(self, action_dict: dict):
        action = Action(**action_dict)
        task = tasks[self.current_task_index]
        self.actions_taken[action.email_id] = action.category
        
        reward = 1.0 if action.category == task.target_mapping.get(action.email_id) else -0.5
        done = len(self.actions_taken) >= len(task.emails)
        
        if done:
            self.current_task_index = (self.current_task_index + 1) % len(tasks)
            
        return self.reset(), reward, done, {"score": 100}
