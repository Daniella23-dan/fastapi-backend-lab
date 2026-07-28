
## Day 7 — Student API

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
