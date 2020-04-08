import socket
import secret

HOST = secret.HOST
PORT = secret.PORT

if __name__ == "__main__":

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		sock.connect((HOST, PORT))
	except ConnectionRefusedError:
		exit("Connection refused: is the server running?")

	data = 'temporary data value'

	while data != '':
		data = sock.recv(2048).decode()
		print(data, flush=True, end='')

	sock.close()

