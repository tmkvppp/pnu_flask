import socket
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Received from client: {message}")

            if message.lower() == "exit":
                break

            time.sleep(5)
            response = "Server received: " + message
            conn.send(response.encode('utf-8'))

print("Connection with client closed.")
