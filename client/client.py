import socket
import secret

HOST = secret.HOST
PORT = secret.PORT

if __name__ == "__main__":

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))

	data = 'temp'

	while data != '':
		data = sock.recv(2048).decode()
		print(data, end='')

	sock.close()

