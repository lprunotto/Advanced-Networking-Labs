#usage python3 client.py server port command
import socket
import ssl
import pprint
from datetime import datetime
from time import sleep
import subprocess
import re
import sys

if len(sys.argv) != 4:
    print('usage: %s <server> <port> <command>' % sys.argv[0])
    sys.exit(1)

server = sys.argv[1]
port = sys.argv[2]
command = sys.argv[3]

buffer_size = 1024


try:
    port = int(port)
except ValueError:
    print("Error: <port> must be an integer.")
    sys.exit(1)

valid_commands = ["CMD_short:0", "CMD_short:1", "CMD_floodme"]
pattern = re.compile(r"This is PMU data \d+")

if command not in valid_commands:
    print("Error: <command> must be one of", ", ".join(valid_commands))
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((server, port))

    s.sendall(command.encode())
    buffer = ""

    while True:
        message = s.recv(buffer_size).decode()
        if not message:
            break
        buffer += message
        while True:
            match = pattern.search(buffer)
            if not match:
                break
            print(match.group())
            buffer = buffer[match.end():]

    if buffer:
        print(buffer)
finally:
    s.close()

