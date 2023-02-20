from datetime import datetime

from pydantic import BaseModel, validator, EmailStr


class UserBase(BaseModel):
    username: EmailStr
    name: str

    class Config:
        orm_mode = True


class UserList(UserBase):
    created_at: datetime


class UserDetail(UserBase):
    created_at: datetime


class UserCreateComplete(BaseModel):
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
    email: EmailStr
