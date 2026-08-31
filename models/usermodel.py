from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class UserModel(BaseModel):
    mobile_no:str |None = None
    user_name : str |None = None
    last_seen: datetime | None = None
    user_id: UUID | None = None
    about:str | None = "Unknown"
