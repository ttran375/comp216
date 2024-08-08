import socket

HOST = "localhost"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    print("Server is running.")
    tcp_server.listen()
    client_conn, addr = tcp_server.accept()
    print(f"Client connected from IP: {addr[0]} via Port: {addr[1]}")
    print(client_conn)

    with client_conn:
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            client_conn.sendall(data)
            print(f"Sent data: {data.decode()}")
