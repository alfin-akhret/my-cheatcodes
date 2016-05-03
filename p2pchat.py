# cheat #1: simple p2p chat app
# @author: alfin.akhret@gmail.com

import socket
import sys
import argparse
import threading
import urllib


peers = {} # simple dictionay to hold client connections fileno:ip_address

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

        # add this new peer to peers array
        peers[client_socket.fileno()] = client_addr[0]

        # start client thread
        try:
            client_handler = threading.Thread(target=handle_client,
                                          args=(client_socket,))
            client_handler.start()
        except:
            print "[*] Error: Unable to start a thread"


def handle_client(client_socket):
    message = client_socket.recv(1024)
    print "[*] client_%s@%s says: %s" % (client_socket.fileno(),
                                         peers[client_socket.fileno()],
                                         message)
    # send back packet
    # client_socket.send('ack!')
    # client_socket.close()


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
