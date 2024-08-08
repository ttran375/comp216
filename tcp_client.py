import socket

SERVER_HOST = "localhost"
SERVER_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
    print(f"Socket object: {tcp_client}")
    tcp_client.connect((SERVER_HOST, SERVER_PORT))
    print(f"Client connected to the server")