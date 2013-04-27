#!/usr/bin/env python
import zmq

ctx = zmq.Context()

sender = ctx.socket( zmq.PUSH )
sender.bind( "tcp://*:5557" )

sink = ctx.socket( zmq.PUSH )
sink.connect( "tcp://localhost:5558" )

print "Press Enter when the workers are ready"

import sys
sys.stdin.read(1)

print "Sending tasks to workers"

sink.send_json( 0 )

import random
tasks = [random.randint(1,100) for _ in range(0,100)]

[sender.send_json( t ) for t in tasks]

print "Total expected cost: %s mec" % sum(tasks)
print "Press Enter when the workers are done"

sys.stdin.read(1)

print "Done"


