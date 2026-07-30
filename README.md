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

 ## Day 9 — Authentication (Password Hashing + JWT)

Added user registration and login, with bcrypt password hashing and JWT-protected routes.

### What I built
- `User` table (id, username, email, hashed_password) — passwords are never stored in plain text
- `POST /auth/register` — hashes the password with bcrypt, rejects duplicate usernames/emails (400)
- `POST /auth/login` — verifies the submitted password against the stored hash, returns a JWT on success, 401 on failure
- `POST /students` is now protected — requires a valid Bearer token, otherwise returns 401
- Tested the full flow both through Swagger UI (`/docs`) and via curl with a real Authorization header

### Challenges
- Confused the `/students` and `/auth/register` endpoints at first while testing — an easy mix-up since Swagger lists all routes together.
- Pasted the JWT into Swagger's Authorize field with quotes around it by mistake, which caused a 422; removing the quotes fixed it.
- Hit "Couldn't connect to server" errors when testing via curl because uvicorn wasn't actually running in a separate terminal tab at the time.
- Learned that JWTs are long (100+ characters) — using a shortened/truncated token instead of the full string causes decode failures.

### What I learned
- Never store plain-text passwords — bcrypt hashes are one-way, so even the server can't "recover" the original password, only verify a match.
- A JWT carries a signed payload (like the username) that the server can trust without a database lookup on every request, as long as the signature checks out.
- Running the API server and testing with curl requires two separate terminal sessions — one to keep the server alive, one to send requests.

