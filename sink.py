#!/usr/bin/env python
import zmq

ctx = zmq.Context()

receiver = ctx.socket( zmq.PULL )
receiver.bind( "tcp://*:5558" )

receiver.recv_json()

import time, sys
start = time.time()

def read():

  receiver.recv_json()
  sys.stdout.write( "." )
  sys.stdout.flush()

[read() for _ in range(0,100)]

print "\nTotal elapsed time: %s" % (time.time() - start )

