import sqlite3
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/mp3_files/<filename>')
def serve_mp3(filename):
    return send_from_directory('static/mp3_files', filename)

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

@app.route("/")
def index():
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    return render_template('index.html', songs=songs)

    