#! /usr/bin/env python3.5

import socket, struct, sys, time

MCAST_GRP = ''
MCAST_PORT = 0
camipro = ""


if len(sys.argv) != 4:
    print('usage: %s <mcast_address> <port> <sciper>' % sys.argv[0])
    sys.exit(1)

try:
    MCAST_GRP = sys.argv[1]
    MCAST_PORT = int(sys.argv[2])
    camipro = sys.argv[3]
except:
    print('Invalid parameters')
    print('usage: %s <mcast_address> <port> <sciper>' % sys.argv[0])
    sys.exit(2)

if len(camipro) != 6 or not camipro.isdigit():
    print("Error: Sciper must be exactly 6 numbers.")
    sys.exit(1)
    
cl_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 10)
cl_sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

text = ""
while True:
    text = input("Enter something: ")
    if text != "":
        cl_sock.sendto((camipro + ": " + text).encode(), (MCAST_GRP, MCAST_PORT))

cl_sock.close()
