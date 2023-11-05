import socket

host = '127.0.0.1'
port = 9500


def client():
    ClientSocket = socket.socket()
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    Response = ClientSocket.recv(1024)
    while True:
        msg = input(' -> ')
        ClientSocket.send(str.encode(msg))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        if msg.lower() == 'quit':
            break

    ClientSocket.close()


if __name__ == "__main__":
    client()
