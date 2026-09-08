from uuid import UUID
from Repository.UserRepository import UserRepository
from sqlalchemy.orm import Session

repository = UserRepository()

class UserInfoService:

    def getUserInfo(self,user_id: UUID,db:Session):
        return repository.getUserInfo(user_id=user_id,db=db)