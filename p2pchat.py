# cheat #1: simple p2p chat app
# @author: alfin.akhret@gmail.com

import socket
import sys
import argparse
import urllib
import threading
from threading import Event

# the server
def start_server(local_port):
    # create socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "[*] Error: Cannot create socket object: %s" % e
        sys.exit(1)

    host = get_public_ip()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, local_port))
    except socket.error, e:
        print "[*] Error: Cannot bind socket: %s" % e

    server_socket.listen(5)
    print "[*] Server listening on %s:%d" % (host, local_port)

    while 1:
        client_socket, client_addr = server_socket.accept()
        print "[*] Accepted connection from: %s:%d" % \
        (client_addr[0], client_addr[1])

        # start two threads
        message_handler(client_socket)

def message_handler(client_socket):

    while 1:

        message = client_socket.recv(1024)
        reply_handler(client_socket)

        if len(message):
            print "\n[*] << %s" % message.rstrip()

            # client close the connection
            if 'exit()' in message and '\r' in message:
                client_socket.close()
                break;

def reply_handler(client_socket):
    reply = raw_input("[*] >> ")
    if len(reply):
        client_socket.send(reply + '\n')

    if 'exit()' in reply and '\r' in reply:
        client_socket.close()

def get_public_ip():
    # get public facing IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip  = s.getsockname()[0]
    s.close()
    return ip


def main():
    parser = argparse.ArgumentParser(description='simple p2p chat')
    parser.add_argument('--port', type=int,
                        required=True,
                        help='listening port to use',
                        dest='local_port')
    parser.add_argument('--host', required=False,
                        help='target host to talk',
                        dest='peer_host')
    parser.add_argument('--tport', required=False,
                        help='target port to talk',
                        dest='peer_port')

    given_args = parser.parse_args()
    local_port = given_args.local_port
    peer_host= given_args.peer_host
    peer_port = given_args.peer_port

    if local_port:
        start_server(local_port)

if __name__ == '__main__':
    main()
