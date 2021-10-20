# CLIENT EXAMPLE
# (c) 2021 by Z. Matni for use in CS176A (UCSB)

# using professor Matni's client example

# Socket programming library:
from socket import *
import sys

ip = sys.argv[1] # the first argument 
port = sys.argv[2] # the second argument

# For this assignment, we'll use PORT = 12000
PORT = 12000
HOST = "127.0.0.1"   # means "local host"
FORMAT = 'utf-8'
SIZE = 2048

#initalize socket with buffer size 2048 bytes
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Enter string: ")
clientSocket.sendto(message.encode(FORMAT), (HOST, PORT))

# using while(true) to keep getting inputs from server
# once final input is received, break
# or if it is a string, print out and break
while(True):
    recvMessage, serverAddress = clientSocket.recvfrom(SIZE)
    if(recvMessage.decode(FORMAT).isnumeric()):
        print("From server:", recvMessage.decode(FORMAT))
        if(len(recvMessage.decode(FORMAT)) == 1):
            clientSocket.close()
            break
    else: 
        print("From server:", recvMessage.decode(FORMAT))
        clientSocket.close()
        break
        