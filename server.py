import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message from {client_address}: {message}")
                broadcast_message(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except Exception as e:
            print(f"Error handling client {client_address}: {str(e)}")
            remove_client(client_socket)
            break

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8546))
    server_socket.listen(5)

    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"New connection established: {client_address}")

        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

clients = []

start_server()
