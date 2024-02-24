#Basic
import socket
import threading

def main():
    host = '127.0.0.1'
    port = 5555
    isServer = input("Do you want to run as a server? (yes/no): ").lower() == 'yes'

    if isServer:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print(f"Server listening on {host}:{port}")

        client_socket, address = server.accept()
        print(f"Client connected at {address}")

        message_receiver = threading.Thread(target=handle_messages, args=(client_socket, False))
        message_receiver.start()

        while True:
            message = input("Server: ")
            client_socket.send(message.encode('utf-8'))
    else:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        message_receiver = threading.Thread(target=handle_messages, args=(client, True))
        message_receiver.start()
        while True:
            message = input("Client: ")
            client.send(message.encode('utf-8'))


def handle_messages(socket, is_server):
    while True:
        try:
            message = socket.recv(1024).decode('utf-8')
            if not message:
                break

            if is_server:
                print(f"Client: {message}")
            else:
                print(f"Server: {message}")

        except ConnectionResetError:
            break


if __name__ == "__main__":
    main()
