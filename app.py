import os
import sqlite3
from flask_wtf.csrf import CSRFProtect


from flask import Flask, render_template, request, send_from_directory, redirect, url_for, abort, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
csrf = CSRFProtect(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/mp3_files/<filename>')
def serve_mp3(filename):
    return send_from_directory('static/mp3_files', filename)

@app.route('/download/<filename>')
def download_file(filename):
    path = 'static/mp3_files/' + filename
    return send_file(path, as_attachment=True)


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
        # check if all fields are filled
        if not request.form['title'] or not request.form['artist'] or not request.form['album']:
            return render_template('create.html', error='Please fill in all fields')
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        print(request.files['file'].filename)
        mfile = request.files['file']
        if mfile:
            # check if song is in mp3 format
            if not mfile.filename.endswith('.mp3'):
                return render_template('create.html', error='File must be in mp3 format')
            filename = mfile.filename
            mfile.save(os.path.join(app.static_folder, 'mp3_files', filename))
            conn = get_db_connection()
            conn.execute('INSERT INTO songs (title, artist, album, filename) VALUES (?, ?, ?, ?)',
                     (title, artist, album, filename))
            conn.commit()
            conn.close()
        
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('create.html')

@app.route('/delete/<song_id>', methods=('GET', 'POST'))
def delete(song_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM songs WHERE id = ?', (song_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        search = request.form['query']
        conn = get_db_connection()
        songs = conn.execute('SELECT * FROM songs WHERE title LIKE ? OR artist LIKE ? OR album LIKE ?',
                             ('%' + search + '%', '%' + search + '%', '%' + search + '%')).fetchall()
        conn.close()
        return render_template('results.html', songs=songs, query=search)
    return render_template('search.html')


@app.route("/")
def index():
    print(app.static_folder)
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    return render_template('index.html', songs=songs)

    