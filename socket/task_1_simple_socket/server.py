import socket
import datetime

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            print(f"Received from client: {decoded_data}")
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Received at: {current_time}")
