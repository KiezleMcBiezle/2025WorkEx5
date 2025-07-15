import asyncio

async def handle_connection(reader, writer):
    print("e")
    # .read() can be used to receive incoming data
    # from the other computer, this blocks the program
    # until some data is available, so await is used
    # to allow other code to run while waiting. It returns
    # a list of bytes.
	
	# The parameter sets the maximum amount of data to read,
	# if more data is available, it is not read into the list.
	# This data will be read on the next call to .read().
	
	# You will need to work out a way of making sure you read 
	# an entire message so no data is lost.
    data = await reader.read(100)
	
	# When reading in a string, .decode() can be used to
	# parse the bytes.
    message = data.decode()
	
	# .write() can be used to send data to the other computer,
	# this data has to be raw binary, so you can't send lists,
	# dictionaries, sets, etc without first serialising them to
	# binary.
    writer.write(data)
	
	# Calling .write() doesn't always actually send the data, it will
	# queue it to be sent, but to ensure the data is actually sent,
	# use .drain(). This will block the program until all the data is sent,
	# so await is used so other code can be run while waiting.
    await writer.drain()
	
	# The socket connection can be closed by either the client or the
	# server using .close(). You will need to handle either the client or
	# the server closing the connection at any time.
    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
	# Bind the server to a specific port (in this case 8888), 
	# the address can be used to limit which computers can 
	# connect to the server, 0.0.0.0 allows any computer on 
	# the network to connect.
    server = await asyncio.start_server(
        handle_connection, '0.0.0.0', 1234)
	
	# A single server can listen on many physical connections 
	# at the same time, for example it could listen on a wired 
	# Ethernet connection and a WiFi connection at the same time.
	# Each one of these will have it's own IP address, this gets
	# all of those addresses, concatenates them and prints them. 
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
	
	# Listen for incoming connections forever.
    async with server:
        await server.serve_forever()

asyncio.run(main())