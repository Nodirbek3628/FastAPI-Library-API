from fastapi import FastAPI,Path

app = FastAPI(title="NT practe")



@app.get("/book/api/{book_id}")
async def get_book(book_id: int = Path(gt=0,lt=100)):
    return {
        "book":book_id
    }