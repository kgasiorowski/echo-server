#!/usr/bin/python3

import sys
import socket
import threading
import random
import string
import time
import secret

HOST = secret.HOST 
PORT = secret.PORT

def socket_action(conn, addr):

    for i in range(0, 15):

        data = ''

        for i in range(20):
            data += random.choice(string.ascii_letters)
       
        print(f"Sending {data} to {addr}")
 
        data += '\n'            
        conn.send(data.encode('utf-8'));

        time.sleep(3)

    conn.close()
    print(f"Closed connection to addr {addr}")

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print(f"Accepted connection from addr {addr}")
        thread = threading.Thread(target=socket_action, args=(conn, addr,))
        thread.start()

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        exit("\nServer script ending")

