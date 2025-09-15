from enum import Enum
from typing import Annotated
from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field


app = FastAPI(title="NT practe")



@app.get("/api/book/{book_id}")
async def get_book(
    book_id:Annotated[int,Path(title='bitta kitob id si',gt=1,lt=100)]

):
    return {
        "book":book_id
    }

@app.get("/api/users/{message}")
async def get_message(message: str = Path(min_length=3,max_length=10, pattern='^[a-zA-Z0-9_-]{3,15}$')):
    return {
        "users":message
    }

@app.get("/api/books")
async def get_book_list(
    author: Annotated[str, Query(title = 'Kitob muallifi',min_length=2,max_length=100)]
    ):
    return {
        "author":author
    }

class Genre(str,Enum):
    fantasy = "fantasy"
    dramma = "dramma"
    romance = "romance"
  

class Book(BaseModel):
    title:Annotated[str,Field(title="kitob nomi",min_length=5,max_length=30)]
    author:Annotated[str,Field(title="kitob muallifi",min_length=5,max_length=30)]
    pages:Annotated[int,Field(title="varoqlar soni",gt=5,lt=30)]
    description:str | None = Field(default=None,title='Tarif', )    #Ixtiyoriy
    genre:Genre

@app.post("/api/books/")
async def post_book(
    book:Book

):
    print(book.model_dump())
    return {"book": book}