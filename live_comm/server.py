import socket
import threading

HOST = "127.0.0.1"
PORT = 4000
active_clients = []


def broadcast_msg(message):
    for username, client in active_clients:
        sendmsg(client, message)
    # log file
    with open("chat_log.txt", "a") as file:
        file.write(f"{username}: {message}\n")
    file.close()


def sendmsg(client, message):
    client.sendall(message.encode("utf-8"))




def client_handler(client):
    while True:
        username = client.recv(2048).decode("utf-8")
        if username != "":
            active_clients.append((username, client))
            print(f"{username} joined the chat.")
            break
        else:
            print("Username cannot be empty.")
    threading.Thread(target=listen_for_msgs, args=(client, username)).start()


def listen_for_msgs(client, username):
    final_msg = username + "~" + "has joined the chat."
    broadcast_msg(final_msg)
    while True:
        try:
            response = client.recv(2048).decode("utf-8")
            if response != "":
                final_msg = username + "~" + response
                broadcast_msg(final_msg)
            else:
                print(f"Oops! {username}'s response cannot be empty.")
        except Exception as e:
            print(f"{username} disconnected. Error: {e}")
            final_msg = username + "~" +"has disconnected"
            broadcast_msg(final_msg)
            active_clients.remove((username, client))
            break


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except Exception as e:
        print(f"Failed to bind the server on {HOST}:{PORT} - {e}")
        exit(1)

    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == "__main__":
    main()
