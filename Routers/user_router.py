from fastapi import APIRouter,Depends;
from uuid import UUID
from Service.messaging_service import MessagingService
from models.usermodel import UserModel
from database.database import get_db

from sqlalchemy.orm import Session

router = APIRouter()

service = MessagingService()

@router.get("/users/{messageid}",response_model=list[UserModel])
def get_messages(messageid: int, db: Session = Depends(get_db)):
    model = service.get_messages(chat_id=messageid, db=db)
    return model