import sqlite3
import client
from client import register
import os
import client

main_dir = os.path.dirname(os.path.abspath(__file__))
database_dir = os.path.join(main_dir, "Database")
auth_db_location = os.path.join(database_dir, "authentication.db")

conn = sqlite3.connect(auth_db_location)
cursor = conn.cursor()

def Create_Table():
    pass