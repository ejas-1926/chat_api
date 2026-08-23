from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ChatModel(BaseModel):
 
    chat_id: int
    recent_chat: str
    chatusername:str
    last_active: datetime
    user_id:UUID
