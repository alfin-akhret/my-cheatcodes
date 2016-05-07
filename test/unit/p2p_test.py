import unittest
import socket
from networking.p2p import P2PChat

class P2PTest(unittest.TestCase):
    def setUp(self):
        self.p2p = P2PChat()

    # create_socket method
    def test_create_socket_should_return_socket_object_given_correct_params(self):
        self.assertIsInstance(self.p2p.create_socket('localhost', 80),
                              socket.socket)

    def test_create_socket_should_raiseexception_if_params_not_string_and_int(self):
        self.assertRaises(TypeError, self.p2p.create_socket, 1, 80)

if __name__ == '__main__':
    unittest.main()
