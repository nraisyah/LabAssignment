import socket
import os
import sys

#server vm ip
hostip = "192.168.177.5"

#socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

#connect socket
serverSocket.connect((hostip, PORT))

sendFile = input("\n\n Please enter file name to send at server: ")
#print("File name: " + sendFile)

file = open(sendFile, "rb")
sendData = file.read(1024)

serverSocket.send(sendFile.encode("utf-8"))

while sendData:
        print("--File received!\n", serverSocket.recv(1024).decode("utf-8"))
        print("\tFile name: " + sendFile)
        serverSocket.send(sendData)
        sendData = file.read(1024)

#close socket
serverSocket.close()
