import socket
import sys

#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

#bind
serverSocket.bind(('', PORT))

#listen to incoming connection
serverSocket.listen(3)
print('--Waiting for incoming connection from client\n')

while True:
        conn, ipaddr = serverSocket.accept()
        print("--Connected to client.\n")

        filename= conn.recv(1024)
        file= open(filename, "wb")

        msg= "--Connected to: " + ipaddr[0] + "\nSystem terminated successfully"
        conn.send(msg.encode("utf-8"))

        #receive data from client
        recvdata= conn.recv(1024)
        while recvdata:
                file.write(recvdata)
                recvdata = conn.recv(1024)

        #close file
        file.close()
        print("\n\n\t--File has been sent successfully at server\n")

        #close connection
        conn.close()
        print("Connection closed.\n")

        break
