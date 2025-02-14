#!/usr/bin/env python3
'''Minimal running example of a ZMQ SUB socket.
'''

import argparse
import zmq

import dss.auxiliaries


def _print(text):
  print(__file__ + ': ' + str(text))

def _main():
  # parse command-line arguments
  parser = argparse.ArgumentParser(description='_zmq_rep.py', allow_abbrev=False, add_help=False)
  parser.add_argument('-h', '--help', action='help', help=argparse.SUPPRESS)
  parser.add_argument('--ip', default='127.0.0.1', help='IP to subscribe to')
  parser.add_argument('--port', default=5559, help='port to subscribe to')
  args = parser.parse_args()

  context = zmq.Context()
  socket = dss.auxiliaries.zmq.Sub(context, ip=args.ip, port=args.port, timeout=30000, subscribe_all=False)
  socket.subscribe('tes')
  _print('Local IP:' + dss.auxiliaries.zmq.get_ip_address())
  _print('Listening for all topics beginning with \'tes\' from: ' + args.ip + ':' + str(args.port))


  while socket:
    try:
      topic, msg = socket.recv()
      _print((topic, msg))
    except zmq.error.Again as error:
      _print(str(error))
    except KeyboardInterrupt:
      socket.close()
      socket = None

if __name__ == "__main__":
  _main()
