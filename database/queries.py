from uuid import UUID
from sqlalchemy import text

def getuserquery(user_id:UUID):
    query =  text("SELECT * FROM users WHERE userid = :user_id")
    return query,{"user_id":user_id}