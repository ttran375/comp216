import socket
import threading

HOST = "localhost"
PORT = 12345


active_clients = []


def client_handler(client_soc_obj):
    username = client_soc_obj.recv(2048).decode("utf-8")
    print(f"User {username} is connected.\n")
    active_clients.append((username, client_soc_obj))
    client_soc_obj.sendall(f"{username} entered Chat Room.".encode("utf-8"))


def incoming_message(client_soc_obj, username):
    while True:
        inbound_message = client_soc_obj.recv(2048).decode("utf-8")
        if not inbound_message:
            break
        print(f"Received from client: {inbound_message}")
        for user, client in active_clients:
            if client != client_soc_obj:
                client.sendall(inbound_message.encode("utf-8"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    print("Server is running.")
    tcp_server.listen()

    while True:
        client_conn, addr = tcp_server.accept()
        print(f"Client connected from IP: {addr[1]} via Port: {addr[0]}")

        threading.Thread(target=client_handler, args=(client_conn,)).start()

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
