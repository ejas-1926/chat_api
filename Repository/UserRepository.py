from sqlalchemy import text
from sqlalchemy.orm import Session
from uuid import UUID
from models.usermodel import UserModel


class UserRepository:

    def get_user_info(self, db: Session, user_id: UUID):

        messages:list[UserModel] = []

        query = text("""
            SELECT *
            FROM get_user_info(:user_id)


        """)

        result = db.execute(
            query,

            {"user_id": user_id}
        )

        rows = result.fetchall()
       

        for row in rows:

            model = UserModel(
                user_id=row.user_id,
                about=row.about,
                mobile_no= row.mobile_no,
                user_name=row.user_name,
                last_seen=(
                                    row.last_seen.strftime("%Y-%m-%d %H:%M:%S")
                                    if row.last_seen is not None
                                    else None
                                )
               
                
            )
            print(model)
            messages.append(model)
        print('leaving repository with messages')
        return messages

