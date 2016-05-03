# cheat #1: simple TCP server 
# @author: alfin.akhret@gmail.com

import socket
import sys
import argparse
import urllib

# the server
def start_server(local_port):
    # create socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as  e:
        print ("[*] Error: Cannot create socket object: %s" % e)
        sys.exit(1)

    host = get_public_ip()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, local_port))
    except socket.error as e:
        print ("[*] Error: Cannot bind socket: %s" % e)

    server_socket.listen(5)
    print ("[*] Server listening on %s:%d" % (host, local_port))

    while 1:
        client_socket, client_addr = server_socket.accept()
        print ("[*] Accepted connection from: %s:%d" % \
        (client_addr[0], client_addr[1]))

        # start two threads
        message_handler(client_socket)

def message_handler(client_socket):

    while 1:
        message = client_socket.recv(1024)

        if len(message):
            print ("\n[*] << %s" % message.rstrip())

            reply = b"server replied\n"
            client_socket.send(reply)

            # client close the connection
            if b'exit()' in message and b'\r' in message:
                reply = b"connection closed!\n"
                client_socket.send(reply)
                client_socket.close()
                break;

def get_public_ip():
    # get public facing IP address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print ("[*] Error: %s" % e)
        sys.exit(1)

    try:
        s.connect(('8.8.8.8', 80))
    except socket.error as e:
        print ("[*] Error: %s" % e)

    ip  = s.getsockname()[0]
    s.close()
    return ip


def main():
    parser = argparse.ArgumentParser(description='simple p2p chat')
    parser.add_argument('--port', type=int,
                        required=True,
                        help='listening port to use',
                        dest='local_port')
    given_args = parser.parse_args()
    local_port = given_args.local_port

    if local_port:
        start_server(local_port)

if __name__ == '__main__':
    main()
