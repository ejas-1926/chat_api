from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
class UserModel(BaseModel):
    username:str|None = None
    user_id:UUID|None = None
    last_active:datetime|None = None
    phone_number:str|None = None
