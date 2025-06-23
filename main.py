from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")
db_file = Path(__file__).parent / "data" / "users.db"


@app.get("/api/users")
async def get_users():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, email FROM users ORDER BY id")
    rows = cur.fetchall()
    users_list = [dict(row) for row in rows]
    conn.close()
    return users_list


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
