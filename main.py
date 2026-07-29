import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine, select

from models import Student

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Student API")


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/students", response_model=list[Student])
def get_students(session: Session = Depends(get_session)):
    return session.exec(select(Student)).all()


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/students", response_model=Student, status_code=201)
def create_student(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@app.put("/students/{student_id}", response_model=Student, status_code=200)
def update_student(student_id: int, updated_student: Student, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = updated_student.name
    student.email = updated_student.email
    student.age = updated_student.age
    student.course = updated_student.course
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@app.delete("/students/{student_id}", status_code=200)
def delete_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"message": f"Student with id {student_id} deleted"}


@app.get("/health")
def health_check():
    return {"status": "ok"}