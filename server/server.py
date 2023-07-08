import socket
import json

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(1)
    print("Server started. Awaiting client connection...")

    client_socket, address = server_socket.accept()
    print("Client connected.")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print("Recieved from client: ", message)

        response = "Server response: " + message.upper()
        client_socket.send(response.encode())

    print("Client disconnected.")
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()