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


@app.put("/students/{student_id}", response_model=Student, status_code=200)
def update_student(student_id: int, updated_student: Student):
    for index, s in enumerate(students):
        if s.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}", status_code=200)
def delete_student(student_id: int):
    for index, s in enumerate(students):
        if s.id == student_id:
            students.pop(index)
            return {"message": f"Student with id {student_id} deleted"}
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/health")
def health_check():
    return {"status": "ok"}