import socket
import threading
from data.var import motd
import sqlite3


class main():
    pass

if __name__ == "__main__":
    print(motd)
    main()

clients = []
IP = "0.0.0.0"
PORT = 4007

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)

print("done")
print(f"\nListening on: {IP}:{PORT}")

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
    green = f"\033[32m"
    red = f"\033[31m"
    clear = f"\033[0m"
    print(f"{clear}{green}The user {nick} has joined.{clear}")
    broadcast(f"\nThe user {nick} has joined.\n".encode(), client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"{clear}{color}{nick}{clear} > {message}{clear}")
                broadcast(f"{nick} > {message}".encode(), client_socket)
            else:
                print(f"{clear}{red}The user {nick} has left.{clear}")
                clients.remove(client_socket)
                broadcast(f"\nThe user {nick} has left.\n".encode(), client_socket)
                break
        except:
            clients.remove(client_socket)
            broadcast(f"{clear}{red}The user {nick} has left.{clear}".encode(), client_socket)

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
