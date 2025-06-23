# technical-interview

A simple FastAPI project that lists users with a styled front-end using Tailwind CSS.

## Prerequisites

- Python >= 3.12
- uv (Python package manager). Install via one of:
  - pip:
    ```
    pip install uv
    ```
  - Homebrew (macOS):
    ```
    brew install uv
    ```
  - Install script:
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

## Installation (using uv)

1. Sync the project dependencies (creates and activates a virtual environment automatically):
   ```bash
   uv sync
   ```

## Database Setup

After syncing dependencies, initialize the SQLite database and populate it with users:
```bash
python init_db.py
```
This creates `data/users.db` and imports entries from `data/users.json`.


## Running the Server

Start the development server with uv:
```
uv run fastapi dev
```

Open your browser at http://127.0.0.1:8000 to view the user list.

## API

- GET /api/users: Returns the list of users in JSON format.

## Data

User data is loaded from `data/users.json`. Edit this file to add, remove, or modify users.
