from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class UserData(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    message: str
    data: UserData

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
