from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str = None
    bio: str = None
    avatar: str = None
