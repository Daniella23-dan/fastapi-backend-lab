from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int = Field(gt=0, description="Age must be a positive integer")
    course: str