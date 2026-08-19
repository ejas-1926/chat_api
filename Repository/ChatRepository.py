from sqlalchemy import text
from sqlalchemy.orm import Session

class UserRepository:

    def create_user(self, db: Session, name: str, email: str):

        query = text("""
            SELECT * FROM create_user(
                :name,
                :email
            )
        """)

        result = db.execute(
            query,
            {
                "name": name,
                "email": email
            }
        )

        return result.fetchone()