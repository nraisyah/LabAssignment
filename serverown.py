import socket
import math
import sys
import time 
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found \n\n'


def process_start(s_sock):
	s_sock.send(str.encode("--Successfully connected to server."))
	while True:
		ans = s_sock.recv(2048).decode("utf-8").split(":")

		if ans[0] == "L" :
			result = math.log(float(ans[1]))

		elif ans[0] == "S":
			result = math.sqrt(float(ans[1]))

		elif ans[0] == "E":
			result = math.exp(float(ans[1]))

		elif ans[0] == "X":
			break

		s_sock.sendall(str.encode(str(result)))
	s_sock.close()

if __name__ == '__main__':

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',8080))
	print("--Listening to client")
	s.listen(3)

try:
	while True:
		try:
			s_sock,s_addr = s.accept()
			print("--Connected from : ", s_addr)
			p = Process(target = process_start,args = (s_sock,))
			p.start()

		except socket.error:
			print('--Socket cannot be created.')

except Exception as e:
	print('an exception occured!')
	print(e)
