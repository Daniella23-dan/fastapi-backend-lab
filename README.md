# Student API

A FastAPI project built incrementally over a series of daily challenges — starting from a simple in-memory CRUD API and evolving into a full application with PostgreSQL persistence and JWT authentication.

## Features

- Full CRUD for student records (GET, POST, PUT, DELETE)
- Input validation via Pydantic/SQLModel (positive age, valid email format)
- PostgreSQL database persistence via SQLModel
- User registration and login with bcrypt password hashing
- JWT-based authentication protecting write access to student data

## Tech Stack

- **FastAPI** — web framework
- **SQLModel** — ORM combining Pydantic validation + SQLAlchemy tables
- **PostgreSQL** — database
- **Passlib (bcrypt)** — password hashing
- **python-jose** — JWT creation and verification

## Setup

```bash
git clone <your-repo-url>
cd student-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Built a simple FastAPI project to practice Pydantic models, routing, and input validation.

### What I built
- Pydantic `Student` model (id, name, email, age, course)
- In-memory list of mock students
- Routes: `GET /students`, `GET /students/{id}`, `POST /students`
- Input validation: age must be positive, email must be valid format

### Challenges
- Kept running into `ModuleNotFoundError` because files created via terminal editors weren't landing in the right folder — VS Code's file explorer and my terminal were pointed at different directories.
- Copy-pasting code into the terminal sometimes split single lines across two lines (e.g. an import statement got broken mid-line), causing `SyntaxError`.
- Fixed both by using `code <filename>` from the terminal to guarantee the file being edited was the exact one in my current folder, then pasting cleanly in the VS Code editor instead of the terminal.

### What I learned
- Always confirm `pwd` and `ls` match what you expect before debugging code — sometimes the bug isn't the code, it's the location.
- FastAPI + Pydantic validation happens automatically — invalid input never even reaches your route function.
=======
# Student API
   A simple FastAPI application with basic routes.


## Setup

1. Create and activate a virtual environment:
'''
   bash
python3 -m venv venv 
source venv/bin/activate

## API Docs
![API docs screenshot](docs-screenshot.png)
>>>>>>> 45f6176137f0718c51df930150da1b78d76afd04


## Day 6 — Read Operations (Pydantic Models & Path Parameters)

Built the foundational Student API with in-memory mock data, basic CRUD-read routes, and input validation.

### What I built
- `Student` Pydantic model with fields: id, name, email, age, course
- A list of mock students held in memory (no database yet)
- `GET /students` — returns all students
- `GET /students/{id}` — returns one student, or a 404 if the ID doesn't exist
- `POST /students` — accepts a student body and adds it to the in-memory list
- Input validation: age must be a positive integer, email must be a valid format

### Challenges
- Ran into repeated `ModuleNotFoundError` and `SyntaxError` issues early on because files were being created in the wrong folder, or terminal copy-paste split single lines of code across two lines.
- Fixed by consistently checking `pwd`/`ls` before troubleshooting code, and by opening files directly with `code <filename>` from the terminal to guarantee I was editing the file that actually lived in my project folder.

### What I learned
- Pydantic validates incoming data automatically — invalid input (like a negative age or a malformed email) is rejected with a `422` before it ever reaches my route logic.
- FastAPI's `/docs` page is generated directly from the Pydantic model, so accurate field types up front save debugging time later.
- A location mismatch between terminal and editor is one of the most common (and confusing) sources of "file not found" errors — always confirm both are pointed at the same folder.


## Day 7 — Update & Delete (CRUD Complete)


Extended the Student API with full CRUD support and proper HTTP status codes.

### What I built
- `PUT /students/{id}` — updates an existing student, returns 200 with updated record
- `DELETE /students/{id}` — removes a student, returns 200 with a confirmation message
- Both routes return 404 with a clear message if the student ID doesn't exist

### Challenges
- A merge conflict from an earlier GitHub sync left leftover conflict markers
  (`=======`, `>>>>>>>`) inside `main.py`, along with duplicated/broken code
  (typos like `respoense_model`, a second `FastAPI()` instance). This caused

  a `SyntaxError` on startup.
