import socket

sock = socket.socket()
host = socket.gethostname()

port = 12000

# https://docs.python.org/3.4/howto/sockets.html
# set socket so that the port is reusable
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to listen to port 12000
sock.bind((host, port))
print('Socket listening, port:', port)

# maximum queued connection is 1
sock.listen(1)

# accept the connection, notify that a client has connected to the server
connectionSocket, addr = sock.accept()
print('A client has connected to the server\n')

while True:
    # server receives a message from the client first
    message = connectionSocket.recv(4096)
    # decode the message and check if it is /q
    message = message.decode()
    # if it is /q, terminate the connection
    if message == '/q':
        print('\nconnection termination request received')
        break
    # else, print the received message
    print('Client : ' + message)
    # collect the server's message and send it to the client
    message = input('Server : ')
    connectionSocket.send(message.encode())
    # check if the sent message is /q and break out of the loop if it is
    if message == '/q':
        print('\nconnection termination request sent')
        break
# when out of the loop, close the socket and terminate the program
connectionSocket.close()
print('Socket successfully closed')
