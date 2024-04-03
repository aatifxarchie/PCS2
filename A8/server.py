import socket

# create socket object
s = socket.socket()
print('Socket created')

# bind socket to a specific address and port
s.bind(('localhost', 9090))

# put the socket into listening mode
s.listen(3)

print('waiting for connections')

while True:
    c, addr = s.accept()
    print('Connected with', addr)

    while True:
        # Send message to client
        message_to_send = 'You are connected to the server!'
        c.send(message_to_send.encode())

        # Receive message from client
        message_received = c.recv(1024).decode()
        if not message_received:
            break
        print('Received from client:', message_received)

    c.close()
