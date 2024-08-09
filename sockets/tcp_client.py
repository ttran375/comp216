import socket
import threading

SERVER_HOST = "localhost"
SERVER_PORT = 12345


def incoming_message(client_soc_obj):
    while True:
        incoming_message = client_soc_obj.recv(2048)
        print(incoming_message.decode("utf-8"))


def sending_message(client_soc_obj):
    while True:
        outbound_message = input("Enter message: ")
        client_soc_obj.sendall(outbound_message.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
    tcp_client.connect((SERVER_HOST, SERVER_PORT))
    print("Client connected to the server")

    username = input("Username: ")
    tcp_client.sendall(username.encode())
    connect_message = tcp_client.recv(2048)
    print(f'{connect_message.decode("utf-8")}')

    threading.Thread(target=incoming_message, args=(tcp_client,)).start()

    sending_message(tcp_client)
