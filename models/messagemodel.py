from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class MessageModel(BaseModel):
    message_id:int
    content : str
    timing: datetime