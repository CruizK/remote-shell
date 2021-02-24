import os
import socket
import subprocess

HOST = '127.0.0.1'
PORT = 2005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
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
                    conn.sendall(b'command complete')
            
            except subprocess.CalledProcessError as e:
                conn.sendall(str(e).encode())

            # print("this is what returned: " + str(output))