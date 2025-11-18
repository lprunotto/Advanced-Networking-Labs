#!/usr/bin/env python3

import socket
import struct
import sys

if len(sys.argv) != 3:
    print('usage: %s <mcast_address> <port>' % sys.argv[0])
    sys.exit(1)

mcast_addr = sys.argv[1]
try:
    mcast_port = int(sys.argv[2])
except ValueError:
    print("Error: <port> must be an integer.")
    sys.exit(1)

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow reuse of addresses (important when rerunning tests)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to all interfaces on the given port
sock.bind(('', mcast_port))

# Join the multicast group
mreq = struct.pack("4sL", socket.inet_aton(mcast_addr), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive loop
while True:
    data, addr = sock.recvfrom(1024)
    print(data.decode().strip(), flush=True)
