import sqlite3

with sqlite3.connect('saves.db') as db:
    cursor = db.cursor()
    query = """ DELETE FROM saveddots """
    cursor.execute(query)
