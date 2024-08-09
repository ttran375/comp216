import socket

HOST = "localhost"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    tcp_server.listen()
    client_conn, addr = tcp_server.accept()

    with client_conn:
        print(f"Client conneted from IP: {addr[0]} via Port: {addr[1]}")
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            print(f"Received from client {data}")
            client_conn.sendall(data)
