from sqlalchemy import text
from sqlalchemy.orm import Session

from uuid import UUID

from models.messagemodel import MessageModel


class MessageRepository:

    def get_messages(self, db: Session, chat_id: int):

        messages:list[MessageModel] = []

        query = text("""
            SELECT *
            FROM get_chat_messages(:chat_id)


        """)

        result = db.execute(
            query,

            {"chat_id": chat_id}
        )

        rows = result.fetchall()
       

        for row in rows:

            model = MessageModel(
                message_id=row.message_id,
                sender_id=row.sender_id,
                content= row.content,
                display_Name=row.display_name,
                message_sent=(
                                    row.created_at.strftime("%Y-%m-%d %H:%M:%S")
                                    if row.created_at is not None
                                    else None
                                )
               
                
            )
            print(model)
            messages.append(model)
        print('leaving repository with messages')
        return messages

