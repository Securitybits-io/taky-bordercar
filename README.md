# taky-bordercar

example COT:
```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<event version="2.0" uid="Unique-uid-{{ callsign }}" type="b-m-p-s-p-loc" how="h-g-i-g-o" time="{{ global.starttime }}" start="{{ global.starttime }}" stale="{{ global.staletime }}">
  <point lat="{{ payload.lat }}" lon="{{ payload.lon }}" hae="{{ payload.hae }}" ce="{{ payload.ce }}" le="{{ payload.le }}" />
  <detail>
    <contact callsign="{{ callsign }}-stream" />
    <link type="a-f-G-U-C-I" uid="ASS-TAK-BOT-FAKE-UID" parent_callsign="ASS-TAK-BOT" relation="p-p" production_time="{{ global.starttime }}" />
    <archive />
    <sensor fov="45" fovBlue="1" displayMagneticReference="0" range="100" fovGreen="1" fovAlpha="0" hideFov="true" fovRed="1" azimuth="270" />
    <remarks />
    <__video uid="Video-UID-{{ callsign }}">
      <ConnectionEntry protocol="rtsp" path="/{{ callsign }}" address="{{global.ip}}" port="8554" uid="Video-UID-{{ callsign }}" alias="{{ callsign }}" roverPort="-1" rtspReliable="0" ignoreEmbeddedKLV="False" networkTimeout="0" bufferTime="-1" />
    </__video>
  </detail>
</event>
```

example stream object:
```json
{
    "items": {
        "ODA-A10-BS": {
            "confName": "~^.*$",
            "conf": {
                "source": "publisher",
                "sourceProtocol": "automatic",
                "sourceAnyPortEnable": false,
                "sourceFingerprint": "",
                "sourceOnDemand": false,
                "sourceOnDemandStartTimeout": "10s",
                "sourceOnDemandCloseAfter": "10s",
                "sourceRedirect": "",
                "disablePublisherOverride": false,
                "fallback": "",
                "rpiCameraCamID": 0,
                "rpiCameraWidth": 1920,
                "rpiCameraHeight": 1080,
                "rpiCameraHFlip": false,
                "rpiCameraVFlip": false,
                "rpiCameraBrightness": 0,
                "rpiCameraContrast": 1,
                "rpiCameraSaturation": 1,
                "rpiCameraSharpness": 1,
                "rpiCameraExposure": "normal",
                "rpiCameraAWB": "auto",
                "rpiCameraDenoise": "off",
                "rpiCameraShutter": 0,
                "rpiCameraMetering": "centre",
                "rpiCameraGain": 0,
                "rpiCameraEV": 0,
                "rpiCameraROI": "",
                "rpiCameraTuningFile": "",
                "rpiCameraMode": "",
                "rpiCameraFPS": 30,
                "rpiCameraIDRPeriod": 60,
                "rpiCameraBitrate": 1000000,
                "rpiCameraProfile": "main",
                "rpiCameraLevel": "4.1",
                "rpiCameraAfMode": "auto",
                "rpiCameraAfRange": "normal",
                "rpiCameraAfSpeed": "normal",
                "rpiCameraLensPosition": 0,
                "rpiCameraAfWindow": "",
                "rpiCameraTextOverlayEnable": false,
                "rpiCameraTextOverlay": "",
                "publishUser": "",
                "publishPass": "",
                "publishIPs": [],
                "readUser": "",
                "readPass": "",
                "readIPs": [],
                "runOnInit": "",
                "runOnInitRestart": false,
                "runOnDemand": "",
                "runOnDemandRestart": false,
                "runOnDemandStartTimeout": "10s",
                "runOnDemandCloseAfter": "10s",
                "runOnReady": "",
                "runOnReadyRestart": false,
                "runOnRead": "",
                "runOnReadRestart": false
            },
            "source": {
                "type": "rtmpConn",
                "id": "36e77a5b-622d-479b-99ab-b5aa1051b040"
            },
            "sourceReady": true,
            "tracks": [
                "H264",
                "MPEG4-audio-gen"
            ],
            "bytesReceived": 25830215,
            "readers": []
        }
    }
}
```