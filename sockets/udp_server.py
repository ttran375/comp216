import socket

HOST = "localhost"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_server:
    udp_server.bind((HOST, PORT))
    while True:
        data, addr = udp_server.recvfrom(1024)
        print(f"Client connected from IP: {addr[0]} via Port {addr[1]}")
        print(f"Data from client: {data}")
        udp_server.sendto(data, addr)
        break
