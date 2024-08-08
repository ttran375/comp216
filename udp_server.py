import socket

HOST = "localhost"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_server:
    udp_server.bind((HOST, PORT))
    print("Server is running.")

    while True:
        message, addr = udp_server.recvfrom(1024)
        print(f"Client connected from IP: {addr[0]} via Port: {addr[1]}")
        print(f'Message from client: {message.decode("utf-8")}')

        outbound_message = b"Messaged Accepted."
        udp_server.sendto(outbound_message, addr)
        break
