#!/usr/bin/python3

import sys
import socket
import threading
import random
import string
import time
import secret
import queue

HOST = secret.HOST 
PORT = secret.PORT


def socket_action2(conn, addr, q, queues):

    while True:
        data = q.get()
        try:
            conn.send(data.encode('utf-8'))
        except ConnectionResetError as cre:
            conn.close()
            queues.remove(q) # This is unsafe
            exit() # Kill this thread quietly


def printing_thread(queues):

    for data in sys.stdin:

        print(data, end='')    
        for q in queues:
            q.put(data) 
        # time.sleep(3)


def main():

    queues = []

    print_thread = threading.Thread(target=printing_thread, args=(queues,), daemon=True)
    print_thread.start()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((HOST, PORT))
    except OSError:
        exit("Socket is busy, try again in a few seconds")        

    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        # print(f"Accepted connection from addr {addr}")

        q = queue.Queue()

        queues.append(q)

        thread = threading.Thread(target=socket_action2, args=(conn, addr, q, queues), daemon=True)
        thread.start()


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        exit("\nServer script ending")
