import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

clients = []


def handle_client(client, address):
    try:
        while True:
            message = client.recv(1024).decode('utf-8')

            for c in clients:
                c.send(f'{address[0]}:{address[1]} says: {message}'.encode('utf-8'))
    except:
        clients.remove(client)
        client.close()


def start_server():
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"Connection from {address} has been established!")

        client_handler = threading.Thread(target=handle_client, args=(client, address))
        client_handler.start()

        clients.append(client)

start_server()
