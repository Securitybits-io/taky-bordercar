import logging
import datetime
import xml.etree.ElementTree as ET

'''
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<event version="2.0" uid="Unique-uid-{{ callsign }}" type="b-m-p-s-p-loc" how="h-g-i-g-o" time="{{ global.starttime }}" start="{{ global.starttime }}" stale="{{ global.staletime }}">
  <point lat="{{ payload.lat }}" lon="{{ payload.lon }}" hae="{{ payload.hae }}" ce="{{ payload.ce }}" le="{{ payload.le }}" />
  <detail>
    <contact callsign="{{ callsign }}-stream" />
    <link type="a-f-G-U-C-I" uid="ASN-TAK-BOT-FAKE-UID" parent_callsign="ASN-TAK-BOT" relation="p-p" production_time="{{ global.starttime }}" />
    <sensor fov="45" fovBlue="1" displayMagneticReference="0" range="100" fovGreen="1" fovAlpha="0" hideFov="true" fovRed="1" azimuth="270" />
    <remarks />
    <__video uid="Video-UID-{{ callsign }}">
      <ConnectionEntry protocol="rtsp" path="/{{ callsign }}" address="{{global.ip}}" port="8554" uid="Video-UID-{{ callsign }}" alias="{{ callsign }}" roverPort="-1" rtspReliable="0" ignoreEmbeddedKLV="False" networkTimeout="0" bufferTime="-1" />
    </__video>
  </detail>
</event>


<event version="2.0" uid="dbc84ae2-937c-4d6f-b6d5-d5278d38b734" type="b-i-v" how="m-g" time="2023-04-15T14:33:56.271Z" start="2023-04-15T14:33:56.271Z" stale="2023-04-15T15:33:56.271Z">
  <point lat="0.000000" lon="0.000000" hae="9999999.0" ce="9999999.0" le="9999999.0"/>
  <detail>
    <contact callsign="Dronefeed ODA-A10"/>
    <link production_time="2023-04-15T14:33:56.271Z" relationship="p-p" uid="dbc84ae2-937c-4d6f-b6d5-d5278d38b734" parent_callsign="ODA-A10-BS"/>
    <__video>
      <ConnectionEntry protocol="rtsp" alias="Dronefeed ODA-A10" address="ace-training.airsoftsweden.com" roverPort="-1" rtspReliable="0" ignoreEmbeddedKLV="false" path="/ODA-A10" uid="dbc84ae2-937c-4d6f-b6d5-d5278d38b734" port="1935" bufferTime="-1" networkTimeout="12000"/>
    </__video>
  </detail>
</event>

'''

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
STALE_DURATION = 5 #StaleOut 5MIN
SENDER_UID = 'taky-bordercar'
SENDER_CALLSIGN = 'Headquarters'

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