import json
import requests

active_streams = []

def fetch_streams(HOST, PORT):
  URL = "http://{}:{}/v1/paths/list".format(HOST, PORT)
  resp = requests.get(url=URL)
  data = json.loads(resp.text)
  
  for stream in data.items():
     print(stream)

  return json.dumps(data, indent=4)


def parse_streams():
    return