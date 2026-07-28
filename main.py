<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from models import Student

app = FastAPI(title="Student API")

students: list[Student] = [
    Student(id=1, name="Angel Dani", age=20, email="angel@example.com", course="Economics"),
    Student(id=2, name="Susan Peters", age=25, email="susan@example.com", course="Geography"),
    Student(id=3, name="Carine Joy", age=18, email="carine@example.com", course="Physics"),
]


@app.get("/students", response_model=list[Student])
def get_students():
    return students


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for s in students:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", response_model=Student, status_code=201)
def create_student(student: Student):
    students.append(student)
    return student
=======
 from fastapi import FASTAPI

app = FastAPI()


@app.get("/")
def read_root():
   return {"meassage": "Welcome to the Student API"}



@app.get("/health")
def health_check():
     return {"status": "ok"}
>>>>>>> 45f6176137f0718c51df930150da1b78d76afd04
