import socket

HOST = '0.0.0.0'
PORT = 8080

def start_echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Echo server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print(f"Received: {data.decode('utf-8')}")
                conn.sendall(data)

if __name__ == "__main__":
    start_echo_server()
