from fastapi import APIRouter,Depends
from models.chatmodel import ChatModel
from datetime import datetime
from Service.chat_service import ChatService
from sqlalchemy.orm import Session
from database.database import engine
from uuid import UUID
from database.database import get_db


router = APIRouter()

chatservice  = ChatService();



# chat id participant name last chat last chat time this much we will get from this 
@router.get("/chats",response_model=list[ChatModel])
def get_chat(user_id:UUID,db: Session = Depends(get_db)):
    x = chatservice.get_chat(user_id= user_id,db=db)
    print(x)



   #return chatservice.get_chat(user_id=user_id,db=db)
   # return ChatModel(recent_chat="Hello World",chat_id=chat_id,chatusername="abc",last_active=datetime.now())







