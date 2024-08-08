import socket

SERVER_HOST = "localhost"
SERVER_PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
    outbound_message = b"Testing UDP socket."
    udp_client.sendto(outbound_message, (SERVER_HOST, SERVER_PORT))

    incoming_message, addr = udp_client.recvfrom(1024)
    print(f"Server Message: {incoming_message.decode('utf-8')}")
    print(f"Server Details: IP: {addr} via Port: {addr[1]}")
