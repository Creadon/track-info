from netdisco.discovery import NetworkDiscovery
from openhomedevice.Device import Device
import json

def ssdpDescription():
    location = ''

    netdis = NetworkDiscovery()
    netdis.scan()

    for dev in netdis.discover():
        data = json.loads(json.dumps(netdis.get_info(dev)))
        if not '\'name\':' in str(data):
            continue
        name = data[0]['name']
        if 'Linn Main Room' == name:
            location = data[0]['ssdp_description']

    netdis.stop()

    if location:
        return location
    else:
        return 'Error'

def trackInfo():
    return json.loads(json.dumps(openhomeDevice.TrackInfo()))

openhomeDevice = Device(ssdpDescription())

