from models.chatmodel import ChatModel
from datetime import datetime


class ChatService:

    def get_chat(self, chat_id: int):

        return ChatModel(
            chat_id=chat_id,
            recent_chat="adsfasdfasdfas World",
            chatusername="abc",
            last_active=datetime.now()
        )