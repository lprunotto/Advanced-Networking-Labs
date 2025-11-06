#! /usr/bin/env python3.5

import socket, struct, sys, time

MCAST_GRP = ''
MCAST_PORT = 0
file = None
interval = 1
buffer_size = 1024

if len(sys.argv) != 3:
    print('usage: %s <mcast_address> <port>' % sys.argv[0])
    sys.exit(1)

try:
    MCAST_GRP = sys.argv[1]
    MCAST_PORT = int(sys.argv[2])
except:
    print('Invalid parameters')
    print('usage: %s <multicast group> <port>' % sys.argv[0])
    sys.exit(2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
    data, addr = sock.recvfrom(1024)
    print(data.decode())

