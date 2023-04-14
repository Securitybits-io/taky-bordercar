import logging
import socket
import os

import cot
import api

import xml.etree.ElementTree as ET

from threading import Thread
from datetime import datetime
from time import sleep
from queue import Queue

STREAM_URL      = os.getenv("STREAM_URL", default="127.0.0.1")
STREAM_API_PORT = os.getenv("STREAM_API_PORT", default=9997)

TAKY_MON_IP     = os.getenv("TAKY_MON_IP", default="127.0.0.1")
TAKY_MON_PORT   = os.getenv("MON_PORT", default=1337)
LOG_LEVEL       = os.getenv("LOG_LEVEL", default="INFO").upper()

def main():
    return


if __name__ == '__main__':
    main()