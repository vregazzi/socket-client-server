import socket


def server_program():
    host = socket.gethostname()
    port = 9500

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        if data.lower() == "hello":
            conn.send("Hi".encode())
        else:
            conn.send("Goodbye".encode())

    conn.close()


if __name__ == '__main__':
    server_program()
