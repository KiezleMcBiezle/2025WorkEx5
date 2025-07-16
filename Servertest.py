import socket
from threading import Thread

SERVER_HOST = "0.0.0.0" # server IP
SERVER_PORT = 8888 # port number
separator_token = "SEPERATE" # we will use this to separate the client name & message

# initialize list/set of all connected client's sockets
client_sockets = list()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
# SO_REUSEADDR makes sure that if 1 client disconnects 
# and one reconnects in a short timespan the server can 
# make use of the free port instead of it being placed in limbo
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket
s.bind((SERVER_HOST, SERVER_PORT))
# listen for 2 connections
s.listen(2)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(CSocket):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            # Must decode to parse the bytes
            msg = CSocket.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(CSocket)
        else:
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            msg = msg.replace(separator_token, ":")
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            # encode the message so that it can be decoded on the client
            client_socket.send(msg.encode())

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()

