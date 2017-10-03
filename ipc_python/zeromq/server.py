# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import

import time
import zmq

from ipc_python import logger, p_title

p_title('0MQ Server')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    logger.info("Received request: %s" % message)
    time.sleep(1)
    socket.send(b"World")
