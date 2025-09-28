from pydantic import BaseModel


# Format data for response and request
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# Validation data
class UpdateBookModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
