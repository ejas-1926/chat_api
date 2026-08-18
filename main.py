from fastapi import FastAPI
from Routers.chat_router import router
from database.database import engine

app = FastAPI()


app.include_router(router)
