from fastapi import APIRouter
from models.chatmodel import ChatModel
from datetime import datetime
from Service.chat_service import ChatService
from sqlalchemy import inspect
from database.database import engine

router = APIRouter()

chatservice  = ChatService();



# chat id participant name last chat last chat time this much we will get from this 
@router.get("/chats/{chat_id}",response_model=ChatModel)
def get_chat(chat_id:int):
    return chatservice.get_chat(chat_id=chat_id)
    return ChatModel(recent_chat="Hello World",chat_id=chat_id,chatusername="abc",last_active=datetime.now())







