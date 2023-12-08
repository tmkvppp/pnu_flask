import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input('Enter something: ')
        message = msg.encode('utf-8')
        s.send(message)

        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
