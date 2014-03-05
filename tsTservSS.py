#!/usr/bin/env python

from SocketServer import (TCPServer as TCP,
    StreamRequestHandler as SRH, ThreadingTCPServer as TTCP)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        while(True):
            self.wfile.write('[%s] %s' % (ctime(),
                self.rfile.readline()))

tcpServ = TTCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
