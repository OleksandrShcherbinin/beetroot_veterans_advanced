import socket

# HOST = '127.0.0.1'
# PORT = 65432
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.bind((HOST, PORT))
#     sock.listen()
#     connection, address = sock.accept()
#
#     with connection:
#         print('Connected by', address)
#         while True:
#             data = connection.recv(1024)
#             if not data:
#                 break
#
#             connection.sendall(data)
#             print('Received', data.decode())
import threading


HOST = '127.0.0.1'
PORT = 65432
HEADER_SIZE = 1024
DISCONNECT_MESSAGE = 'exit'
ADDRESS = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(connection, address):
    print('New connection', address)
    connected = True
    while connected:
        message = connection.recv(HEADER_SIZE).decode()
        if message:
            print(f'[{address}] - {message}')
            if message == DISCONNECT_MESSAGE:
                connected = False

            connection.send(f'Message received from {address}'.encode())

    connection.close()


def start():
    server.listen()
    print(f'Server listen on {HOST}')
    while True:
        connection, address = server.accept()
        # handle_client(connection, address)
        thread = threading.Thread(
            target=handle_client,
            args=(connection, address)
        )
        thread.start()


if __name__ == '__main__':
    start()
