from flask import Flask, render_template, request
from track import trackInfo
import json

app = Flask(__name__)

@app.route('/')
def appPage():
    return render_template('index.html')

@app.route('/title')
def title():
    return trackInfo()['title']

@app.route('/artist') #TODO clean up returned list
def artist():
    return json.dumps(trackInfo()['artist'])

@app.route('/album')
def album():
    return trackInfo()['albumTitle']

@app.route('/artwork')
def artwork():
    return trackInfo()['albumArtwork']

if __name__ == '__main__':
    app.run()