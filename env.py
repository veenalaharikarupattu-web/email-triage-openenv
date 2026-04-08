import openenv
from models import Action, Observation
from tasks import tasks

class EmailTriageEnv(openenv.Environment):
    def __init__(self):
        self.current_task_index = 0
        self.actions_taken = {}

    def reset(self) -> Observation:
        # Cycle through the 3 tasks
        task = tasks[self.current_task_index]
        self.actions_taken = {}
        return Observation(
            unread_count=len(task.emails),
            emails=task.emails,
            current_status=f"Starting Task: {task.name} ({task.difficulty})"
        )

    def step(self, action: Action):
        task = tasks[self.current_task_index]
        self.actions_taken[action.email_id] = action.category
        
        # Reward Logic (Rule 4)
        reward = 0.0
        if action.category == task.target_mapping.get(action.email_id):
            reward = 1.0  # Correct!
        else:
            reward = -0.5 # Mistake
            
        done = len(self.actions_taken) >= len(task.emails)
        
        # Move to next task if done
        if done:
            self.current_task_index = (self.current_task_index + 1) % len(tasks)
            
        return self.reset(), reward, done, {"score": task.grade(self.actions_taken)}