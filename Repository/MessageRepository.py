from sqlalchemy import text
from sqlalchemy.orm import Session

from uuid import UUID

from models.messagemodel import MessageModel


class MessageRepository:

    def get_messages(self, db: Session, user_id: UUID):

        chats: list[MessageModel] = []

        query = text("""
            SELECT *
            FROM getmessagesfromchat(:user_id)


        """)

        result = db.execute(
            query,

            {"user_id": user_id}
        )

        rows = result.fetchall()
       

        for row in rows:

            model = MessageModel(
                message_id=row.message_id,
                sender_id=row.sender_id,
                chat_id=row.chat_id,
                content= row.content,
               
                
            )
            print(f"Row type: {type(row)}")
            print(f"Row mappings and values: {row._mapping}")  # ← PARENTHESES ADDED HERE
            #print(f"Row as dictionary: {dict(row)}")

            chats.append(model)

        return chats

