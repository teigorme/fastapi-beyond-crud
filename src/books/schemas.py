from pydantic import BaseModel
from datetime import datetime
import uuid


# Format data for response and request
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


# Validation data
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
