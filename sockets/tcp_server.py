import socket
import threading

HOST = "localhost"
PORT = 12345

active_clients = []
clients_lock = threading.Lock()


def client_handler(client_soc_obj):
    try:
        username = client_soc_obj.recv(2048).decode("utf-8")
        print(f"User {username} is connected.\n")
        with clients_lock:
            active_clients.append((username, client_soc_obj))
        sending_message(f"{username} entered Chat Room.".encode())

        threading.Thread(
            target=incoming_message, args=(client_soc_obj, username)
        ).start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_soc_obj.close()
        with clients_lock:
            active_clients.remove((username, client_soc_obj))
        sending_message(f"{username} has left the Chat Room.".encode())


def incoming_message(client_soc_obj, username):
    while True:
        try:
            inbound_message = client_soc_obj.recv(2048).decode("utf-8")
            if not inbound_message:
                break
            print(f"Message Log: {username} -- {inbound_message}")
            outbound_message = f"{username} ~ {inbound_message}".encode()
            sending_message(outbound_message)
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"User {username} has disconnected.")
    with clients_lock:
        active_clients.remove((username, client_soc_obj))
    sending_message(f"{username} has left the Chat Room.".encode())


def sending_message(message):
    with clients_lock:
        for user in active_clients:
            tcp_client_soc = user[1]
            try:
                tcp_client_soc.sendall(message)
            except Exception as e:
                print(f"Error sending message to {user[0]}: {e}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
    tcp_server.bind((HOST, PORT))
    print("Server is running.")
    tcp_server.listen()

    while True:
        client_conn, addr = tcp_server.accept()
        print(f"Client connected from IP: {addr[0]} via Port: {addr[1]}")
        threading.Thread(target=client_handler, args=(client_conn,)).start()
