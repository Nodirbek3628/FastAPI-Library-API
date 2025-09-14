from fastapi import FastAPI

app = FastAPI(title="NT practe")



@app.get("/")
async def root():
    return {
        "Name":"Qalaysan ali"
    }