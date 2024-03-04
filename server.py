import socket
import threading
import signal
import sys

clients = []
client_info = {}  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def broadcast_message(message, sender_socket=None):
    for client_socket in clients:
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            clients.remove(client_socket)
            client_socket.close()

def handle_client(client_socket, client_address):
    username = client_socket.recv(1024).decode('utf-8')
    welcome_message = f"\n\n{username} has joined the chat!"
    broadcast_message(welcome_message)
    client_info[client_socket] = username

    connected_users = [info for sock, info in client_info.items() if sock != client_socket]
    if len(connected_users) > 0:
        client_socket.send(f"\n\nConnected users: {', '.join(connected_users)}".encode('utf-8'))
    else:
        client_socket.send(f"\n\nYou're currently alone in this room.".encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'quit':
                break
            else:
                broadcast_message(f"{username}: {message}", client_socket)
        except:
            break

    clients.remove(client_socket)
    broadcast_message(f"\n\n{username} has left the chat.\n\n")
    del client_info[client_socket]
    client_socket.close()

def start_server():
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen()
    print("Server started, waiting for connections...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
        except OSError:  
            break

def signal_handler(sig, frame):
    print("Shutting down server...")
    for client_socket in clients:
        client_socket.close()
    server_socket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

start_server()