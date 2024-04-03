import socket

# Create a socket object
s = socket.socket()

port = 9090

# Connect to the server 
s.connect(('127.0.0.1', port))

while True:
    
    # Receive message from server
    message_received = s.recv(1024).decode()
    if not message_received:
        break
    print('Received from server:', message_received)

    # Send message to server
    message_to_send = input('Give your message : ')
    s.send(message_to_send.encode())

# Close the connection
s.close()