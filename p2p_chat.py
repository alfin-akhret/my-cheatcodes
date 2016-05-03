#!/usr/bin/env python3

# @author: alfin.akhret@gmail.com
# inspired by Teddy_K
# check out his awesome work here:
# https://code.activestate.com/recipes/578591-primitive-peer-to-peer-chat/

import socket
import threading
import select
import time
import argparse


# global vars
HOST = ''
PORT = 9999
SND_BUF_SIZE = 2048
RCV_BUF_SIZE = 2048
peer_ip = ''

def main():
    parser = argparse.ArgumentParser(description='Primitive P2P chat \
                                     application')
    parser.add_argument('--host', dest='host', default='', help='Your \
                        IP Address', required=False)
    parser.add_argument('--port', dest='port', default=PORT, help='port \
                        to listen. (default=9999)', required=False)
    parser.add_argument('--peer', dest='peer_ip', default=peer_ip,
                        help='peer\'s ip address, leave blank if you just \
                        want to wait for your peer to connect', required=False)
    given_args = parser.parse_args()

    if not len(given_args.host):
        # get public facing IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        HOST = s.getsockname()[0]
        s.close()
    print ("{}".format(HOST))

if __name__ == '__main__':
    main()
