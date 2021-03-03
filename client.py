#!/usr/bin/python
import socket
import sys
import re

if len(sys.argv) != 2:
    print("usage: client.py host_name")
    sys.exit(1)

#HOST = '157.230.52.239'
# HOST = '127.0.0.1'
# PORT = 4040

HOST = sys.argv[1]
PORT = 2005

BUFFER_SIZE = 2048

def cwd_parser(cwd):
    match = re.match("^/home/\w+", cwd)
    if match:
        print(cwd.split(match[0]))
    return cwd

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    print("enter 'exit' to disconnect")
    user_in = ""
    while True:
        cwd = s.recv(BUFFER_SIZE).decode('utf-8')
        user_in = input(cwd_parser(cwd) + '$ ')
        if user_in == "exit":
            break
        s.sendall(user_in.encode('utf-8'))
        data = s.recv(BUFFER_SIZE)
        print(data.decode('utf-8'), end='')


