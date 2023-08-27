import socket
import threading

print()
print("  ______     ______   ____ _           _     ____                           ")
print(" |  _ \ \   / /  _ \ / ___| |__   __ _| |_  / ___|  ___ _ ____   _____ _ __ ")
print(" | |_) \ \ / /| |_) | |   | '_ \ / _` | __| \___ \ / _ \ '__\ \ / / _ \ '__|")
print(" |  __/ \ V / |  _ <| |___| | | | (_| | |_   ___) |  __/ |   \ V /  __/ |   ")
print(" |_|     \_/  |_| \_\\\\____|_| |_|\__,_|\__| |____/ \___|_|    \_/ \___|_|   ")
print("                                                                            ")
print()

clients = []
IP = "0.0.0.0"
PORT = 4007

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)

print("\nListening on: {}:{}".format(IP, PORT))

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                pass

def handle_client(client_socket):
    nick = client_socket.recv(1024).decode()
    color = f"\033[34m"
    broadcast(f"\033[32mThe user {nick} has joined.\033[0m\n".encode(), client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"{color}{nick}\033[0m > {message}")
                broadcast(f"{color}{nick}:\033[0m {message}".encode(), client_socket)
            else:
                clients.remove(client_socket)
                broadcast(f"\033[33mThe user {nick} has left.\033[0m".encode(), client_socket)
                break
        except:
            clients.remove(client_socket)
            broadcast(f"\033[31mThe user {nick} has left.\033[0m".encode(), client_socket)

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print("Connected from {}".format(client_address))
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
