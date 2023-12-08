import socket
import threading

SERVER = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client.send(message.encode('utf-8'))
