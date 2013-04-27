#!/usr/bin/env python

import zmq

ctx = zmq.Context()

receiver = ctx.socket( zmq.PULL )
receiver.connect( "tcp://127.0.0.1:5557" )

sink = ctx.socket( zmq.PUSH )
sink.connect( "tcp://127.0.0.1:5558" )

while True:

  task = receiver.recv_json()
  print "Sleeping for %s msec" % task

  import time
  time.sleep( task / 1000.0 )

  sink.send_json( task )

