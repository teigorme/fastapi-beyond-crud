from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


# use params
@app.get("/greet/{name}")
async def greet_name(name: str):
    return {"name": name}


# use query
# greet-name?name=Igor&age=22
@app.get("/greet-name")
async def greets_name(name: str = "Python", age: int = 0):
    return {"name": name, "age": age}


# create object dto
class BookCreateModel(BaseModel):
    title: str
    author: str


# use post routes and create json schema
@app.post("/create-book", status_code=201)
async def create_book(book_data: BookCreateModel):
    return book_data
