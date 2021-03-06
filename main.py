from netdisco.discovery import NetworkDiscovery
from openhomedevice.Device import Device
from flask import Flask, render_template, request
import json

#Device

def ssdpDescription():
    netdis = NetworkDiscovery()
    netdis.scan()

    for dev in netdis.discover():
        data = json.loads(json.dumps(netdis.get_info(dev)))
        if not '\'name\':' in str(data):
            continue
        name = data[0]['name']
        if 'Linn Main Room' == name:
            netdis.stop()
            return data[0]['ssdp_description']

    netdis.stop()
    return 'Error'

def trackInfo():
    return json.loads(json.dumps(openhomeDevice.TrackInfo()))

openhomeDevice = Device(ssdpDescription())

#Server

app = Flask(__name__)

@app.route('/')
def appPage():
    return render_template('index.html')

@app.route('/title')
def title():
    return trackInfo()['title']

@app.route('/artist')
def artist():
    artistsRaw = json.dumps(trackInfo()['artist'])
    artistsRaw = artistsRaw[1:-1]
    artistsRaw = artistsRaw.split(', ')
    artistList = ''
    for artist in artistsRaw:
        artist = artist[1:-1]
        artistList += artist + ', '
    artistList = artistList[0:-2]
    return artistList

@app.route('/album')
def album():
    return trackInfo()['albumTitle']

@app.route('/artwork')
def artwork():
    return trackInfo()['albumArtwork']

if __name__ == '__main__':
    app.run()