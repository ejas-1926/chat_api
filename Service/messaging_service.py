from models.messagemodel import MessageModel
from datetime import datetime
from Repository.MessageRepository import MessageRepository 
from sqlalchemy.orm import Session

repo = MessageRepository()
class MessagingService:

    


    def get_messages(self, chat_id: int, db: Session):
        print('reached service')
        model = repo.get_messages(db=db, chat_id=chat_id)
        print('left service')
        return model