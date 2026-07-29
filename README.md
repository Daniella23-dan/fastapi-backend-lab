
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



  ## Day 8 — Database Integration (PostgreSQL + SQLModel)

Replaced the in-memory mock data with a real PostgreSQL database, so data now persists across server restarts.

### What I built
- Installed PostgreSQL locally and created a `student_api` database with a dedicated user
- Redefined `Student` as a SQLModel table (combines Pydantic validation with a real database table)
- Added a database engine and session dependency, injected into each route
- Updated all five routes (GET all, GET one, POST, PUT, DELETE) to read/write from PostgreSQL instead of a Python list
- Stored the database connection string in `.env`, loaded via `python-dotenv`, and excluded from GitHub via `.gitignore`

### Challenges
- Accidentally created `.env` and `requirements.txt` files outside the project folder before realizing the terminal wasn't `cd`'d into `student-api`.
- Had two virtual environments (`venv` and `.venv`) after a mixed setup; confirmed the active one with `which python` before removing the unused one.
- Hit a `permission denied for schema public` error when SQLModel tried to create the table — PostgreSQL 15+ restricts schema permissions by default. Fixed by explicitly granting schema privileges to the database user.
- Pasted the wrong file contents into `models.py` and `main.py` at one point, causing a circular import; fixed by rewriting each file with only its intended content.
- Discovered `.venv` (an old, unused virtual environment) had been accidentally committed to git early on. Removed it from tracking as part of this update.

### What I learned
- SQLModel combines a Pydantic model and a SQLAlchemy table definition in one class — no need to maintain them separately.
- FastAPI's dependency injection (`Depends(get_session)`) hands each route a fresh database session automatically.
- Restarting the server and confirming data survives is the real test that a database (not memory) is being used.
- Never commit `venv`/`.venv` folders or `.env` files — `.gitignore` should be set up *before* the first commit, not after.