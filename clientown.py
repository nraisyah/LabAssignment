import sys
import socket

clientSocket = socket.socket()
host = '192.168.177.5'
port = 8080

print("--Connecting to server.\n")
print("--CALCULATOR SYSTEM FOR MATHEMATICAL FUNCTION--\n")

try:
	clientSocket.connect((host,port))

except socket.error as e:
	print(str(e))


response = clientSocket.recv(1024)
print(response.decode())

while True:
	opt = input('\n\nPlease Select Mathematical Function \n[L]:Logarithmic |  \n[S]:Square root |  \n[E]:Exponential | \n[X]Exit Calculator System\n You Choose: ')

	if opt == 'L' or opt == 'S' or opt == 'E':

		number = input("Enter the number to be process: ")
		opt = opt + ":" + number
		clientSocket.send(str.encode(opt))
		response = clientSocket.recv(1024)
		print("\nAnswer: ")
		print(response.decode("utf-8"))

	elif opt == 'X':
		print("\n--This system is successfully terminated--\n\t\tTHANK YOU :)")
		clientSocket.send(str.encode(option))
		sys.exit()


clientSocket.close()
