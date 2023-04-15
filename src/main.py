import logging
import socket
import os
import requests
import json
import certutil

import cot

from threading import Thread
from time import sleep
from queue import Queue


STREAM_URL      = os.getenv("STREAM_URL", default="127.0.0.1")
STREAM_API_PORT = os.getenv("STREAM_API_PORT", default=9997)

CERT_PASS       = os.getenv('CERT_PASS')
LOG_LEVEL       = os.getenv("LOG_LEVEL", default="INFO").upper()
TAKY_IP         = os.getenv('IP')


def init_certs(cert_password):
    logging.info("Creating TAKY-BORDERCAR Certs")
    certutil.build_certs(cert_password)
    return


def send_stream(certpass, streams):
    logging.info(f"[+] Consumer Thread started, waiting on Active Streams...")
    while(True):
        if streams.empty():
            pass
        else:
            stream = streams.get()
            message = cot.composeCoT(STREAM_URL, stream['callsign'])
            try:
                cot.sendCoT(message)
            except:
                logging.error(message)
            
            sleep(0.5)


def fetch_streams(HOST, PORT, active_streams):
    # active_streams
    logging.info("[+] Producer Thread started, fetching streams...")
        
    URL = "http://{}:{}/v1/paths/list".format(HOST, PORT)
    while (True):
        resp = requests.get(url=URL)
        if resp.status_code == 200:
            data = json.loads(resp.text)
            
            for _, streams in data.items():
                for callsign, properties in streams.items():
                
                    logging.info("Active Stream - Callsign: {}, Source-ID: {}".format(callsign, properties['source']['id']))
                    active_streams.put({
                            'callsign': callsign,
                            'stream-id': properties['source']['id']
                            }
                        )
        else:
            logging.error('Could not connect to Streaming API')
        sleep(10)        


def main():
    logging.basicConfig(format='%(levelname)s:%(threadName)s:%(message)s', level=LOG_LEVEL)
    logging.info('Server Started')
    #logging.info(api.fetch_streams(STREAM_URL, STREAM_API_PORT))
    
    streams = Queue()
    init_certs(CERT_PASS)

    consumer = Thread(target=send_stream, args=(CERT_PASS, streams))
    consumer.start()

    logging.info(f"Connected to Taky Monitor Port")
    producer = Thread(target=fetch_streams, args=(STREAM_URL, STREAM_API_PORT, streams))
    producer.start()

    return


if __name__ == '__main__':
    main()