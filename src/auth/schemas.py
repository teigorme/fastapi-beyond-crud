import uuid
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class UserCreateModel(BaseModel):
    username: str = Field(..., max_length=50)
    first_name: str = Field(..., max_length=180)
    last_name: str = Field(..., max_length=128)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6, max_length=32)


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    password_hash: str = Field(exclude=True)
    is_verified: bool
    created_at: datetime
    updated_at: datetime
