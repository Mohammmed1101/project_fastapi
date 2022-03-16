from fastapi import FastAPI
from typing import Optional,List
from database import engine , localsession ,  Base
from sqlalchemy.orm import Session
import models
from routers import post , user , login


Base.metadata.create_all(bind = engine)



app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(login.router)
db = localsession()
