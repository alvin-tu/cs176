# SERVER
# (c) 2021 by Z. Matni for use in CS176A (UCSB)

# using Professor Matni's example code to code assignment 3
# server tcp

# Socket programming library:
from socket import *
import sys

port = sys.argv[1] # the first argument 

# For this example, we'll use PORT = 12000
PORT = 12000
SERVER = "127.0.0.1"   # means "local host"
FORMAT = 'utf-8'
SIZE = 2048

#initalize socket
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# bind socket to port and connect
serverSocket.bind(('', PORT))


connected = True
while connected:
    message, clientAddress = serverSocket.recvfrom(SIZE)
    if message:
        modMessage = message.decode(FORMAT)
        if(modMessage.isnumeric()):
            if(len(modMessage) == 1):
                serverSocket.sendto(modMessage.encode(FORMAT), clientAddress)

            while(len(modMessage) != 1):
                sum = 0
                stringSum = ""
                for letter in modMessage:
                    sum += int(letter)

                # print(modMessage)
                stringSum = str(sum)
                print(stringSum)
                modMessage = stringSum
                serverSocket.sendto(stringSum.encode(FORMAT), clientAddress)
            
            connected = False
        else:
            responseMessage = "Sorry, cannot compute!"
            serverSocket.sendto(responseMessage.encode(FORMAT), clientAddress)
            connected = False
    continue