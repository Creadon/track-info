from flask import Flask, render_template
from track import trackInfo

app = Flask(__name__)

@app.route('/')
def appPage():
    data = trackInfo()
    return render_template('index.html',
        art = data['albumArtwork'],
        track = data['title'],
        artist = data['artist'], 
        album = data['albumTitle'])

if __name__ == '__main__':
    app.run()