import os
import sqlite3

from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/mp3_files/<filename>')
def serve_mp3(filename):
    return send_from_directory('static/mp3_files', filename)

@app.route('/song/<int:song_id>')
def song(song_id):
    conn = get_db_connection()
    song = conn.execute('SELECT * FROM songs WHERE id = ?', (song_id,)).fetchone()
    conn.close()
    if not song:
        abort(404)
    return render_template('song.html', song=song)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        print(request.files['file'].filename)
        mfile = request.files['file']
        if mfile:
            filename = mfile.filename
            mfile.save(os.path.join(app.static_folder, 'mp3_files', filename))
            conn = get_db_connection()
            conn.execute('INSERT INTO songs (title, artist, album, filename) VALUES (?, ?, ?, ?)',
                     (title, artist, album, filename))
            conn.commit()
            conn.close()
        
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route("/")
def index():
    print(app.static_folder)
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    return render_template('index.html', songs=songs)

    