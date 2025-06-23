#!/usr/bin/env python3
"""
Initialize the SQLite database and populate it with users from data/users.json
"""
import sqlite3
import json
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "users.db"
JSON_PATH = DATA_DIR / "users.json"

def init_db():
    # Ensure data directory exists
    DATA_DIR.mkdir(exist_ok=True)
    # Connect to SQLite (creates file if not exists)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Drop existing users table and create with first_name and last_name
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute(
        '''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL
        )
        '''
    )
    # Load users from JSON and split names
    with JSON_PATH.open('r') as f:
        users = json.load(f)
    records = []
    for u in users:
        full = u.get('name', '').strip()
        parts = full.split()
        if len(parts) > 1:
            first = ' '.join(parts[:-1])
            last = parts[-1]
        else:
            first = parts[0] if parts else ''
            last = ''
        records.append((u['id'], first, last, u['email']))
    # Insert or replace users
    cur.executemany(
        'INSERT OR REPLACE INTO users (id, first_name, last_name, email) VALUES (?, ?, ?, ?)',
        records
    )
    conn.commit()
    conn.close()
    print(f"Initialized database at {DB_PATH} with {len(users)} users.")

if __name__ == '__main__':
    init_db()