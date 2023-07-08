import socket
import json

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))

    user_input = input("Enter a message to the server: ")

    data = {
        "username":"khethelo",
        "message":user_input
    }

    message = json.dumps(data)
    client_socket.send(message.encode())

    response = client_socket.recv(1024)
    print("Received from server: ", response.decode())

    client_socket.close()

if __name__ == "__main__":
    main()