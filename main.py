from flask import Flask, render_template
from track import trackInfo

app = Flask(__name__)

@app.route('/app')
def appPage():
    data = trackInfo()
    return render_template('app.html', 
        tabTitle = 'What\'s playing?',
        art = data['albumArtwork'],
        track = data['title'],
        artist = data['artist'], 
        album = data['albumTitle'])

@app.route('/settings')
def settingsPage():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run()