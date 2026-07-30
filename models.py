from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    age: int = Field(gt=0, description="Age must be a positive integer")
    course: str


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    hashed_password: str


class UserRegister(SQLModel):
    """What the client sends when registering — plain password, not stored directly."""
    username: str
    email: EmailStr
    password: str

class UserLogin(SQLModel):
    """What the client sends when logging in."""
    username: str
    password: str