#usage python3 client.py server port command
import socket
import ssl
import pprint
from datetime import datetime
from time import sleep
import subprocess
import re
import sys
import websocket

if len(sys.argv) != 4:
    print('usage: %s <server> <port> <command>' % sys.argv[0])
    sys.exit(1)

server = sys.argv[1]
port = sys.argv[2]
command = sys.argv[3]


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
url = f"ws://{server}:{port}"
ws = websocket.WebSocket()
ws.connect(url)
ws.send(command)

try:
    buffer = ""

    while True:
        message = ws.recv()
        if not message:
            break
        buffer += str(message.decode())
        '''while True:
            match = pattern.search(buffer)
            if not match:
                break
            print(match.group())
            buffer = buffer[match.end():]'''
        print(buffer)
        buffer = ""
finally:
    s.close()

