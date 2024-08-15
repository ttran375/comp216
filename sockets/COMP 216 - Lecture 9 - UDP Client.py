import socket

SERVER_HOST = "localhost"
SERVER_PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
    udp_client.sendto(b"Testing UDP socket", (SERVER_HOST, SERVER_PORT))
    data, addr = udp_client.recvfrom(1024)
print(f"Recieved from {addr[0]} server: {data}")
