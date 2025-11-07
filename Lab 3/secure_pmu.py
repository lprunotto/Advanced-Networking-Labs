import socket
import ssl
import pprint
from datetime import datetime
from time import sleep
import subprocess
import re
import random
import sys

HOST = 'localhost'
#PORT = 5003
BUFFER_SIZE = 1024

if len(sys.argv) != 4:
    print('usage: %s <port> <certificate> <key>' % sys.argv[0])
    sys.exit(1)

port = sys.argv[1]
filecert = sys.argv[2]
key = sys.argv[3]

try:
    port = int(port)
except ValueError:
    print("Error: <port> must be an integer.")
    sys.exit(1)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=filecert, keyfile=key)
context.verify_mode = ssl.CERT_NONE  
pmu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pmu_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
pmu_socket.bind((HOST, port))
pmu_socket.listen(5)
print(f"Listening on {HOST}:{port}")

while True:
	conn, addr = pmu_socket.accept()
	print("first step ok")
	socket_ssl = context.wrap_socket(conn, server_side=True)
	print(f"Connection from {addr} accepted")
	cmd = socket_ssl.recv(BUFFER_SIZE).decode()
	if cmd.startswith("CMD_short:0"):
		n = random.randint(5, 10)
		for i in range(n):
			message = "This is PMU data " + str(i)
			socket_ssl.sendall(message.encode('utf-8'))
			sleep(1)
	socket_ssl.close()
