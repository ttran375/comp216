import socket
import time

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

    # tcp_client.sendall("Terry".encode())
    # message = tcp_client.recv(1024)
    # print(message.decode("utf-8"))

    # for i in range(4):
    #     outbound_message = f"Message {i}"
    #     tcp_client.sendall(outbound_message.encode())
    #     inbound_message = tcp_client.recv(1024)
    #     print(f'Received from server: {inbound_message.decode("utf-8")}')
    #     time.sleep(1)
