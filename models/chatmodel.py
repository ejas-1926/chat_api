from uuid import UUID
from pydantic import BaseModel

class ChatModel(BaseModel):
    user_id: UUID | None = None
    recent_chat: str | None = None
    chatusername: str | None = None
    last_seen: str | None = None