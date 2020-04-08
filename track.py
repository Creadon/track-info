from netdisco.discovery import NetworkDiscovery
from openhomedevice.Device import Device
import json

def ssdpDescription():

    netdis = NetworkDiscovery()
    netdis.scan()

    for dev in netdis.discover():
        data = json.loads(json.dumps(netdis.get_info(dev)))
        if not '\'name\':' in str(data):
            continue
        name = data[0]['name']
        if 'Linn Main Room' == name:
            netdis.stop();
            return data[0]['ssdp_description']

    netdis.stop()
    return 'Error'

def trackInfo():
    return json.loads(json.dumps(openhomeDevice.TrackInfo()))

openhomeDevice = Device(ssdpDescription())