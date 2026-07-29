from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    age: int = Field(gt=0, description="Age must be a positive integer")
    course: str