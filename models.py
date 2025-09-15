from enum import Enum
from sqlalchemy import (
    Column,Integer,String,CheckConstraint,Text,Enum as SEnum
)
from database import BASE

class Genre(str,Enum):
    fantasy = "fantasy"
    dramma = "dramma"
    romance = "romance"

class Book(BASE):
    __tablename__ = "books"

    booK_id = Column('id',Integer,primary_key=True,nullable=False,index=True)
    title = Column(String(length=30),nullable=False)
    author = Column(String(length=30),nullable=False)
    pages = Column(Integer,CheckConstraint("pages>=1"),nullable=False)  # bu chek qilish
    description = Column(Text)
    genre = Column(SEnum(Genre))