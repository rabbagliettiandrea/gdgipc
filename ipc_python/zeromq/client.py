# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import

import zmq

from ipc_python import logger, p_title

p_title('0MQ Client')

context = zmq.Context()

logger.info('Connecting to hello world server…')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in xrange(10):
    logger.info('Sending request %s...' % request)
    socket.send(b'Hello')

    #  Get the reply.
    message = socket.recv()
    logger.info('Received reply %s [ %s ]' % (request, message))
