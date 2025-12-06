import socket

def client_program():
    host = socket.gethostname()    # server is on same machine
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode("utf-8"))
        data = client_socket.recv(1024).decode("utf-8")
        print("Received from server:", data)

        message = input(" -> ")

    client_socket.close()


if __name__ == "__main__":
    client_program()
