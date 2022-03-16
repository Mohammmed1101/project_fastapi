from datetime import datetime
from database import Base
from sqlalchemy import Column, Integer , Text ,DateTime,String , ForeignKey
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer , primary_key=True ,index=True)
    title = Column(String(50) , index=True)
    description = Column(Text)
    image_url = Column(URLType)
    create_at = Column(DateTime , default=datetime.now())
    owner_id = Column(Integer , ForeignKey("users.id"))
    owner = relationship("User" , back_populates="posts")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String , index=True)
    email = Column(String , index=True)
    password = Column(String)
    posts = relationship("Post" , back_populates="owner")