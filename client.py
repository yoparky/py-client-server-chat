import socket

sock = socket.socket()
host = socket.gethostname()

port = 12000

# https://docs.python.org/3.4/howto/sockets.html
# set socket so that the port is reusable
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((host, port))
print('Socket connected to host port:', port, '\n')

while True:
    # client side send message to connected server side socket
    message = input('Client : ')
    sock.send(message.encode())
    # check if the sent message is /q to break out of loop and close socket
    if message == '/q':
        print('\nconnection termination request sent')
        break
    # after sending the message, receive from the same socket
    message = sock.recv(4096).decode()
    # check if the received message is /q to  break out of loop and close socket
    if message == '/q':
        print('\nconnection termination request received')
        break
    # if not /q, print the message to console
    print('Server : ' + message)
# when out of the loop, close the socket and terminate the program
sock.close()
print('Socket successfully closed')

