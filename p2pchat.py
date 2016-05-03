# cheat #1: simple p2p chat app
# @author: alfin.akhret@gmail.com

import socket
import sys
import argparse

# the server
def start_server(local_port):
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, local_port))
    server_socket.listen(5)
    '''
    while 1:
        client_socket, client_addr = server_socket.accept()
    '''

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


