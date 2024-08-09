import socket

HOST = "localhost"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    print("Server is running.")
    tcp_server.listen()

    while True:
        client_conn, addr = tcp_server.accept()
        print(f"Client connected from IP: {addr[1]} via Port: {addr[0]}")

    # client_conn, addr = tcp_server.accept()
    # print(f"Client connected from IP: {addr[0]} via Port: {addr[1]}")
    # # print(client_conn)

    # with client_conn:
    #     while True:
    #         inbound_message = client_conn.recv(1024)
    #         if not inbound_message:
    #             break
    #         print(f"Received from client: {inbound_message.decode('utf-8')}")
    #         outbound_msg = "Server processed message: " + inbound_message.decode(
    #             "utf-8"
    #         )
    #         # client_conn.send(outbound_msg.encode())
    #         # print(f"Sent data: {inbound_message.decode()}")
    #         client_conn.sendall(outbound_msg.encode())
