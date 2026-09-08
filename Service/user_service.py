from models.messagemodel import MessageModel
from datetime import datetime
from Repository.UserRepository import UserRepository
from sqlalchemy.orm import Session
from uuid import UUID

repo = UserRepository()
class UserService:

    def get_userinfo(self, user_id: UUID, db: Session):
        print('reached service')
        model = repo.get_user_info(db=db, user_id=user_id)
        print('left service')
        return model