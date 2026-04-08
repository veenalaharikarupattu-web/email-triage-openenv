from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str

class Observation(BaseModel):
    unread_count: int
    emails: List[Email]
    current_status: str

class Action(BaseModel):
    # Agents can categorize or mark as urgent
    action_type: Literal["categorize", "mark_urgent", "ignore"]
    email_id: str
    category: Optional[Literal["work", "billing", "spam"]] = None