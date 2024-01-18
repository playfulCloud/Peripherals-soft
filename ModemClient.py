import socket
import os

def receive_file(server_socket):
    client_socket, address = server_socket.accept()
    print(f"Połączenie z {address} zostało nawiązane.")

    with client_socket:
        file_name = client_socket.recv(1024).decode()
        file_size = int(client_socket.recv(1024).decode())

        with open(file_name, 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
                bytes_received += len(data)

        print(f"Plik {file_name} został odebrany.")

def main():
    host = '0.0.0.0'  # Nasłuchiwanie na wszystkich dostępnych interfejsach sieciowych
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Serwer nasłuchuje na porcie {port}...")
        receive_file(server_socket)

if __name__ == "__main__":
    main()
