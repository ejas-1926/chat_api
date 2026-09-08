from fastapi import APIRouter,Depends
from models.usermode import UserModel
from sqlalchemy.orm import Session
from uuid import UUID
from database.database import get_db
from Service.userinfo_service import UserInfoService

router = APIRouter()
service = UserInfoService()

@router.get("/userinfo",response_model=UserModel)
def get_messages(user_id: UUID, db: Session = Depends(get_db)):
    return service.getUserInfo(user_id=user_id,db=db)