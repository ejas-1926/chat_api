from fastapi import FastAPI
from Routers.chat_router import router as chat_router
#for debugging
from debugger.inspector import router as inspector_router
from database.database import engine

app = FastAPI()

app.include_router(inspector_router)
app.include_router(chat_router)
