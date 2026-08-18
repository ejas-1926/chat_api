from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class ChatModel(BaseModel):
 
    chat_id: int     #chat id 
    recent_chat: str #recent message name 
    chatusername:str #user name 
    last_active: datetime #time


