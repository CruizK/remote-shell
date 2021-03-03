#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) != 2:
    print("usage: client.py host_name")
    sys.exit(1)

HOST = sys.argv[1]
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((HOST, PORT))
        print("enter 'exit' to disconnect")
        user_in = input('$>')
        
        while user_in != "exit":
            s.sendall(bytes(user_in, 'utf-8'))
            data = s.recv(2048)
            print(data.decode('utf-8'), end='')
    
            user_in = input('$>')
