from models.chatmodel import ChatModel
from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import Session
from Repository.ChatRepository import ChatRepository 


ct = ChatRepository()

class ChatService:

    def get_chat(self,db:Session, user_id: UUID):
        return ct.get_chats(db,user_id)



    