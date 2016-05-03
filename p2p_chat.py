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

# Server Class
class Server(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.running = 1
        self.conn = None
        self.addr = None
        self.ip = ip
        self.port = port

    def run(self):
        s = create_socket(self.ip, self.port)
        s.listen(1)
        self.conn, self.addr = s.accept()
        while self.running:
            input_ready, output_ready, except_ready \
                    = select.select([self.conn], [self.conn], [])
            for input_item in input_ready:
                buff = self.conn.recv(RCV_BUFF_SIZE)
                if buff:
                    print ("Them: {}".format(buff))
                else:
                    break
            time.sleep(0)

    def kill(self):
        self.running = 0

# helper
def create_socket(ip, port, ctype=server):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print ("[Error]: {}".format(e))

    if ctype == 'server':
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
    else:
        pass

    return s

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

    if not len(given_args.peer_ip):
        # act like server
        pass
    else:
        # act like client
        pass

if __name__ == '__main__':
    main()
