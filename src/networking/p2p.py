#!/usr/bin/env python3
import socket

class P2PChat():
    def __init__(self):
        pass

    def create_socket(self, host, port):
        if type(host) == str and type(port) == int:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            raise TypeError("TypeError: {} and {}".format(host, port))

        return s

