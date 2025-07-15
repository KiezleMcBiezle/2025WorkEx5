import socket 

# The address of the other computer, 
# 127.0.0.1 is a special address which
# refers to this computer. If you run the
# server and the client at the same time,
# connecting to 127.0.0.1 will allow you to
# test everything on one laptop.
ADDRESS = '127.0.0.1'     
PORT = 8888 # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server
s.connect((ADDRESS, PORT))

# Sends "Hello, world" to the server, 
# the b in front of the string tells
# Python to represent the string in binary,
# which allows it to be sent using the socket.

# unlike .write() for the asyncronous socket, 
# .sendall() does actually send the data instead 
# of buffering, so there is no .drain()
s.sendall(b'byebye, World')

# This would fail, since a string isn't binary data
# s.sendall('Hello, world')

# .recv() works like .read() on the server, the
# parameter is used as the maximum amount of data
# to read. Any further data will not be read until the
# next .recv().
data = s.recv(1024)
print('Received', repr(data))

# The socket connection can be closed by either the client or the
# server using .close(). You will need to handle either the client or
# the server closing the connection at any time.
s.close()