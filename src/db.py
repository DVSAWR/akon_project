import os
import sqlite3

DATABASE = "akontech.db"


def initialize_db() -> None:
    """Initialize SQLite DB with init.sql."""
    init_file = os.path.join(os.path.dirname(__file__), "init.sql")
    with open(init_file, "r") as file:
        sql_script = file.read()

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()


def get_connection():
    """Get connection to SQLite"""
    return sqlite3.connect(DATABASE)
