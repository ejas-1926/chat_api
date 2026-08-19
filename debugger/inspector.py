from sqlalchemy import inspect
from database.database import engine  # import your engine
from fastapi import APIRouter




router = APIRouter()

@router.get("/tables")
def get_all_tables():
    inspector = inspect(engine)
    return {"tables": inspector.get_table_names()}