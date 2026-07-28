
## Day 6 — Student API

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
- Fixed by rewriting the file cleanly instead of patching each broken line,
  then confirming with `grep -n "<<<<<<<\|=======\|>>>>>>>" main.py` that no
  markers remained.

### What I learned
- Always check for leftover merge conflict markers after resolving a merge —
  `grep` is a fast way to confirm a file is clean.
- POST returns 201 (created), while PUT and DELETE return 200 (success on an
  existing resource) — the status code communicates *what kind* of success
  happened, not just that it succeeded.