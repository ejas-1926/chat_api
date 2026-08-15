from fastapi import FastAPI
from Routers.chat_router import router

app = FastAPI()


app.include_router(router)
