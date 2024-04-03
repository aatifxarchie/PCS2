import unittest
import socket

class Test(unittest.TestCase):
    def test_server(self):
        
        s = socket.socket()
        port = 9090

        s.connect(('localhost', port))

        message_to_send = 'Hello from client'
        s.send(message_to_send.encode())

        message_received = s.recv(1024).decode()
        message_received = message_received.split('!')[0] + '!'

        # Check if the message received is equal to 'You are connected to the server!'
        self.assertEqual(message_received, 'You are connected to the server!')

        s.close()

if __name__ == '__main__':
    unittest.main()