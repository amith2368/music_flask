import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO songs (title, artist, album, filename) VALUES (?, ?, ?, ?)", ("Risk", "StudioKolomna", "Risk", "risk.mp3"))
cur.execute("INSERT INTO songs (title, artist, album, filename) VALUES (?, ?, ?, ?)", ("LifeLike", "AlexiAction", "LifeLike", "lifelike.mp3"))

conn.commit()
conn.close()

