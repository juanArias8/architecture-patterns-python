from fastapi import FastAPI

from api.user_api import router as UserRouter
from models.common import Response

app = FastAPI()

app.include_router(UserRouter, tags=["auth"], prefix="/user")


@app.get("/")
async def root():
    return Response(message="Hellow from server")
