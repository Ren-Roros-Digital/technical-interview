# technical-interview

A simple FastAPI project that lists users with a styled front-end using Tailwind CSS.

## Prerequisites

- Python >= 3.12
- uv (Python package manager):
  ```
  pip install uv
  ```

## Installation (using uv)

1. Create a virtual environment for the project (optional but recommended):
   ```
   uv venv create
   uv venv use
   ```
2. Sync the project dependencies:
   ```
   uv sync
   ```

Alternatively, if you need to add dependencies:
```
uv add fastapi[standard] uvicorn[standard]
uv sync
```

## Running the Server

Start the development server with uv:
```
uv run fastapi dev
```

Open your browser at http://127.0.0.1:8000 to view the user list.

## API

- GET /api/users: Returns the list of users in JSON format.
