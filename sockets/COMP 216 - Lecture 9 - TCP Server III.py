import socket
import threading

HOST = "localhost"
PORT = 12345

active_clients = []


def client_handler(client_soc_obj):
    username = client_soc_obj.recv(2048).decode("utf-8")
    print(f"User {username} connected.\n")
    active_clients.append((username, client_soc_obj))

    sending_message(f"{username} entered the chat room.".encode())
    threading.Thread(
        target=incoming_message,
        args=(
            client_soc_obj,
            username,
        ),
    ).start()


def incoming_message(client_soc_obj, username):
    while True:
        inbound_message = client_soc_obj.recv(2048).decode("utf-8")
        print(f"Message Log: {username} --- {inbound_message}\n")
        outbound_message = f"{username} ~ {inbound_message}".encode()
        sending_message(outbound_message)


def sending_message(message):
    for user in active_clients:
        tcp_client = user[1]
        tcp_client.sendall(message)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    print(f"Server is running on {HOST}:{PORT}.\n")
    tcp_server.listen()

    while True:
        client_conn, addr = tcp_server.accept()
        print(f"Client connected from IP:{addr[0]} via Port: {addr[1]}\n")

        threading.Thread(target=client_handler, args=(client_conn,)).start()
