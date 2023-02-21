import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO songs (title, artist, album) VALUES (?, ?, ?)", ("The Sound of Silence", "Simon & Garfunkel", "Sounds of Silence"))
cur.execute("INSERT INTO songs (title, artist, album) VALUES (?, ?, ?)", ("The Sound of Silence2", "Simon & Garfunkel", "Sounds of Silence"))

conn.commit()
conn.close()

