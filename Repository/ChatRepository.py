from sqlalchemy import text
from sqlalchemy.orm import Session

from uuid import UUID

from models.chatmodel import ChatModel


class ChatRepository:

    def get_chats(self, db: Session, user_id: UUID):

        chats: list[ChatModel] = []

        query = text("""
            SELECT *
            FROM getuserchats(:user_id)


        """)

        result = db.execute(
            query,

            {"user_id": user_id}
        )

        rows = result.fetchall()
        print(type(rows[0].last_seen))

        for row in rows:

            model = ChatModel(
                user_id=row.user_id,
                chat_id = row.chat_id,
                recent_chat=row.content,
                chatusername=row.name,
                last_active=(
                    row.last_seen.strftime("%Y-%m-%d %H:%M:%S")
                    if row.last_seen is not None
                    else None
                )
            )
            print(f"Row type: {type(row)}")
            print(f"Row mappings and values: {row._mapping}")  # ← PARENTHESES ADDED HERE
            #print(f"Row as dictionary: {dict(row)}")

            chats.append(model)

        return chats

