import logging
import datetime
import socket
import ssl
import os
import xml.etree.ElementTree as ET

from certutil import BOT_CERT_PATH, CERT_PATH

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
STALE_DURATION = 5 #StaleOut 5MIN
SENDER_UID = 'taky-bordercar'
SENDER_CALLSIGN = 'Headquarters'

IP = str(os.getenv('IP'))
PORT = 8089

SCRT = CERT_PATH + "/server.crt"
CCRT = BOT_CERT_PATH + "/taky-bordercar.crt"
CKEY = BOT_CERT_PATH + "/taky-bordercar.key"


def sendCoT(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_ssl = ssl.wrap_socket(sock, ca_certs=SCRT, cert_reqs=ssl.CERT_NONE, certfile=CCRT, keyfile=CKEY)

    conn = sock_ssl.connect((IP, PORT))
    sock_ssl.send(message)


def composeCoT(address, callsign):
    logging.basicConfig(format='%(levelname)s:%(threadName)s:%(message)s', level=logging.DEBUG)

    now = datetime.datetime.utcnow()
    start = now.strftime(DATETIME_FORMAT)
    time = now.strftime(DATETIME_FORMAT)
    stale = (now + datetime.timedelta(minutes=STALE_DURATION)).strftime(DATETIME_FORMAT) 

    event = ET.Element('event')
    event.set('version', '2.0')
    event.set('uid', 'UID-{}'.format(callsign))
    event.set('type', 'b-i-v')
    event.set('how', 'm-g')
    event.set('time', time)
    event.set('start', start)
    event.set('stale', stale)

    point = ET.SubElement(event, 'point')
    point.set('le', '9999999.0')
    point.set('ce', '9999999.0')
    point.set('hae', '9999999.0')
    point.set('lat', '0.000000')
    point.set('lon', '0.000000')

    detail = ET.SubElement(event, 'detail')
    
    contact = ET.SubElement(detail, 'contact')
    contact.set('callsign', 'VideoFeed: {}'.format(callsign))

    link = ET.SubElement(event, 'link')
    
    link.set('production_time', time)
    link.set('relationship', 'p-p')
    link.set('uid', 'UID-{}'.format(callsign))
    link.set('parent_callsign', callsign)

    __video = ET.SubElement(detail, '__video')
    __video.set('uid', 'Video-UID-{}'.format(callsign))

    connectionEntry = ET.SubElement(__video, 'ConnectionEntry')
    connectionEntry.set('protocol','rtsp')
    connectionEntry.set('alias','VideoFeed: {}'.format(callsign))
    connectionEntry.set('address', address)
    connectionEntry.set('roverPort','-1')
    connectionEntry.set('rtspReliable','0')
    connectionEntry.set('ignoreEmbeddedKLV','false')
    connectionEntry.set('path','/{}'.format(callsign))
    connectionEntry.set('uid','Video-UID-{}'.format(callsign))
    connectionEntry.set('port','8554')
    connectionEntry.set('bufferTime','-1')
    connectionEntry.set('networkTimeout','0')

    return ET.tostring(event)