# import os
import socket
import sys
#HOST = '157.230.52.239'
HOST = '127.0.0.1'
PORT = 4040

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((HOST, PORT))
        print("enter 'exit' to disconnect")
        user_in = input('$>')
        
        while user_in != "exit":
            s.sendall(bytes(user_in, 'utf-8'))
            data = s.recv(2048)
            print(data.decode('utf-8'), end='')
    
            user_in = input('$>')
