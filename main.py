import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session, create_engine, select

from models import Student, User, UserRegister, UserLogin
from auth import hash_password, verify_password, create_access_token, get_current_username

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Student API")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"],
allow_credentials=True, allow_methods=["*"],
allow_headers=["*"],)


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


# ---------- Auth routes ----------

@app.post("/auth/register", status_code=201)
def register(user_data: UserRegister, session: Session = Depends(get_session)):
    existing = session.exec(
        select(User).where(
            (User.username == user_data.username) | (User.email == user_data.email)
        )
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User registered successfully", "username": new_user.username}


@app.post("/auth/login")
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == user_data.username)).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# ---------- Student routes ----------

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
def create_student(
    student: Student,
    session: Session = Depends(get_session),
    current_username: str = Depends(get_current_username),
):
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
