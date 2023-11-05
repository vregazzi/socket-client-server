import socket
from _thread import start_new_thread

host = '127.0.0.1'
port = 9500
ThreadCount = 0


def client_handler(conn):
    conn.send(str.encode('successfully connected, type "quit" to leave'))
    while True:
        data = conn.recv(2048)
        message = data.decode('utf-8')
        if message.lower() == 'quit':
            break
        elif message.lower() == 'hello':
            conn.sendall(str.encode("Hi"))
        else:
            conn.sendall(str.encode("Goodbye"))
    conn.close()


def accept_connections(server_socket):
    Client, address = server_socket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))


if __name__ == '__main__':
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()
    
    while True:
        accept_connections(ServerSocket)
