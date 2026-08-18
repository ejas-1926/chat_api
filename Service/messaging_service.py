from models.messagemodel import MessageModel
from datetime import datetime 
class MessagingService:

    def get_chat(self, chat_id: int):

        return MessageModel(
            chat_id=chat_id,
            recent_chat="adsfasdfasdfas World",
            chatusername="abc",
            last_active=datetime.now()
        )