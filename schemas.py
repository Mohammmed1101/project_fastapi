import datetime
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    id : Optional[int]
    title : str
    description : str
    image_url : str
    create_at : datetime.datetime
    owner_id : int

    class Config:
        orm_mode = True

class User(BaseModel):
    id : Optional[int]
    username:str
    email:str
    password:str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    email: Optional[str] = None