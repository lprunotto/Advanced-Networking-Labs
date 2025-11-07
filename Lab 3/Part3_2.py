#usage python3 client.py server port
import socket
import sys

if len(sys.argv) != 3:
    print('usage: %s <server> <port> <command>' % sys.argv[0])
    sys.exit(1)    

server = sys.argv[1]
port = sys.argv[2]
buffer_size = 1024

try:
    port = int(port)
except ValueError:
    print("Error: <port> must be an integer.")
    sys.exit(1)

ipv4_addr = socket.gethostbyname(server) 
ipv6_info = socket.getaddrinfo(server, port, socket.AF_INET6)[0]
ipv6_info = ipv6_info[4]

sum = 0
for i in range(60):
    count = 0
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)   

    message = "RESET:20"
    s6.settimeout(1)
    s4.settimeout(1)
    flag = True

    while flag:
        count += 1
        s4.sendto(message.encode(), (ipv4_addr, port))
        s6.sendto(message.encode(), ipv6_info)
        try:
            data, addr = s4.recvfrom(buffer_size)  
            print(f"It took {count} tries")
            sum += count
            flag = False
            m = data.decode()
            print("Received:", data.decode())
            s4.close()
            s6.close()
        except socket.timeout:
            try:
                data, addr = s6.recvfrom(buffer_size)  
                print(f"It took {count} tries")
                sum += count
                flag = False
                m = data.decode()
                print("Received:", data.decode())
                s4.close()
                s6.close()
            except socket.timeout:
                flag = True

print(f"On average, it took {sum/60} tries")


