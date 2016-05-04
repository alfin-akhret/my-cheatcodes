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
import sys

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
        s = create_socket(ip=self.ip, port=self.port)
        s.listen(1)
        print ("Listening on {}:{}".format(self.ip, self.port))
        self.conn, self.addr = s.accept()
        while self.running:
            input_ready, output_ready, except_ready \
                    = select.select([self.conn], [self.conn], [])
            for input_item in input_ready:
                buff = self.conn.recv(RCV_BUF_SIZE)
                if buff:
                    print ("Them: {}".format(buff))
                else:
                    break
            time.sleep(0)

    def kill(self):
        self.running = 0

# client class
class Client(threading.Thread):
    def __init__(self, ip, peer_port=None, peer_ip=None):
        threading.Thread.__init__(self)
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.sock = None
        self.running = 1

    def run(self):
        self.sock = create_socket(ctype='client')
        self.sock.connect((self.peer_ip, self.peer_port))
        print ("CLient Listening on {}:{}".format(self.peer_ip, self.peer_port))

        while self.running:
            input_ready, output_ready, except_ready \
                    = select.select([self.sock], [self.sock], [])
            for input_item in input_ready:
                buff = self.sock.recv(RCV_BUF_SIZE)
                if buff:
                    print ("Them: {}".format(buff))
                else:
                    break
            time.sleep(0)

    def kill(self):
        self.running = 0

class TextInput(threading.Thread):
    def __init__(self, client=None, server=None):
        threading.Thread.__init__(self)
        self.running = 1
        self.client = client
        self.server = server

    def run(self):
        while self.running:
            text = input(">>")
            try:
                self.client.sendall(text)
                print("sending...")
            except socket.error as e:
                print("[Error]: {}".format(e))
                sys.exit(1)

            try:
                self.server.sendall(text)
                print ("sending...")
            except socket.error as e:
                print("[Error]: {}".format(e))
                sys.exit(1)
            time.sleep(0)

    def kill(self):
        self.running = 0

# helper
def create_socket(ip='', port=0, ctype='server'):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print ("[Error]: {}".format(e))

    if ctype == 'server':
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))

    return s

def main():
    parser = argparse.ArgumentParser(description='Primitive P2P chat \
                                     application')
    parser.add_argument('--host', dest='host', default='', help='Your \
                        IP Address', required=False)
    parser.add_argument('--port', dest='port', default=9999, type=int,  help='port \
                        to listen. (default=9999)', required=False)
    parser.add_argument('--peer', dest='peer_ip', default='',
                        help='peer\'s ip address [ip:port], leave blank if you just \
                        want to wait for your peer to connect', required=False)
    given_args = parser.parse_args()

    if not len(given_args.host):
        # get public facing IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        HOST = s.getsockname()[0]
        s.close()
    else:
        HOST = given_args.host

    PORT = given_args.port
    if len(given_args.peer_ip):
        peer_ip = given_args.peer_ip.split(':', 1)[0]
        peer_port = int(given_args.peer_ip.split(':',1)[1])


    if not len(given_args.peer_ip):
        # act like server
        chat_server = Server(HOST, PORT)
        chat_server.start()
        chat_client = Client(HOST)
        print("chat server {}".format(chat_server))
        print("chat_client {}".format(chat_client))
        text_input = TextInput(server=chat_server)
        text_input.start()
    else:
        # act like client
        chat_server = Server(HOST, PORT)
        chat_client = Client(HOST, peer_ip=peer_ip, peer_port=peer_port)
        print("chat server {}".format(chat_server))
        print("chat_client {}".format(chat_client))

        chat_client.start()
        text_input = TextInput(client=chat_client)
        text_input.start()

if __name__ == '__main__':
    main()
