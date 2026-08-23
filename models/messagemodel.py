from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class MessageModel(BaseModel):
    message_id:int |None = None
    content : str |None = None
    message_sent: datetime | None = None
    sender_id: UUID | None = None
    display_Name:str | None = "Unknown"
