import socket


HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    print('Connected to server, type `exit` to quit')

    while True:
        message = input('Enter your message: ')
        if message.lower() == 'exit':
            print('Closing connection...')
            break

        sock.sendall(message.encode())
        data = sock.recv(1024)
        print('Server:', data.decode())
