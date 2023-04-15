import logging
import socket
import os
import requests
import json

import cot

import xml.etree.ElementTree as ET

from threading import Thread
from datetime import datetime
from time import sleep
from queue import Queue

STREAM_URL      = os.getenv("STREAM_URL", default="ace-training.airsoftsweden.com")
STREAM_API_PORT = os.getenv("STREAM_API_PORT", default=9997)

TAKY_MON_IP     = os.getenv("TAKY_MON_IP", default="127.0.0.1")
TAKY_MON_PORT   = os.getenv("MON_PORT", default=1337)
LOG_LEVEL       = os.getenv("LOG_LEVEL", default="INFO").upper()

def taky_connect(HOST, PORT):
    return True

def fetch_streams(HOST, PORT, active_streams):
    # active_streams
    logging.info("[+] Producer Thread started, fetching streams...")
        
    URL = "http://{}:{}/v1/paths/list".format(HOST, PORT)
    while (True):
        resp = requests.get(url=URL)
        data = json.loads(resp.text)
        
        for _, streams in data.items():
            for callsign, properties in streams.items():
            
                logging.info("New Stream - Callsign: {}, Source-ID: {}".format(callsign, properties['source']['id']))
                active_streams.put({
                        'callsign': callsign,
                        'stream-id': properties['source']['id']
                        }
                    )
                active_streams.put({'callsign':'test-A10','session-id':'bf59b093-8ad6-498a-b73e-499eb3cf2704'})
        sleep(5)        

def main():
    logging.basicConfig(format='%(levelname)s:%(threadName)s:%(message)s', level=LOG_LEVEL)
    logging.info('Server Started')
    #logging.info(api.fetch_streams(STREAM_URL, STREAM_API_PORT))
    
    streams = Queue()

    taky = taky_connect(TAKY_MON_IP, TAKY_MON_PORT)

    if (taky._connected == True): #Start the consumer of tghe queue
       pass


    logging.info(f"Connected to Taky Monitor Port")
    producer = Thread(target=fetch_streams, args=(STREAM_URL, STREAM_API_PORT, streams))
    producer.start()



    return


if __name__ == '__main__':
    main()